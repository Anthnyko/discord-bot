import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import json
import asyncio

print("BOT INSTANCE STARTED")
print("RUNNING FROM:", os.path.abspath(__file__))

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

async def load_extensions():
    for ext in initial_extensions:
        try:
            await bot.load_extension(ext)
            print(f"Loaded extension: {ext}")
        except Exception as e:
            print(f"Failed to load {ext}: {e}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("All cogs loaded!")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

asyncio.run(main())