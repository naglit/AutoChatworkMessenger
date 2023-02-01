import os, sys
import json
from pychatworkAPI.pychatworkAPI import api as cwapi

# read config
backslash = ""
if os.name == "nt": 
    backslash = os.path.dirname(os.path.abspath(__file__)) + ".\\"

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
    chatwork = cwapi.Chatwork(message["api_key"])
    chatwork.send_message(message["room_id"], message["body"])

if __name__ == "__main__":
    main()
