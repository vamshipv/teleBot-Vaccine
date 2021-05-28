import json

def writeJson(msg):
    with open("response.json", 'w') as f:
        json.dump(msg, f, indent=4)
