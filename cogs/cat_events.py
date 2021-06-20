import discord
import os
import datetime
import inspect
import sqlite3
import jishaku
import json
import asyncio
import asyncpg
import aiohttp
from discord.ext import commands
from config import CROSSMARK, CHECKMARK, LOGS, PREFIX, OWNER

class cp:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        log = self.bot.get_channel(LOGS)
        await log.send(f"```{datetime.datetime.utcnow()}```\n{CHECKMARK} **Guild Create** `{guild.name}` (`{guild.id}`)\n**Owner:** {guild.owner} **Members** {guild.member_count}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        log = self.bot.get_channel(LOGS)
        await log.send(f"```{datetime.datetime.utcnow()}```\n{CROSSMARK} **Guild Delete** `{guild.name}` (`{guild.id}`)\n**Owner:** {guild.owner} **Members** {guild.member_count}")

    @commands.Cog.listener()
    async def on_ready(self):
        guild_count = 0
        for guild in self.bot.guilds:
            print("\n")
            print(f"- {guild.id} (name: {guild.name}) members: {guild.member_count} owner: {guild.owner}")
            guild_count = guild_count + 1
        print("\n\nservers: " + str(guild_count))
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"@{self.bot.user.name}"))  
        print(f"{cp.FAIL}➔ {cp.OKGREEN} {self.bot.user} is Ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == f"<@{self.bot.user.id}>" or message.content == f"<@!{self.bot.user.id}>":
            embed = discord.Embed(
                description=f"Run `{PREFIX}help` to get more informations",
                color=0x2F3136
            )
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            await message.reply(embed=embed, mention_author=False)
        if not message.guild:
            if message.author.bot:
                return
            else:
                staff = self.bot.get_channel(LOGS)
                await staff.send(f"**Author:** {message.author} ({message.author.id})\n**message:** {message.content}")
                await message.author.send(f"**Sending to staff:**\n```{message.content}```")    

def setup(bot):
    bot.add_cog(events(bot))
