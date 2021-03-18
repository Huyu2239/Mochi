import discord
from discord.ext import commands
from datetime import datetime


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.send('pong!')
        await msg.edit(content=f"pong!\n`{self.bot.ws.latency * 1000:.0f}ms`")

    @commands.command()
    async def about(self, ctx):
        timestamp = datetime.utcfromtimestamp(int(self.bot.user.created_at.timestamp()))
        embed = discord.Embed(title="BOT情報", description=">>> ```クリエイター（主に映像）アシスタントBotです。```", timestamp=timestamp, color=0x009193)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="導入サーバー数", value=f"`{len(self.bot.guilds)}`")
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name="総ユーザー数", value=f"`{len(set(self.bot.get_all_members()))}`")
        embed.add_field(name="動作環境", value="`TeraServer`")
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name="応答速度", value=f"`{self.bot.ws.latency * 1000:.0f}ms`")
        embed.set_footer(text="このBOTの作成日")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
