import discord
from discord.ext import commands
import json
import emoji as EM


class Others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command()
    async def expand(self, ctx, arg=None):
        if arg == 'on' and ctx.guild.id not in self.bot.expand:
            self.bot.expand.append(ctx.guild.id)
            await ctx.send('オンにしました')
        if arg == 'off' and ctx.guild.id in self.bot.expand:
            self.bot.expand.remove(ctx.guild.id)
            await ctx.send('オフにしました')
        with open(f'{self.bot.data_directory}expand.json', 'w', encoding='utf-8') as f:
            json.dump(self.bot.expand, f, ensure_ascii=False, indent=4)

    @commands.guild_only()
    @commands.command()
    async def poll(self, ctx, *args):
        if len(args) == 0:
            await ctx.send('選択肢がありません')
            return
        if len(args) > 10:
            await ctx.send('選択肢が多すぎます')
            return
        if len(args) == 1:
            embed = discord.Embed(
                title='投票が開始されました',
                color=discord.Colour.from_rgb(255, 255, 255))
            embed.add_field(name=str(args[0]), value='‪')
            m = await ctx.send(embed=embed)
            emojis = [':o:', ':x:']
            for reac in emojis:
                reac = EM.emojize(reac, use_aliases=True)
                await m.add_reaction(reac)
            return
        emoji_list = [':zero:', ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':ten:']
        means = ''
        i = 1
        while i < len(args):
            means = f"{means}{emoji_list[i - 1]}:{args[i]}\n"
            i += 1
        embed = discord.Embed(
            title='投票が開始されました',
            description=str(args[0]),
            color=discord.Colour.from_rgb(255, 255, 255))
        embed.add_field(name="選択肢：‪", value=means)
        m = await ctx.send(embed=embed)
        i = 0
        while i < len(args) - 1:
            reac = EM.emojize(emoji_list[i], use_aliases=True)
            await m.add_reaction(reac)
            i += 1

    @commands.guild_only()
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.bot.fetch_user(payload.user_id)
        try:
            title = message.embeds[0].title
        except Exception:
            return
        # 投票以外なら処理しない
        if title != "投票が開始されました":
            return
        # 投票の選択肢の数だけループ
        for r in message.reactions:
            # 今押した絵文字以外なら
            if str(payload.emoji) != str(r.emoji):
                # ユーザーが重複していたら減らす
                async for u in r.users():
                    if user.id == u.id:
                        if user != self.bot.user:
                            await message.remove_reaction(r.emoji, user)


def setup(bot):
    bot.add_cog(Others(bot))
