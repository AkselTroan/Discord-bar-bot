# Discord-bar-bot
A discord bot that simulates being at a bar.

Due to covid-19, a lot of people are recommended to stay at home. This is where the Discord-bar bot comes in. This bot will simulate being at the bar with the same fun activity that happens within a bar.

# Introduction
Start your night in a voice channel with your mates. Head to the bar with !start. You walk into the bar and start hearing the bar ambience. A bartender greets you and asks the group to take a seat. When everyone is seated you tell the bartender that everyone is seated at the table. Then you can start ordering drinks, but beware, the bartender is counting how many drinks you've had and does not like overly drunk people in his bar! If you become too drunk the bartender will mute you for 1 minute.

If you want to challenge one of your friends at the table to take a shot you can do so. Roll the dice and if the challenger gets a 5 or 6 the victim has to take a shot, however, if the challenger gets 1-4 the challenger has to take a shot. The bartender will pour a shot for the loser.  

The bartender also has a set of "Never Have I Ever" questions. Just ask him for a statement and he will provide one.

On your table, you can see a deck of cards. The bartender knows the rules for Ring of Fire and he will gladly be the game master and guide you through the game.

> **_NOTE:_**  This is not at all a polished or finished bot. Made this because I wanted to learn discord.py and get a fun little bot to play around with my friends.

# Installation
At the time the bot is not running 24/7 on a server so you will need to run it on your own system.

Clone the repository
```
$ git clone https://github.com/AkselTroan/Discord-bar-bot.git
```
Change the working directory to Discord-Bar-Bot
```
$ cd Discord-Bar-Bot
```
Install the requirements
```
$ python3 -m pip install -r requirements.txt
```

[FFmpeg](https://ffmpeg.org/download.html) and an mp3 (Preferably with bar ambience) are required to run the bot.

Edit the code, change the marked text to the pathway of your ffmpeg.exe and bar.mp3.
![alt text](https://i.imgur.com/kvSTlw8.png)

The last step is to acquire a bot token. Go to your discord developer page and make a new bot. Go through the setup, insert your token in the code.

<div style="text-align:center"><img src="https://i.imgur.com/GLG3MXO.png" /></div>

The last thing to do is to invite your bot to your desired server and run the script.
