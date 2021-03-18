from discord.ext import commands
from dispander import dispand
lists = [
    689098603871862833
]


class On_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author is self.bot.user:
            return
        if message.guild.id in self.bot.expand:
            await dispand(message)
        if message.channel.id in lists:
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
