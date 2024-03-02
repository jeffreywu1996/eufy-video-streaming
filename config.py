import os
from dotenv import load_dotenv

load_dotenv()

DEVICE_SERIAL = os.getenv("DEVICE_SERIAL")

RTSP_USERNAME = os.getenv("RTSP_USERNAME")
RTSP_PASSWORD = os.getenv("RTSP_PASSWORD")
RTSP_SERVER_IP = os.getenv("RTSP_SERVER_IP")
