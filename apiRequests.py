import json
from typing import Pattern
from flask import Flask, request, render_template
from flask.wrappers import Response
import requests
from requests import status_codes
from requests import sessions
from werkzeug.utils import redirect
import apiRequests
import re
import datetime

def writeJson(msg):
    with open("response.json", 'w') as f:
        json.dump(msg, f, indent=4)

def getSlots(pinCode, date):
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(pinCode, date)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    records = []
    response = requests.get(URL, headers = header)
    if response.ok:
        data_json = response.json()
        # print(data_json)
        for i in data_json['sessions']:
            hospitalName = i['name']
            available = i['available_capacity']
            ageLimit = i['min_age_limit']
            brand = i['vaccine']
            records.append([hospitalName,available,ageLimit,brand])
    else:
        return ""
    return records

def parseMsg(msg):
    if 'message' in msg.keys():
        chatID = msg['message']['chat']['id']
        text = msg['message']['text']
        # print(chatID, text)
    else:
        chatID = msg['edited_message']['chat']['id']
        text = msg['edited_message']['text']
    #regular expression for validating pincode
    pattern = r'^/\d{6}$'
    match = re.findall(pattern, text) # returns list of words in msg matching the pattern

    pincode = ''
    if match:
        pincode = match[0][1:] #ignore '/'
    return chatID, pincode

def sendMsg(chatID, msg, token):
    URL = 'https://api.telegram.org/bot{}/sendMessage'.format(token)
    payload = {'chat_id' : chatID, 'text' : msg}
    requests.post(URL, json=payload)
# print(getSlots("577201", "28-5-2021"))

