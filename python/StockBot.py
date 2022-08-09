import discord
from TOKEN import TOKEN
from pandas_datareader import data as pdr
from discord.ext import commands
from datetime import date
from QuoteFilter import quoteFilter

date = date.today()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command()
async def ping(ctx):
    await ctx.send(f'`Latency: {round(bot.latency * 1000)}ms`')


@bot.command()
async def list(ctx):
    members = ctx.guild.members
    memberList = ''
    for member in members:
        memberList += str(member) + "\n"
    memberList = f"""```python
--- MEMBERS --- 
{memberList}
```"""
    await ctx.send(memberList)


@bot.command()
async def doc(ctx):
    await ctx.send('`discord.py Documentation:`\nhttps://discordpy.readthedocs.io/en/stable/index.html')


@bot.command()
async def github(ctx):
    await ctx.send('`Github:`\n https://github.com/alchemi7/StockBot')


@bot.command()
async def quote(ctx, stock):
    try:
        quote = pdr.get_data_yahoo(stock, date, date).round(2).to_string()
        await ctx.send(quoteFilter(quote, stock, date))

    except Exception:
        await ctx.send("`Quote could not be found`")


bot.run(TOKEN)
