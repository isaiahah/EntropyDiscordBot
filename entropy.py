import discord
import bot_secrets
import commands


client = discord.Client(activity=discord.Game(name='D&D'))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # await client.change_presence(activity=discord.Activity(name='D&D'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(bot_secrets.PREFIX):
        message_content = message.content[len(bot_secrets.PREFIX):].lower()
        response = commands.command_handler(message_content)
        if response is not None:
            await message.channel.send(response)

client.run(bot_secrets.TOKEN)
