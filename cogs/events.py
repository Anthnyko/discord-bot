import discord
from discord.ext import commands

print("LOADED: events")

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.banned_words = ["poo"]
        self.triggers = {
            "hello bot": "Hello there!",
            "good bot": "😊 Thanks!",
            "bad bot": "😢 I'm trying my best..."
        }

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f"Welcome to the server, {member.name}!")

    @commands.Cog.listener()
    async def on_message(self, message):
        print("EVENT FIRED")
        if message.author.bot:
            return

        # triggers
        msg = message.content.lower()
        for key, response in self.triggers.items():
            if key in msg:
                await message.channel.send(response)

        # profanity filter
        if any(word in msg for word in self.banned_words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} watch your language!")

        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Events(bot))
