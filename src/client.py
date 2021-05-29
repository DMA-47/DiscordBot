import os
import discord
from config import settings
from discord_slash import SlashCommand # Importing the newly installed library.
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.all())
#slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)