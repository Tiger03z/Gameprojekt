import json
from gamekeys_list import gamekeys

def lagre(data):
    with open("save.json", "w") as fil:
        json.dump(data, fil, indent=4)

try:
    with open("save.json", "r") as fil:
        data = json.load(fil)
except (json.JSONDecodeError, FileNotFoundError):
    data = []

if data == []:
    print("wellcome new player")
    data = gamekeys
else:
    print("hi")

lagre(data)