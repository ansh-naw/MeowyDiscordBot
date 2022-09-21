import discord
import requests
from AnilistPython import Anilist
anilist = Anilist() 
from discord.ext import tasks
client=discord.Client()
import os
from letterboxdpy import movie , user
from dotenv import load_dotenv

load_dotenv()

prefix="#"

abc=os.getenv("Bot_token")
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
        embedVar = discord.Embed(title=anime_details['name_romaji'],url='https://anilist.co/anime/21483/Seraph-of-the-End-Vampire-Reign--Owaranai-Seraph/', description=anime_details['desc'], color=0x00ff00)
        embedVar.set_thumbnail(url=anime_details['cover_image'])
        await message.channel.send(embed=embedVar)
    
    elif message.content.startswith(prefix + "dog"):
        response=requests.get('https://dog.ceo/api/breeds/image/random')
        data=response.json()
        await message.channel.send(data['message'])
    
    elif message.content.startswith(prefix + "av"):
        clientProfilePicture = message.author.avatar_url
        await message.channel.send(clientProfilePicture)

 
    elif message.content.startswith(prefix +'embed'):
        embedVar = discord.Embed(title="Sex",url='https://anilist.co/user/Kratos31/', description="Chutad", color=0x00ff00)
        embedVar.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
        await message.channel.send(embed=embedVar)





client.run(abc)
