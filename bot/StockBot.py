import discord
import TOKEN
from discord.ext import commands
from discord import Guild

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send(f"`Latency: {round(bot.latency * 1000)}ms`")


# guild = Guild()

@bot.command()
async def list(ctx):
    members = ctx.guild.members
    memberList = ''
    for member in members:
        memberList += str(member) + "\n"
    memberList = f"""```c
--- MEMBERS --- 
{memberList}```"""
    await ctx.send(memberList)

bot.run(TOKEN.TOKEN)
