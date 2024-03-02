import websocket
import json
import av
import cv2

from config import DEVICE_SERIAL

buffer = bytearray()

def is_h264_complete(buffer):
    # Convert the buffer to bytes
    buffer_bytes = bytes(buffer)

    # Look for the start code in the buffer
    start_code = bytes([0, 0, 0, 1])
    positions = [i for i in range(len(buffer_bytes)) if buffer_bytes.startswith(start_code, i)]

    # Check for the presence of SPS and PPS
    has_sps = any(buffer_bytes[i+4] & 0x1F == 7 for i in positions)
    has_pps = any(buffer_bytes[i+4] & 0x1F == 8 for i in positions)

    return has_sps and has_pps

def on_message(ws, message):
    # print(message)
    data = json.loads(message)
    message_type = data["type"]
    if message_type == "event" and data["event"]["event"] == "livestream video data":
        image_buffer = data["event"]["buffer"]["data"]
        print(image_buffer)
        if not is_h264_complete(image_buffer):
            print(f"Error! incomplete h264: {len(image_buffer)}")
            return

        buffer_bytes = bytes(image_buffer)
        packet = av.Packet(buffer_bytes)
        codec = av.CodecContext.create('h264', 'r')
        frames = codec.decode(packet)

        # Display the image
        for frame in frames:
            image = frame.to_ndarray(format='bgr24')
            # Put the length of the buffer on the image
            cv2.putText(image, f"Buffer Length: {len(image_buffer)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow('Image', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")

    # Send a message to the server
    ws.send(json.dumps({"messageId" : "start_listening", "command": "start_listening"}))  # replace with your command and parameters
    ws.send(json.dumps({"command": "set_api_schema", "schemaVersion" : 20}))
    ws.send(json.dumps({"messageId" : "start_livestream", "command": "device.start_livestream", "serialNumber": DEVICE_SERIAL}))  # replace with your command and parameters

    print('message sent')

if __name__ == "__main__":
    # websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:3000",  # replace with your server URI
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
