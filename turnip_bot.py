import os

from discord.ext import commands
from dotenv import load_dotenv

from row_col_updater import update_row_col


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='ttracker', help='Inputs your turnip prices into the spreadsheet.')
async def tracker(ctx, day_and_time: str, price: int):
    emoji = '\N{THUMBS UP SIGN}'
    print("updating row and col")
    update_row_col(str(ctx.author), day_and_time.lower(), price)
    await ctx.message.add_reaction(emoji)


@bot.command(name='ttracker_name', help="Inputs someone else's turnip prices into the spreadsheet.")
async def tracker2(ctx, day_and_time: str, price: int, name: str):
    emoji = '\N{THUMBS UP SIGN}'
    print("updating row and col")
    update_row_col(name, day_and_time.lower(), price)
    await ctx.message.add_reaction(emoji)


@bot.command(name='tlink', help='Links to the turnip tracker spreadsheet.')
async def linker(ctx):
    link = 'https://docs.google.com/spreadsheets/d/17wQSnRnS9_s7lbMCJZvl1FNRkAWlPlRDnwHMDPV0QRY/edit?usp=sharing'
    await ctx.send('{}'.format(link))

bot.run(TOKEN)