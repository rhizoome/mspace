import asyncio

import aiofiles
import toml
from quart import Quart, render_template, websocket

app = Quart(__name__)

lock = asyncio.Lock()


async def update_db(track_id, action):
    db_file = f"database/{track_id}.toml"
    async with lock:
        async with aiofiles.open(db_file, mode="r", encoding="UTF-8") as f:
            data = await f.read()
        entry = toml.loads(data)
        assert entry["id"] == track_id
        action(entry)
        data = toml.dumps(entry)
        async with aiofiles.open(db_file, mode="w", encoding="UTF-8") as f:
            await f.write(data)
    return entry


def update_view_count(entry):
    entry["counts"]["view"] += 1


@app.route("/<track_id>")
async def index(track_id):
    track_id = track_id.lower()
    entry = await update_db(track_id, update_view_count)
    entry["cover"] = f"{track_id}-cover.jpg"
    entry["stream"] = f"{track_id}-stream.mp3"
    return await render_template("index.html", **entry)


if __name__ == "__main__":
    app.run()
