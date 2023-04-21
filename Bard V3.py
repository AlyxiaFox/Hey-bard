import os
import discord
import openai
import asyncio
# This code assumes you have your Discord token and OpenAI key in your OS environment, You can google how to do that.
# Get your Discord bot token from the Discord Developer Portal
discord_Token = os.getenv("DISCORD_TOKEN")
print('Discord key get')
# Get your OpenAI API key from the OpenAI API
API_KEY = os.getenv("OPENAI_API_KEY")
print("Open API key get")
# Do a thing to tell openAI you are using the API
openai.api_key = API_KEY
# Set the channel for the bot to work in. Also set your permissions to only allow it to talk in specific channels
# see comments to see the locations 
class Bard(discord.Client):
    async def on_ready(self):
        print('Meow!', self.user)
        channel = self.get_channel(1098980943533969508) #Put your channel ID here (the current ID will NOT work for you)
        await channel.send('Bard is now Online!')
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.channel.id != 1098980943533969508: #Put your channel ID here (the current ID will NOT work for you)
            return
        if message.content.lower().startswith("hey bard"):
            print('Message recived')
            await message.add_reaction("✅")
            await respond_to_message(message)
            

    
async def respond_to_message(message):
    print("Generating Message")
    # Get a response from the OpenAI API
    response = openai.Completion.create(
        prompt=f"{message.author.id}: {message.content[8:]}",
        engine="text-davinci-003",
        temperature=1,
        max_tokens=500,
        stop=None,
        n=1,
    )
    print(response)
    # Send the response back to the user in the form of an embed
    await message.channel.send(embed=discord.Embed(
        title="Bard's Response",
        description=f"{message.author.mention} {response['choices'][0]['text']}",
        color=0xff69b4 # You can change the color of the Embed here~
    ))
    print('Sending message embed')

    # React to the message with a thumbs up emoji
    await message.add_reaction("👍")

async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = Bard(intents=intents)
    await client.start(discord_Token)




asyncio.run(main())
