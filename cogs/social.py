import discord
from discord import app_commands
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

    @app_commands.command(name="quote", description="Quotes a message")
    @app_commands.describe(text = "The message you want to quote")
    async def quote(self, interaction: discord.Interaction, member: discord.Member,text:str):
        with open(QUOTE_FILE, "r") as f:
            data = json.load(f)

        data.append(f"{member}: {text}")

        with open(QUOTE_FILE, "w") as f:
            json.dump(data, f)

        await interaction.response.send_message(f"Quote Saved!", ephemeral=True)

    @app_commands.command(name="quotes", description="Show last 10 saved quotes")
    async def quotes(self, interactions: discord.Interaction):
        with open(QUOTE_FILE, "r") as f:
            data = json.load(f)
        if not data:
            await interactions.response.send_message("No saved quotes", ephemeral=True)
            return
        last_quotes = "\n".join(data[-10:])
        await interactions.response.send_message(last_quotes)

    @app_commands.command(name="ghostping", description="Ghost ping")
    @app_commands.describe(member="The user you want to ghost ping")
    @app_commands.guild_only()
    async def ghostping(self, interaction:discord.Interaction, member:discord.Member):
        await interaction.response.send_message(f"Ghost ping sent!", ephemeral=True)

        ghost_message = await interaction.channel.send(member.mention)
        await ghost_message.delete()

async def setup(bot):
    await bot.add_cog(Social(bot))
