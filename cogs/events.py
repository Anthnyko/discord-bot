import discord
from discord.ext import commands

print("LOADED: events")

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Removed banned_words entirely
        self.triggers = {
            "hello bot": "Hello there!",
            "good bot": "😊 Thanks!",
            "bad bot": "😢 I'm trying my best..."
        }

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            await member.send(f"Welcome to the server, {member.name}!")
        except discord.Forbidden:
            # User has DMs closed
            pass

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        msg = message.content.lower()

        # Keyword triggers only
        for key, response in self.triggers.items():
            if key in msg:
                await message.channel.send(response)
                return

        # IMPORTANT:
        # Do NOT call process_commands — slash commands don't use message parsing.
        # Prefix commands are deprecated.
        # So we leave this listener as-is with no command processing.
        # await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Events(bot))
