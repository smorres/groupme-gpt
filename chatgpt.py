import openai
import os
import sys

os.environ["OPENAI_API_KEY"] = "<chatGPT_api_key>"


class ChatGPT:
    def __init__(self, api_key):
        openai.api_key = api_key

    def query(self, text):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        return response.choices[0].text.strip()

class Chatbot:
    def __init__(self, chatgpt):
        self.chatgpt = chatgpt

    def run(self):
        while True:
            try:
                # Listen for query from stdin
                query = input("> ")
            except KeyboardInterrupt:
                # Exit gracefully on Ctrl-C
                print()
                break

            # Generate response using ChatGPT
            response = self.chatgpt.query(query)

            # Output response to stdout
            print(response)

if __name__ == "__main__":
    # Initialize Chatbot with ChatGPT instance
 
    api_key = os.environ["OPENAI_API_KEY"]
    chatgpt = ChatGPT(api_key)
    chatbot = Chatbot(chatgpt)

    # Start the chatbot
    chatbot.run()