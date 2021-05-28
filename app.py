from flask import Flask, request
from flask.wrappers import Response
import requests
import apiRequest


app = Flask(__name__)

# Authentication token
token = '1853149779:AAHrjUwlISb-VqGFcuK-oTu-pBjhPjhi-lI'

# https://api.telegram.org/bot<token>/setWebhook?url=<ngrokURL>

# /getMe : A simple method for testing your bot's auth token. Requires no parameters. Returns basic information about the bot in form of a User object.
check = 'https://api.telegram.org/bot{}/getMe'.format(token)

@app.route('/', methods = ['POST'])
def hello_world():
    # resp = requests.get(check) -> returns information about our bot
    if request.method == 'POST':
        msg = request.get_json()
        apiRequest.writeJson(msg)
        print(msg)
        return Response('ok', status = 200)

if __name__ == "__main__":
    app.run(debug = True)