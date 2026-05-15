import discord
from discord.ext import commands
import asyncio

print("LOADED: utility")

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, message):
        embed = discord.Embed(title="New Poll", description=message, color=discord.Color.green())
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    @commands.command()
    async def remind(self, ctx, time: int, *, message):
        await ctx.send(f"Okay! I'll remind you in {time} seconds.")
        await asyncio.sleep(time)
        await ctx.author.send(f"Reminder: {message}")

    @commands.command()
    async def dm(self, ctx, *, message):
        await ctx.author.send(message)

    @commands.command()
    async def reply(self, ctx):
        await ctx.reply("This is a reply!")

    @commands.command()
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="Server Info", color=discord.Color.blue())
        embed.add_field(name="Name", value=ctx.guild.name)
        embed.add_field(name="Members", value=ctx.guild.member_count)
        embed.add_field(name="Owner", value=ctx.guild.owner)
        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f"{member.name}'s Info", color=discord.Color.purple())
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Joined", value=member.joined_at)
        embed.add_field(name="Created", value=member.created_at)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
