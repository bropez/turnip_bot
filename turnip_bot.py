import os

from discord.ext import commands
from dotenv import load_dotenv

from row_col_updater import update_row_col


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='turnip_tracker', help='Inputs your turnip prices into the spreadsheet.')
async def tracker(ctx, day_and_time: str, price: int):
    emoji = '\N{THUMBS UP SIGN}'
    print("updating row and col")
    update_row_col(str(ctx.author), day_and_time.lower(), price)
    await ctx.message.add_reaction(emoji)
    # await ctx.send('recorded, {}'.format(ctx.author))

bot.run(TOKEN)