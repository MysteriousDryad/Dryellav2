import settings
import discord 
from discord.ext import commands
import cogs 
import os 


logger = settings.logging.getLogger('bot')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds)
    logger.info(f"{bot.user} is connected to: '{guild.name}' - (ID: {guild.id})")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")   
            

@commands.command()
@commands.dm_only()
@commands.is_owner()
async def sync(ctx):
    try:            
        
        synced = await bot.tree.sync()
        for command in bot.tree.walk_commands():
            names = f'{command.qualified_name}'
            title = f"{command.wrapped.module}"

        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                count = +1

       # ListofCogs = bot.cogs

       # for NameofCog, TheClassofCog in ListofCogs.items():
           # cog = NameofCog

        emb = discord.Embed(title="Success!", color= discord.Color.green())
        emb.add_field(name = f"Cogs loaded: {count}", value = title[5:], inline = False)
        emb.add_field(name = f"Commands: {len(list(synced))}", value = f"{names}")
        await ctx.send(embed = emb)
    
        # await ctx.send(f'``{names}`` synced successfully')
        # print(f'Synced {len(synced)} command(s)')
    except Exception as e: 
        await ctx.send("Error!")
        print(e)
bot.add_command(sync)


bot.run(settings.DISCORD_API_SECRET, root_logger=True)


