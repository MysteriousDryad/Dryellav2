import settings
import discord 
from discord.ext import commands
import cogs 

logger = settings.logging.getLogger('bot')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds)
    logger.info(f"{bot.user} is connected to: '{guild.name}' - (ID: {guild.id})")

    await bot.load_extension("cogs.messages")



@commands.command()
@commands.dm_only()
@commands.is_owner()
async def sync(ctx):
    try:
        synced = await bot.tree.sync()
        await ctx.send(f'Synced {len(synced)} command(s)')
        print(f'Synced {len(synced)} command(s)')
    except Exception as e: 
        await ctx.send("Error!")
        print(e)
bot.add_command(sync)

bot.run(settings.DISCORD_API_SECRET, root_logger=True)


