import asyncio
import pathlib
import ssl
import websockets, json

async def hello(websocket, path):
    data = await websocket.recv()
    data =  json.loads(data)

    received = f"Your data : {data}!"

    await websocket.send(received)
    print(f"> {received}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.WindowsPath('C:/Users/Sahan Prabodh/key/').with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(hello, "localhost", 8765 , ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
