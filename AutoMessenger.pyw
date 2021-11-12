from os import read
import requests
import configparser

# read config
config = configparser.ConfigParser()
config.read("message.cfg")
chatwork_config = config["chatwork"]

def main():
    message = read_message()
    send_message(message)

# read a text in message.txt
def read_message():
    # init
    message = {
        "roomid" : "",
        "content" : ""
    }
    content = ""

    # read
    with open('message.txt', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if ("ROOMID" in line):
                message["roomid"] = line.replace(" ", "").replace("\t", "").replace("\"", "").replace("ROOMID=", "").replace("\r\n", "").rstrip()
            else:
                content += line
        message["content"] = content
    return message

# send a message on Chatowork
def send_message(message):    
    url = chatwork_config["chatwork_url"] + '/rooms/' + message["roomid"] + '/messages?force=1'
    headers = { 'X-ChatWorkToken': chatwork_config["api_key"] }
    params = { 'body': message["content"] }

    # send a request
    resp = requests.post(url,
        headers=headers,
        params=params)

if __name__ == "__main__":
    main()