import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name="ping",
        usage="-",
        description="Returns bot latency",
        aliases=["latency", "pong"]
    )
    async def _ping(self, ctx):
        latency = round(self.bot.latency*1000)
        await ctx.reply(f"🏓**Pong!** `{latency}ms`", mention_author=False)


def setup(bot):
    bot.add_cog(ping(bot))
