from flask import Flask, request, render_template, redirect
from flask.wrappers import Response
import requests
import apiRequests

app = Flask(__name__)

# Authentication token
token = '1853149779:AAHrjUwlISb-VqGFcuK-oTu-pBjhPjhi-lI'

# https://api.telegram.org/bot<token>/setWebhook?url=<ngrokURL>
# https://api.telegram.org/bot1853149779:AAHrjUwlISb-VqGFcuK-oTu-pBjhPjhi-lI/setWebhook?url=https://f0f9359a56dd.ngrok.io

# /getMe : A simple method for testing your bot's auth token. Requires no parameters. Returns basic information about the bot in form of a User object.
check = 'https://api.telegram.org/bot{}/getMe'.format(token)

@app.route('/', methods = ['POST'])
def hello_world():
    # resp = requests.get(check) -> returns information about our bot
    if request.method == 'POST':
        msg = request.get_json()
        apiRequests.writeJson(msg)
        print(msg)
        return Response('ok', status=200) #informing telegram to we are getting response as we expected

# @app.route('/home', methods=['GET','POST'])
# def home():
#     if request.method == 'POST':
#         pinCode = request.form['pinCode']
#         date = request.form['date']
#     return render_template('home.html', pin = pinCode, da = date)
        
if __name__ == "__main__":
    app.run(debug = True)