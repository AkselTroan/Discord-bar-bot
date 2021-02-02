import discord
import os

client = discord.Client()
welcome = open("Welcome.txt", "r")
seated = False


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.connect()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!start'):
        await message.channel.send(welcome.read())
        welcome.close()
        await join()

    if message.content.startswith('!seated'):
        await message.channel.send('Everyone is seated!')
        seated = True

    if (message.content.startswith('!sit')):
        author = str(message.author)
        author1 = author.split("#", 1)
        await message.channel.send(f'Welcome, take a seat {author1[0]}')

client.run('INSERT BOT TOKEN HERE!')
