import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



@bot.event
async def on_ready():
    print(f'{bot.user.name} is alive and well')


@bot.command(name='id')
async def get_user_id(ctx):

    await ctx.send(ctx.author.id)

bot.run(TOKEN)