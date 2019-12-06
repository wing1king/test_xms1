import time
import requests

# Host = 'http://10.72.17.30'
Host = 'http://119.29.1.133'
URL = "/app/voice/edit-room"


def timestamp(str_time):
    time_list = str_time.split(":")
    return int(time_list[0])*60*60 + int(time_list[1])*60


def _request():
    header = {
        "Content-Type": "text/plain",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6ImtpZC1oZWFkZXIiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE1NzYyMzIyNjQsInVpZCI6MTExMTExMTExMTF9.c5KMcdUukKZ2UkMoiF9Fgbeissx9gY2QslYKk7lww0E"
    }
    data = {"room_id": 10000, "fields": ["play_schedule", "replay_times"],
            "room": {"play_schedule": 127,
                     "replay_times": [{"start": timestamp("09:53"),
                                       "end": timestamp("09:58")}]}}
    resp = requests.post(Host+URL, json=data, headers=header)
    print(resp.text)


if __name__ == "__main__":
    _request()
