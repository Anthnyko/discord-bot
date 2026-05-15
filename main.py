import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import json

print("BOT INSTANCE STARTED")

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Load prefix from config
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("data/config.json"):
    with open("data/config.json", "w") as f:
        json.dump({"prefix": "!"}, f)

with open("data/config.json", "r") as f:
    prefix = json.load(f)["prefix"]

bot = commands.Bot(command_prefix=prefix, intents=intents)

initial_extensions = [
    "cogs.events",
    "cogs.fun",
    "cogs.utility",
    "cogs.social"
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for ext in initial_extensions:
        await bot.load_extension(ext)
    print("All cogs loaded!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
