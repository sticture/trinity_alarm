import asyncio
import json
import websockets
from trinity_requests import Sender

clients = set()
sender = Sender()
sender.token = 0


async def handler(websocket, path):
    clients.add(websocket)
    print(websocket)

    try:
        async for message in websocket:
            print(message)
            data = json.loads(message)
            alert = {
                'alert_type': '208',
                'time': '123',
                'img_url': '0',
                'video_url': '0',
                'data': {
                    "name": data.get("event_name","unknown")
                }
            }
            sender.send(alert)
            # for client in clients:
            #     await client.send(message)
    except Exception as e:
        print(f"exception:{e}")
    finally:
        clients.remove(websocket)


async def start_server():
    async with websockets.serve(handler, "0.0.0.0", 7866):
        await asyncio.Future()


asyncio.run(start_server())
