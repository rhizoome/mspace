import aiofiles
import toml
from quart import Quart, render_template, websocket

app = Quart(__name__)


@app.route("/")
async def index():
    async with aiofiles.open("database/file.toml", mode="r", encoding="UTF-8") as f:
        data = await f.read()
    entry = toml.loads(data)
    entry["counts"]["view"] += 1
    data = toml.dumps(entry)
    async with aiofiles.open("database/file.toml", mode="w", encoding="UTF-8") as f:
        await f.write(data)
    return await render_template("index.html", **entry)


if __name__ == "__main__":
    app.run()
