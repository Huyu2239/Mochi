from discord.ext import commands
import async_google_trans_new


class Translation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.trans = async_google_trans_new.google_translator()

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER P}':
            trans_ja = self.trans.translate(reaction.message.content, dest='ja')
            await reaction.message.channel.send(trans_ja.text)
            return
        if reaction.emoji == '\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}':
            trans_en = self.trans.translate(reaction.message.content, dest='en')
            await reaction.message.channel.send(trans_en.text)
            return
        if reaction.emoji == '\N{REGIONAL INDICATOR SYMBOL LETTER D}\N{REGIONAL INDICATOR SYMBOL LETTER E}':
            trans_de = self.trans.translate(reaction.message.content, dest='de')
            await reaction.message.channel.send(trans_de.text)
            return


def setup(bot):
    bot.add_cog(Translation(bot))
