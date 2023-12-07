import asyncio
import json
import websockets
from alarm_trigger import send_alarm

clients = set()


async def handler(websocket, path):
    clients.add(websocket)
    print(websocket)

    try:
        async for message in websocket:
            print(f"ws message{message}")
            resp = send_alarm(message)
            print(f"trigger alarm resp:{resp}")
            # for client in clients:
            #     await client.send(message)
    except Exception as e:
        print(f"exception:{e}")
    finally:
        clients.remove(websocket)


async def start_server():
    async with websockets.serve(handler, "0.0.0.0", 7658):
        await asyncio.Future()


asyncio.run(start_server())
