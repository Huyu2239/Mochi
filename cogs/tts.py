import discord
from discord.ext import commands

class tts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def join(self, message):

def setup(bot):
    bot.add_cog(tts(bot))