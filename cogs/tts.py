import discord
from discord.ext import commands

class tts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def join(self, message):
        await message.channel.send('–¢ŽÀ‘•‚Å‚·\n‚µ‚Î‚ç‚­‚¨‘Ò‚¿‚­‚¾‚³‚¢')
def setup(bot):
    bot.add_cog(tts(bot))