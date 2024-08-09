import base64

import requests


# Create Smash Image API V3 Sample
# Powered by MaguRo 🐟 2024

# Key
key = ""

# Host ※ Do not change!
url = "http://{IP}/smash"


# Text Draw
params = {
    "key"   : key
}


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
