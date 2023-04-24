# Discord OpenAI Bot

This Python code implements a Discord bot that uses the OpenAI API to generate responses to user messages. The bot listens for messages starting with "hey bard" in a specific Discord channel, sends them to the OpenAI API for processing, and then replies with the generated response in an embed.

## Requirements

To use this bot, you need to have the following:

- A Discord account and a Discord bot token from the Discord Developer Portal. See [Creating a Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html#creating-a-bot-account) for instructions on how to create a bot account and get a token.
- An OpenAI account and an OpenAI API key. See [API Keys](https://beta.openai.com/docs/api-reference/authentication/api-keys) for instructions on how to get an API key.

## Installation

1. Clone this repository or download the code as a ZIP file and extract it.
2. Install the required Python packages by running `pip install -r requirements.txt` in the command line or terminal.
3. Set your Discord bot token and OpenAI API key in your OS environment variables. You can do this by following the instructions for your operating system or by using a tool like [direnv](https://direnv.net/). The environment variables are `DISCORD_TOKEN` and `OPENAI_API_KEY`, respectively.

## Usage

To use the bot, follow these steps:

1. Run the Python code by running `python bot.py` in the command line or terminal.
2. The bot should now be running and listening for messages in the Discord channel specified in the code (currently set to `1098980943533969508`). You can change this channel ID in the code to the ID of the channel you want the bot to listen in.
3. To send a message to the bot, type "hey bard" followed by your message in the Discord channel.
4. The bot should reply with a generated response from the OpenAI API in an embed. You can change the color of the embed by modifying the `color` parameter in the code.
5. The bot will add a ✅ when a messsage has been seen and has started to generate a response.
6. The bot will respond and then react to the question with a 👍 once the messsage has been responded too.

## NOTES

The whole bot works asynchronously, if multiple users are talking to the bot it will respond in the order it has been seen. And react accordingly. 

## Credits

This code was written by me and is licensed under the [MIT License](https://opensource.org/licenses/MIT). The code is based on the [Discord.py](https://github.com/Rapptz/discord.py) library and the [OpenAI API](https://beta.openai.com/docs/api-reference/introduction).
