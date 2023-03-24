import os
import requests
import json
import time 
import chatgpt

bot_name = '<your_bot_name>'
bot_id = '<your_bot_id>'
access_token = '<your_groupme_access_token>'
group_id = '<your_groupme_group_id>'
os.environ["OPENAI_API_KEY"] = "<your_openai_api_key>"


def send_message(message):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': bot_id,
        'text': message,
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

def listen():
    url = 'https://api.groupme.com/v3/groups/{}/messages'.format(group_id)
    params = {
        'token': access_token,
        'limit' : 1,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['response']['count'] > 0:
        message = data['response']['messages'][0]
        if bot_name in message['text'] and message['text'].startswith(bot_name):
            gpt_question = message['text'].split(' ', 1)[1]
            chat_bot_response = chatgpt.query(gpt_question)
            send_message(chat_bot_response)
            print("sent message")

if __name__ == '__main__':
    api_key = os.environ["OPENAI_API_KEY"]
    chatgpt = chatgpt.ChatGPT(api_key)
    while True:
        listen()
        time.sleep(2)