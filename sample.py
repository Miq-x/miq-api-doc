import base64

import requests


# Create Make Image API V3 Sample
# Powered by MaguRo 🐟 2024

# Key
key = ""

# Host ※ Do not change!
url = "http://{IP}/make"


# Text Draw
params = {
    "key"   : key,
    "param" : "makemono2#c71585",
    "name"  : "MaguRo Kawaii",
    "text"  : "Hello MaguRo",
    "id"    : "0001112222",
    "mid"   : "u66aa785c06415da8850a19a6e16c223f12345",
    "meta"  : "None",
    "stamp" : "None"
}

# Line-Sticker Draw
"""
params = {
    "key"   : "MaguRo04",
    "param" : "make",
    "name"  : "まぐふぁよ",
    "text"  : "",
    "id"    : "0001112222",
    "mid"   : "u66aa785c06415da8850a19a6e16c223f12345",
    "meta"  : "None",
    "stamp" : "22395286_571129566",
}
"""

# Line-Emoji Draw
"""
params = {
    "key"   : "MaguRo04",
    "param" : "make",
    "name"  : "まぐふぁよ",
    "text"  : "(emoji)(emoji)(emoji)",
    "id"    : "0001112222",
    "mid"   : "u66aa785c06415da8850a19a6e16c223f12345",
    "meta"  : str([{"productId":"631ebb54f1289d7e58de92e4","E":7,"resourceType":"STATIC","version":1,"sticonId":"030","S":0},{"productId":"631ebb54f1289d7e58de92e4","S":7,"E":14,"sticonId":"031","resourceType":"STATIC","version":1},{"E":21,"S":14,"resourceType":"STATIC","sticonId":"032","productId":"631ebb54f1289d7e58de92e4","version":1}]),
    "stamp" : "None",
}
"""

# Icon image
file = {
    "img": open("req.jpg", "rb")
}


# Request
try:
    res = requests.post(url, params=params, files=file, timeout=60).json()
except requests.exceptions.ReadTimeout:
    print("timeout")
    exit()


# Result
if res["status"] == "error":
    print(res["message"])
else:
    with open("res.jpg", mode="wb") as f:
        f.write(base64.b64decode(res["image"]))

    print(res["message"])


# Show Results
#print(res)
