from datetime import datetime, timedelta
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from flask.wrappers import Response
import requests
import apiRequests

app = Flask(__name__)

# Authentication token
token = '1853149779:AAHrjUwlISb-VqGFcuK-oTu-pBjhPjhi-lI'
# https://api.telegram.org/bot<token>/setWebhook?url=<ngrokURL>
# https://api.telegram.org/bot<token>/setWebhook?url=https://f0f9359a56dd.ngrok.io

# /getMe : A simple method for testing your bot's auth token. Requires no parameters. Returns basic information about the bot in form of a User object.
# check = 'https://api.telegram.org/bot{}/getMe'.format(token)

@app.route('/', methods = ['POST'])
def hello_world():
    # resp = requests.get(check) -> returns information about our bot
    if request.method == 'POST':
        msg = request.get_json()
        # apiRequests.writeJson(msg) -> to see the structure of reponse structure
        # print(msg)
        chatID, pinCode = apiRequests.parseMsg(msg)
        if pinCode == '':
            # print(chatID)
            #sending error msg to the user
            errorMsg = 'Incorrect command format.\nsend /<6-digit Pincode>'
            apiRequests.sendMsg(chatID, errorMsg, token)
        else:
            for i in range(3):
                curDate = datetime.today() + timedelta(i)
                curDate = curDate.strftime('%d-%m-%Y')
                slots = apiRequests.getSlots(pinCode, curDate)
                if len(slots) == 0:
                    apiRequests.sendMsg(chatID, "Date: {}\nNo Slots Available".format(curDate), token)
                else:
                    finalMsg = ""
                    vis = 1
                    endLine = "--------------------------------------------------------\n"
                    for slot in slots:
                        if vis == 1:
                            title = "Available Slot for Date: {}\n".format(curDate) + "\tCenter Name: {}\n".format(slot[0]) + "\tAvailability: {}\n".format(slot[1]) + "\tAge limit: {}\n".format(slot[2]) + "\tVaccine: {}\n".format(slot[3])
                            finalMsg += title
                            finalMsg += endLine
                            vis += 1
                        else:
                            title = "\tCenter Name: {}\n".format(slot[0]) + "\tAvailability: {}\n".format(slot[1]) + "\tAge limit: {}\n".format(slot[2]) + "\tVaccine: {}\n".format(slot[3])
                            finalMsg += title
                            finalMsg += endLine
                    apiRequests.sendMsg(chatID, finalMsg, token)
            # curDate = datetime.today().strftime('%d-%m-%Y')
            # print(curDate, pinCode)
            # res = apiRequests.getSlots(pinCode, curDate)
            # print(res)
        return Response('ok', status=200) #informing telegram to we are getting response as we expected

# @app.route('/home', methods=['GET','POST'])
# def home():
#     if request.method == 'POST':
#         pinCode = request.form['pinCode']
#         date = request.form['date']
#     return render_template('home.html', pin = pinCode, da = date)
        
if __name__ == "__main__":
    app.run(debug = True)