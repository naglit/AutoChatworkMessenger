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
    id = retrieve_arg()
    print(id)
    message = read_message(id)
    send_message(message)

def retrieve_arg(): return str(sys.argv[1]) if len(sys.argv) > 1 else ""

# read a text in message.txt
def read_message(id):

    if id == "":
        print("An id should be taken as an argument ")
        return

    # read
    with open(backslash + 'messages.json', "r", encoding="utf-8") as f:
        # lines = f.readlines()
        messages = json.load(f)["messages"]
        for message in messages:
            if message["id"] == id: return message

# send a message on Chatowork
def send_message(message):
    print(message)
    url = chatwork_config["chatwork_url"] + '/rooms/' + message["room_id"] + '/messages?force=1'
    headers = { 'X-ChatWorkToken': chatwork_config["api_key"] }
    params = { 'body': message["body"] }

    # send a request
    resp = requests.post(url,
        headers=headers,
        params=params)

if __name__ == "__main__":
    main()
