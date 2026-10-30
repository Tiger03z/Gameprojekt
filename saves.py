import json
import gamekeys_list

try:
    with open("save.json", "r") as fil:
        data = json.load(fil)
except (json.JSONDecodeError, FileNotFoundError):
    data = []

if data == []:
    print("wellcome new player")
    data = 
else:
    print("hi")