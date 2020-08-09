import discord
from discord.ext import commands
from googletrans import Translator
    
class Translation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):
        if reaction.emoji == '\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER P}':
            translator = Translator()
            trans_ja = translator.translate(reaction.message.content, dest='ja')
            await reaction.message.channel.send(trans_ja.text)
            return
        if reaction.emoji == '\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}':
            translator = Translator()
            trans_en = translator.translate(reaction.message.content, dest='en')
            await reaction.message.channel.send(trans_en.text)
            return
        if reaction.emoji == '\N{REGIONAL INDICATOR SYMBOL LETTER D}\N{REGIONAL INDICATOR SYMBOL LETTER E}':
            translator = Translator()
            trans_de = translator.translate(reaction.message.content, dest='de')
            await reaction.message.channel.send(trans_de.text)
            return
def setup(bot):
    bot.add_cog(Translation(bot))