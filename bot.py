import os
import discord
import random
import wikipediaapi
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=">>", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'booted {bot.user.name}')

@bot.command(name="wiki", help="search wikipedia with keyword")
async def wiki(ctx, search_keyword):
    search_request = wikipediaapi.Wikipedia('en')
    search_result = search_request.page(search_keyword)
    if search_result.exists():
        await ctx.reply(search_result.fullurl)
    else:
        await ctx.reply("Your search keyword could not be found")
    

@bot.command(name="roll", help="simulates rolling dice")
async def roll_dice(ctx):
    await ctx.reply(str(random.choice(range(1, 7))))

bot.run(DISCORD_TOKEN)
