import asyncio
from functools import partial

import aiofiles
import toml
from quart import Quart, render_template, websocket

app = Quart(__name__)

lock = asyncio.Lock()

downloads = {
    "flac": "flac",
    "apple lossless": "m4a",
    "opus": "opus",
    "mp3": "mp3",
}


async def update_db(track_id, action):
    db_file = f"database/{track_id}.toml"
    async with lock:
        async with aiofiles.open(db_file, mode="r", encoding="UTF-8") as f:
            data = await f.read()
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


def download_files(track_id):
    for key, value in downloads.items():
        yield (key, f"{track_id}-download.{value}")


@app.route("/<track_id>/play")
async def play(track_id):
    track_id = track_id.lower()
    await update_db(track_id, update_play_count)
    return "counted"


@app.route("/<track_id>")
async def index(track_id):
    track_id = track_id.lower()
    entry = await update_db(track_id, update_view_count)
    entry["cover"] = f"{track_id}-cover.jpg"
    entry["stream"] = f"{track_id}-stream.mp3"
    entry["downloads"] = download_files(track_id)
    return await render_template("index.html", **entry)


if __name__ == "__main__":
    app.run()
