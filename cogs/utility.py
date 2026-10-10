import discord
from discord.ext import commands
from discord import app_commands
import asyncio

print("LOADED: utility")

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="poll", description="Create a poll with thumbs up/down reactions")
    @app_commands.describe(message="The poll question")
    async def poll(self, interaction: discord.Interaction, message: str):
        embed = discord.Embed(
            title="New Poll",
            description=message,
            color=discord.Color.green()
        )

        await interaction.response.send_message("Poll created!", ephemeral=True)
        poll_message = await interaction.channel.send(embed=embed)

        await poll_message.add_reaction("👍")
        await poll_message.add_reaction("👎")

    @app_commands.command(name="serverinfo", description="Show information about the server")
    @app_commands.guild_only()
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild

        embed = discord.Embed(
            title="Server Info",
            color=discord.Color.blue()
        )
        embed.add_field(name="Name", value=guild.name)
        embed.add_field(name="Members", value=guild.member_count)
        embed.add_field(name="Owner", value=guild.owner)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="userinfo", description="Show information about a user")
    @app_commands.describe(member="The user to get info about")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user

        embed = discord.Embed(
            title=f"{member.name}'s Info",
            color=discord.Color.purple()
        )
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Joined", value=member.joined_at)
        embed.add_field(name="Created", value=member.created_at)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
