# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:31:37 2018

@author: jason
"""

import discord
import asyncio
import re

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----')
    
@client.event
async def on_message(message):
    cmd = re.split("\s+",message.content)[0]
    if cmd in commands:
        await commands[cmd](message)
    
async def hello(message, **varargs):
    await client.send_message(message.channel, "Hello " + message.author.display_name )
    
commands = {'?hello' : hello}

def run():
    with open('discord.key') as fd:
        client.run(fd.read())

    
if __name__ == '__main__':
    run()