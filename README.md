# Streaming Eufy Video
This repo tries out different methods of streaming video from Eufy camera

There is two main ways to do this:
1. Get stream data directly from camera
2. RTSP

RTSP seems the easiest to get started.

## NOTE: This work is still in progress

## 1. Stream from camera
This method mainly utilizes the `eufy-security-ws` package

[ eufy camera ] <--> [ eufy-security-server ] <--> [ eufy-security-client ]

1. Start `eufy-security-server`. It defaults to port 3000
2. Start `eufy-security-client`
3. Run `eufy-test.py`. It should start streaming raw data


## 2. RTSP
Take a look at `rtsp-test.py`
1. First enable RTSP on the eufy app. Camera `settings` -> `General` -> `Storage` -> `NAS(RTSP)` -> follow setup
2. They should have a RTSP link that looks like `rtsp://username:password@192.168.1.1/live0`
3. Put this into `rtsp-test.py`
