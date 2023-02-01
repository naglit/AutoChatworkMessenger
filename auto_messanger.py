import os, sys
from os import read
import requests
import configparser
import json

# read config
config = configparser.ConfigParser()
backslash = ""
if os.name == "nt": 
    backslash = os.path.dirname(os.path.abspath(__file__)) + ".\\"
config.read(backslash + "message.cfg")
chatwork_config = config["chatwork"]

def main():
    message = read_message(retrieve_arg())
    send_message(message)

def retrieve_arg(): return str(sys.argv[1]) if len(sys.argv) > 1 else ""

def read_message(id):
    ''' read a text in messages.json '''
    if id == "":
        print("This script needs to take an argument.")
        return

    # read
    with open(backslash + 'messages.json', "r", encoding="utf-8") as f:
        messages = json.load(f)["messages"]
        for message in messages:
            if message["id"] == id: return message


def send_message(message):
    ''' send a message on Chatowork'''
    if message == None:
        return

    url = chatwork_config["chatwork_url"] + '/rooms/' + message["room_id"] + '/messages?force=1'
    headers = { 'X-ChatWorkToken': message["api_key"] }
    params = { 'body': message["body"] }

    # send a request
    resp = requests.post(url,
        headers=headers,
        params=params)

if __name__ == "__main__":
    main()
