import discord
from discord.ext import commands
import json
import os

QUOTE_FILE = "data/quotes.json"

print("LOADED: social")

class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        if not os.path.exists(QUOTE_FILE):
            with open(QUOTE_FILE, "w") as f:
                json.dump([], f)

    @commands.command()
    async def quote(self, ctx, *, text):
        with open(QUOTE_FILE, "r") as f:
            data = json.load(f)

        data.append(f"{ctx.author}: {text}")

        with open(QUOTE_FILE, "w") as f:
            json.dump(data, f)

        await ctx.send("Quote saved!")

    @commands.command()
    async def quotes(self, ctx):
        with open(QUOTE_FILE, "r") as f:
            data = json.load(f)

        if not data:
            await ctx.send("No quotes saved yet.")
            return

        await ctx.send("\n".join(data[-10:]))

async def setup(bot):
    await bot.add_cog(Social(bot))
