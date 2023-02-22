from quart import Quart, render_template, websocket
import asyncio

app = Quart(__name__)

@app.route("/")
async def hello():
    return await render_template("index.html")

@app.websocket("/ws")
async def ws():
    enum=0
    while True:
        await websocket.send(f'<div id="ws-value">websocket connected {enum}</div>')
        enum+=1
        await asyncio.sleep(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
