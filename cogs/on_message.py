import discord
from discord.ext import commands

lists=[
    721270505621028926,
    689098603871862833,
    730043491626778775,
    730043630626144298,
    726656130654273636
]

class On_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.guild_only()  
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id==721265051729657879:
            return
        if message.channel.id==721270505621028926:
            await self.bot.get_channel(689098603871862833).send(message.content)
        if message.channel.id not in lists:
            return

        if "眠い" in message.content or "ねむい" in message.content:
            await message.channel.send("寝なさい")
            return
        if "お疲れ" in message.content or "おつかれ" in message.content:
            await message.channel.send("お疲れ様です")
            return
        if "Adobe" in message.content or "アドビ" in message.content or "adobe" in message.content:
            await message.channel.send("買いなさい（強制）")
            return
        if "進歩" in message.content or "進捗" in message.content:
            await message.channel.send("編集しなさい")
            return

def setup(bot):
    bot.add_cog(On_message(bot))