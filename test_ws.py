import websocket

try:
    ws = websocket.create_connection("ws://0.0.0.0:3000")
    print("Port is open")
except ConnectionRefusedError:
    print("Port is closed")
finally:
    # ws.close()
    pass
