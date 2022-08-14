import discord
import requests
from AnilistPython import Anilist
anilist = Anilist() 
from discord.ext import tasks
client=discord.Client()
from letterboxdpy import movie , user

prefix="#"


@client.event

async def on_message(message):
    if message.content.startswith(prefix + "movie"):
         movie_name= message.content.removeprefix('#movie ')
         movie_details = movie.Movie(movie_name)
         data=movie_details.jsonify()
         await message.channel.send(data)

    elif message.content.startswith(prefix + "user"):
        user_name= message.content.removeprefix('#user ')
        user_details=user.User(user_name)
        yep=user_details.jsonify()
        await message.channel.send(yep)
    
    elif message.content.startswith(prefix + "cat"):
        response=requests.get('https://aws.random.cat/meow')
        data=response.json()
        await message.channel.send(data['file'])
    
    elif message.content.startswith(prefix+"animesearch"):
        anime_name=message.content.removeprefix('#animesearch ')
        if anime_name.isnumeric():
            anime_details=anilist.get_anime_with_id(anime_name)
            await message.channel.send(anime_details)
        else:
           anime_details=anilist.get_anime(anime_name)
           await message.channel.send(anime_details)
    
    elif message.content.startswith(prefix + "dog"):
        response=requests.get('https://dog.ceo/api/breeds/image/random')
        data=response.json()
        await message.channel.send(data['message'])
        
client.run('ODg5MDY4Mzc0NzUwMDExNDAz.YUb3cg.PeualFHCwvkUPVv_VDoIgbeSqjw')
