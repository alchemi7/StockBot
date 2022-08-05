import discord
import TOKEN
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")


@bot.command()
async def list(ctx):
    await ctx.send(bot.users)


bot.run(TOKEN.TOKEN)
