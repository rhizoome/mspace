import asyncio
from functools import partial

import aiofiles
import toml
from quart import Quart, abort, render_template, websocket

app = Quart(__name__)

lock = asyncio.Lock()

downloads = {
    "mp3": "mp3",
    "flac": "flac",
    "alac": "m4a",
    "wav": "wav",
}


async def update_db(track_id, action):
    db_file = f"database/{track_id}.toml"
    async with lock:
        try:
            async with aiofiles.open(db_file, mode="r", encoding="UTF-8") as f:
                data = await f.read()
        except FileNotFoundError:
            abort(404)
        entry = toml.loads(data)
        assert entry["track_id"] == track_id
        action(entry)
        data = toml.dumps(entry)
        async with aiofiles.open(db_file, mode="w", encoding="UTF-8") as f:
            await f.write(data)
    return entry


def update_count(field, entry):
    entry["counts"][field] += 1


update_view_count = partial(update_count, "view")
update_play_count = partial(update_count, "play")
update_download_count = partial(update_count, "download")


def download_files(entry):
    track_id = entry["track_id"]
    title = entry["title"]
    yield ("soundcloud", entry["soundcloud"], None)
    yield ("bandcamp", entry["bandcamp"], None)
    for key, value in downloads.items():
        yield (key, f"{track_id}-download.{value}", f"{title}.{value}")


async def page(track_id, count=False):
    track_id = track_id.lower()
    if count:
        entry = await update_db(track_id, update_view_count)
    else:
        entry = await update_db(track_id, lambda x: None)
    entry["cover"] = f"{track_id}-cover.jpg"
    entry["stream"] = f"{track_id}-stream.mp3"
    entry["downloads"] = download_files(entry)
    return await render_template("index.html", **entry)


@app.route("/<track_id>/play")
async def play(track_id):
    track_id = track_id.lower()
    await update_db(track_id, update_play_count)
    return "counted"


@app.route("/<track_id>/download")
async def download(track_id):
    track_id = track_id.lower()
    await update_db(track_id, update_download_count)
    return "counted"


@app.route("/<track_id>/view")
async def index(track_id):
    return await page(track_id, count=False)


@app.route("/<track_id>")
async def view(track_id):
    return await page(track_id, count=True)


if __name__ == "__main__":
    app.run()
