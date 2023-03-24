# Project Overview
## This project contains two Python scripts, chatgpt.py and groupmegpt.py, that work together to create a chatbot using the OpenAI GPT-3 language model. The chatbot is designed to be used in a GroupMe chat, where it listens for messages that begin with a specific bot name and then responds to those messages using the chatgpt.py script.


# Getting Started
## Prerequisites
Before running this project, you will need:

- An OpenAI API key to use the GPT-3 language model. You can get an API key from the OpenAI website.
- A GroupMe account and a bot set up for your group. You can create a new bot by going to dev.groupme.com/bots.

## Installation
1. Clone the repository to your local machine.
2. Install the required packages by running pip install -r requirements.txt in the project directory.
3. Set the OPENAI_API_KEY, bot_name, bot_id, access_token, and group_id variables in the groupmegpt.py script to match your environment.


## Usage
To use the chatbot, run the 'groupmegpt.py' script in your terminal with the command 'python groupmegpt.py'. The chatbot will start listening for messages in your GroupMe chat and responding to any messages that start with the specified bot name.

To customize the behavior of the chatbot, you can modify the 'chatgpt.py' script. Specifically, you can adjust the 'max_tokens', 'n', 'stop', and 'temperature' parameters in the query method of the ChatGPT class to change how the GPT-3 language model generates responses.

## GPT Only
If you are only using chatgpt.py, you just need to update the 'os.environ["OPENAI_API_KEY"] = "<chatGPT_api_key>"'

running 'python chatgpt.py' from command line allow you to have a conversation with the chatgpt api on your terminal directly, not through groupme.
