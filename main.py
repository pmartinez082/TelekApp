# Dependencias
import os, discord
from dotenv import load_dotenv
from discord.ext import commands

# Creo que es obvio que solo sacamos el fakin token del .env pero vaya
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Intents, los usos que puede hacer un bot
# Los que ponemos en true aquí son los que usa. Los demás se desactivan. Security is my motto.
intents = discord.Intents.default()
intents.message_content = True

# Loggeamos el bot con el token del .env
bot =  discord.Client(intents=intents)

# Eventos a los que el bot responde
@bot.event
# Mensaje con string específica
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "Hello World!":
        print("Omg omg they said the thing")
        await message.channel.send("La tuya por si acaso")
    elif message.content == "lol":
        print("ew hueles a otaku")
        await message.channel.send("Dúchate, lolero")
    elif message.content == "Cine":
        print("ABSOLUTE CINEMA")
        await message.channel.send("https://tenor.com/view/me-atrapaste-es-cine-its-cinema-cinema-esto-es-cine-gif-17729711691959966457")


# Por algún motivo que aun no entiendo esto tiene que ir al final
bot.run(DISCORD_TOKEN)