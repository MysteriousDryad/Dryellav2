import discord 
from discord.ext import commands 


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.hybrid_command(name = "hello")
    async def hello(self, ctx):
        await ctx.send(f'Hello!')
    
async def setup(bot: commands.Bot) -> None:
   await bot.add_cog(Messages(bot))

