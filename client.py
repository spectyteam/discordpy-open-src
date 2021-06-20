import discord
from discord.ext import commands as gateway
import os
from config import TOKEN, PREFIX, OWNER

class cp:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'

bot = gateway.Bot(

    command_prefix=gateway.when_mentioned_or(PREFIX),
     owner_id=OWNER, 
     case_insensitive=True,
     shard_count=1, 
     shard_id=0, 
     intents=discord.Intents().all(),
     self_bot=False,
     activity=discord.Activity(type=3, name=f"Connecting..."),
     help_command=None
     )


for fil in os.listdir('./cogs'):
    if fil.endswith('.py'):
        try:
            bot.load_extension(f"cogs.{fil[:-3]}")
            
            print(f"{cp.FAIL}➔ {cp.OKGREEN}{fil} Loaded")

        except Exception as e:
            
            print(f"❌ {e}")


bot.run(
    TOKEN, 
    reconnect=True, 
    bot=True
    )
