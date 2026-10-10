import discord
from discord.ext import commands
from discord import app_commands
import random
import aiohttp

print("LOADED: fun")

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ---------------------------
    # Dice
    # ---------------------------
    @app_commands.command(name="dice", description="Roll a 6-sided dice")
    async def dice(self, interaction: discord.Interaction):
        roll = random.randint(1, 6)
        await interaction.response.send_message(f"You rolled a {roll}!")

    # ---------------------------
    # Coinflip
    # ---------------------------
    @app_commands.command(name="coinflip", description="Flip a coin")
    async def coinflip(self, interaction: discord.Interaction):
        await interaction.response.send_message(random.choice(["Heads", "Tails"]))

    # ---------------------------
    # Eightball
    # ---------------------------
    @app_commands.command(name="eightball", description="Ask the magic 8-ball a question")
    @app_commands.describe(question="The question you want to ask the 8-ball")
    async def eightball(self, interaction: discord.Interaction, question: str):
        responses = [
            "Yes", "No", "Maybe", "Definitely", "Absolutely not",
            "Ask again later", "I don't think so", "100% yes"
        ]
        answer = random.choice(responses)
        await interaction.response.send_message(
            f"**Question:** {question}\n**Answer:** {answer}"
        )

    # ---------------------------
    # Roast
    # ---------------------------
    @app_commands.command(name="roast", description="Roast a server member")
    @app_commands.describe(member="The server member you want to roast")
    async def roast(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        roasts = [
            "You're not stupid — you just have bad luck thinking.",
            "If I wanted to kill myself, I'd climb your ego and jump to your IQ.",
            "You have the charisma of a damp sock."
        ]
        await interaction.response.send_message(
            f"{member.mention} {random.choice(roasts)}"
        )

    # ---------------------------
    # Compliment
    # ---------------------------
    @app_commands.command(name="compliment", description="Give a friendly compliment")
    @app_commands.describe(member="The server member you want to compliment")
    async def compliment(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        compliments = [
            "You're awesome.",
            "You're smarter than you think.",
            "You make the server better."
        ]
        await interaction.response.send_message(
            f"{member.mention} {random.choice(compliments)}"
        )

    # ---------------------------
    # Meme
    # ---------------------------
    @app_commands.command(name="meme", description="Fetch a random meme from Reddit")
    async def meme(self, interaction: discord.Interaction):
        await interaction.response.defer()
        async with aiohttp.ClientSession() as session:
            async with session.get("https://meme-api.com/gimme") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    await interaction.followup.send(data["url"])
                else:
                    await interaction.followup.send("Failed to fetch a meme.")

    # ---------------------------
    # Dog
    # ---------------------------
    @app_commands.command(name="dog", description="Get a random dog image")
    async def dog(self, interaction: discord.Interaction):
        await interaction.response.defer()
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    await interaction.followup.send(data["message"])
                else:
                    await interaction.followup.send("Failed to fetch a dog picture.")

    # ---------------------------
    # Cat
    # ---------------------------
    @app_commands.command(name="cat", description="Get a random cat image")
    async def cat(self, interaction: discord.Interaction):
        await interaction.response.defer()
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    await interaction.followup.send(data[0]["url"])
                else:
                    await interaction.followup.send("Failed to fetch a cat picture.")

async def setup(bot):
    await bot.add_cog(Fun(bot))
