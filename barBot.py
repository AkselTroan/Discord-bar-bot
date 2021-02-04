
import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from youtube_dl import *
import time
import random

import os


##########################
##### Shot challenge
#     Buy fiter
#     Drink tracker
#
#####

#client = discord.Client() # This might ruin everything
client = commands.Bot(command_prefix='!')

rwelcome = open("Welcome.txt", "r")
welcome = rwelcome.read()
rwelcome.close()

rhelplist = open("Commands.txt", "r")
helplist = rhelplist.read()
rhelplist.close()

rmenu = open("Menu1.txt", "r")
menulist = rmenu.read()
rmenu.close()

openDrinks = ["Tuborg", "IPA", "Stout", "Wine", "Cider", "Shot"]
members = []
isSeated = False
URL = 'https://www.youtube.com/watch?v=ZSrVznkaMEM'  # Bar Ambiance


class Member:  # Class for each member in the voice channel. Keeping track of sit sate and drink count

    def __init__(self, name):
        self.name = name
        self.isSeated = False
        self.drink = []

    def add_drink(self, drink):
        self.drink.append(drink)

    def drink_count(self):
        return len(self.drink)

    def sits(self):
        self.isSeated = True


@client.event
async def on_ready():
    print('Bot online.')


@client.command(pass_context=True)  # Bot join the voice channel
async def start(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()


    vc.play(discord.FFmpegPCMAudio(executable="D:/Koding/Python/BarBot/ffmpeg-2021-02-02-git-2367affc2c-full_build/bin/ffmpeg.exe", source='D:/Koding/Python/BarBot/bar_ambiance.mp3'))

    await ctx.message.channel.send(welcome)  # Outputs welcome text to current text channel


@client.command()  # Bot leaving the voice channel
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.command()
async def sit(message):  # This is the first command users will put. We will add every member to a list of objects
    author = str(message.author).split("#", 1)
    member = Member(author[0])
    duplicate = False

    global members
    global isSeated

    for obj in members:
        if obj.name == member.name:
            await message.channel.send("You're already seated!")
            duplicate = True

    if duplicate is False and isSeated is False:
        await message.channel.send(f'Welcome, take a seat {author[0]}')
        member.sits()
        members.append(member)

    elif duplicate is False and isSeated is True:
        await message.channel.send("I'm sorry the table is full. Let me see if I a can find a extra chair. Wait here")
        time.sleep(10)
        await message.channel.send("Aaaa found a chair")
        await message.channel.send('Here you go, enjoy!')
        member.sits()
        members.append(member)  # Append this new member to members



@client.command()
async def seated(message):
        global isSeated

        if isSeated is False:
            isSeated = True
            await message.channel.send('Everyone is seated!')
            await message.channel.send('If you guys want to see a menu please let me know (!menu)')

        else:
            await message.channel.send('You are already seated at the table. Are you already drunk?')


@client.command()
async def menu(message):
    global menulist
    await message.channel.send(menulist)


@client.command()
async def barhelp(message):
    await message.channel.send(helplist)


@client.command()
async def buy(message, drink):
    author = str(message.author).split("#", 1)
    member = Member(author[0])
    for obj in members:
        if obj.name == member.name:
            member = obj

    if drink in openDrinks:
        await message.channel.send(f"{author[0]} just bought a {drink}! Enjoy my dude")
        member.add_drink(drink)
    else:
        await message.channel.send(f"I'm sorry {author[0]}, I don't think we have that drink in the bar")


@client.command()
async def amidrunk(message):
    author = str(message.author).split("#", 1)
    member = Member(author[0])
    for obj in members:
        if obj.name == member.name:
            member = obj
    await message.channel.send(f"You've had {member.drink_count()} drink(s). These were: {', '.join(member.drink)}")
    if member.drink_count() <= 2:
        await message.channel.send("You are not to drunk you can stay a bit more")


@client.command()
async def shot(message, victim):
    author = str(message.author).split("#", 1)
    vicMember = Member(victim)
    isVicMember = False
    for obj in members:
        if obj.name == vicMember.name:
            vicMember = obj
            isVicMember = True

    if isVicMember is False:
        await message.channel.send(f"I did not the who you challenged. Try using their Discord name and not nickname")

    elif isVicMember is True:
        await message.channel.send(f"{author[0]} challenges {victim} for a shot. Roll 5 or 6 to win")
        randomroll = random.randint(1, 6)
        if randomroll > 4:
            await message.channel.send(f"{author[0]} rolls a {randomroll}! {victim} loses to do a shot!")
            member = Member(author[0])
            for obj in members:
                if obj.name == member.name:
                    member = obj
            member.add_drink("Shot")

            await message.channel.send(f"I have added one Shot to {author[0]}'s drinks")
        else:
            await message.channel.send(f"{author[0]} rolls a {randomroll}... {author[0]} do a shot!")
            vicMember.add_drink("Shot")
            await message.channel.send(f"I have added one Shot to {vicMember}'s drinks")


client.run('INSERT TOKEN')

