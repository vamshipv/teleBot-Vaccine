from flask import Flask, request, render_template
from flask.wrappers import Response
import requests
from werkzeug.utils import redirect
import apiRequests


app = Flask(__name__)

# Authentication token
token = '1853149779:AAHrjUwlISb-VqGFcuK-oTu-pBjhPjhi-lI'

# https://api.telegram.org/bot<token>/setWebhook?url=<ngrokURL>

# /getMe : A simple method for testing your bot's auth token. Requires no parameters. Returns basic information about the bot in form of a User object.
check = 'https://api.telegram.org/bot{}/getMe'.format(token)

@app.route('/')
def hello_world():
    return render_template('home.html')
    # resp = requests.get(check) -> returns information about our bot
    # if request.method == 'POST':
    #     msg = request.get_json()
    #     apiRequests.writeJson(msg)
    #     print(msg)
    #     return Response('ok', status = 200)

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        pinCode = request.form['pinCode']
        date = request.form['date']
    return render_template('home.html', pin = pinCode, da = date)
        


if __name__ == "__main__":
    app.run(debug = True)