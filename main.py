import settings
import discord 
from discord.ext import commands

logger = settings.logging.getLogger('bot')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds)
    logger.info(f"{bot.user} is connected to: '{guild.name}' - (ID: {guild.id})")

@commands.command()
async def ping(ctx):
    await ctx.send("pong")
bot.add_command(ping)

bot.run(settings.DISCORD_API_SECRET, root_logger=True)