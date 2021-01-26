import pathlib
import ssl

from websocket import create_connection
import json

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
localhost_pem = pathlib.WindowsPath('C:/Users/Sahan Prabodh/key/').with_name("localhost.pem")
ssl_context.load_verify_locations(localhost_pem)

ws = create_connection("ws://localhost:8765", ssl=ssl_context)
print("Sending message")
ws.send(json.dumps([json.dumps({'name': 'sahan', 'app': '1', 'versions': ['1', 'pre2', 'pre1']})]))

print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()

