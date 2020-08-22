import discord
from discord.ext import commands

lists=[
    721270505621028926,
    689098603871862833,
    730043491626778775,
    730043630626144298,
    726656130654273636
]

contents = {
    "寝なさい": ["眠い", "ねむい"],
    "お疲れ様です": ["つかれ", "疲れ"],
    "買いなさい（強制）": ["Adobe","adobe","あどび","アドビ"],
    "編集しなさい":["進捗","進歩"]
}

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
        
        content = "おつかれ～"

        for key, item in contents.items():
            for i in item:
                if i in message.content:
                    await message.channel.send(key)
                    break


def setup(bot):
    bot.add_cog(On_message(bot))
