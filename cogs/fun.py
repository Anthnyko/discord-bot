import discord
from discord.ext import commands
import random
import aiohttp

print("LOADED: fun")

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        await ctx.send(f"You rolled a {random.randint(1, 6)}!")

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send(random.choice(["Heads", "Tails"]))

    @commands.command()
    async def eightball(self, ctx, *, question):
        responses = [
            "Yes", "No", "Maybe", "Definitely", "Absolutely not",
            "Ask again later", "I don't think so", "100% yes"
        ]
        await ctx.send(random.choice(responses))

    @commands.command()
    async def roast(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        roasts = [
            "You're not stupid — you just have bad luck thinking.",
            "If I wanted to kill myself, I'd climb your ego and jump to your IQ.",
            "You have the charisma of a damp sock."
        ]
        await ctx.send(f"{member.mention} {random.choice(roasts)}")

    @commands.command()
    async def compliment(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        compliments = [
            "You're awesome.",
            "You're smarter than you think.",
            "You make the server better."
        ]
        await ctx.send(f"{member.mention} {random.choice(compliments)}")

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://meme-api.com/gimme") as resp:
                data = await resp.json()
                await ctx.send(data["url"])

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                data = await resp.json()
                await ctx.send(data["message"])

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
                data = await resp.json()
                await ctx.send(data[0]["url"])

async def setup(bot):
    await bot.add_cog(Fun(bot))
