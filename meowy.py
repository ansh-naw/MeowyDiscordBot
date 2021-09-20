import discord
import requests
from discord.ext import tasks
client = discord.Client()



@client.event
async def on_message(message):
     prefix="!"   
     if message.content.startswith(prefix + 'cat'):
            @tasks.loop(minutes = 10) # repeat after every 10 seconds
            async def myLoop():
             response = requests.get('https://aws.random.cat/meow')
             data = response.json()
             await message.channel.send(data['file'])
            myLoop.start()
     if message.content.startswith(prefix + "stop"):
          
               myloop.stop()
     
client.run('ODg5MDY4Mzc0NzUwMDExNDAz.YUb3cg.PeualFHCwvkUPVv_VDoIgbeSqjw')