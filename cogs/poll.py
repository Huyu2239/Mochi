import discord
from discord.ext import commands

class Pole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("m?poll "):
            emoji_list = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟️']
            vote_list = message.content[len("m?poll "):].split()
            vote_list_count = []
            result_str = '‪'
            count=len(vote_list)
            if count==1:
                embed = discord.Embed(title='投票が開始されました',color=discord.Colour.from_rgb(255,255,255))
                embed.add_field(name=vote_list[0],value='‪')
                m = await message.channel.send(embed=embed)
                await m.add_reaction('〇')
                await m.add_reaction('✕')
                return
            if count>10:
                return await message.channel.send('選択肢が多すぎます')
            for i in range(len(vote_list)):
                q=i+1
                if q==count:
                    break
                result_str = result_str + str(i) + "：" + vote_list[q] + "\n"
                vote_list_count.append(0)
            embed = discord.Embed(title='投票が開始されました',description=str(vote_list[0]),color=discord.Colour.from_rgb(255,255,255))
            embed.add_field(name="選択肢：‪",value=result_str)
            m = await message.channel.send(embed=embed)
            for i in range(len(vote_list)):
                q=i+1
                if q==count:
                    break
                await m.add_reaction(emoji_list[i])

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.bot.fetch_user(payload.user_id)
        # 投票以外なら処理しない
        if not ("投票が開始されました" in message.embeds[0].title):
            return
        # 投票の選択肢の数だけループ
        for r in message.reactions:
            # 今押した絵文字以外なら
            if str(payload.emoji) != str(r.emoji):
                # ユーザーが重複していたら減らす
                async for u in r.users():
                    if user.id == u.id:
                        if user.id != 721265051729657879:
                            await message.remove_reaction(r.emoji, user)

def setup(bot):
    bot.add_cog(Pole(bot))