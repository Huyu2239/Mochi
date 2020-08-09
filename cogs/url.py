import re
import discord
from discord.ext import commands

class Url(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if re.findall("https?://discordapp.com/channels/[0-9]+/[0-9]+/[0-9]+", message.content):
            for message_url in re.findall("https?://discordapp.com/channels/[0-9]+/[0-9]+/[0-9]+", message.content):
                global messagess
                messagess = ""
                while True:
                    if not messagess:
                        messagess = message_url
                    if "@me" in messagess:
                        await message.channel.send(embed=discord.Embed(description=f"{message.author.mention}\nこのBotは個人チャットのメッセージは転送できません。", colour=discord.Color.dark_red()))
                        break

                    messages = messagess.split('/')
                    channels = self.bot.get_channel(int(messages[5]))
                    servers = self.bot.get_guild(int(messages[4]))
                    if not servers:
                        await message.channel.send(embed=discord.Embed(description=f"{message.author.mention}\nこのBotが参加していないサーバーのメッセージは転送できません。", colour=discord.Color.dark_red()))
                        break
                    try:
                        if "\n" in messages[6]:
                            message_id = messages[6].split('\n')[0]
                        elif messages[6].split():
                            message_id = messages[6].split()[0]
                        else:
                            message_id = messages[6]
                        msg = await channels.fetch_message(int(message_id))
                        link1 = re.findall("https?://discordapp.com/channels/[0-9]+/[0-9]+/[0-9]+", msg.content)
                        link2 = re.findall("https?://canary.discordapp.com/channels/[0-9]+/[0-9]+/[0-9]+", msg.content)
                        if link1:
                            messagess = f"{link1[0]}"
                        elif link2:
                            messagess = f"{link2[0]}"
                        else:
                            author = msg.author
                            content = msg.content
                            guild_name = msg.guild.name
                            channel_name = msg.channel.name

                            if msg.embeds and msg.embeds[0]:
                                await message.channel.send(embed=msg.embeds[0])
                                break

                            if any([True for s in ['.jpg', '.png', '.jpeg', '.tif', '.tiff', '.bmp', '.gif', '.mp4'] if s in content]):
                                embed = discord.Embed(description=f"`サーバー名: [{guild_name}] | チャンネル名: [{channel_name}]`", timestamp=msg.created_at)
                                embed.set_image(url=content)

                            elif msg.attachments and content:
                                embed = discord.Embed(description=f"`サーバー名: [{guild_name}] | チャンネル名: [{channel_name}]`\n" + content, timestamp=msg.created_at)
                                embed.set_image(url=msg.attachments[0].url)
                            elif msg.attachments:
                                embed = discord.Embed(description=f"`サーバー名: [{guild_name}] | チャンネル名: [{channel_name}]`", timestamp=msg.created_at)
                                embed.set_image(url=msg.attachments[0].url)
                            else:
                                embed = discord.Embed(description=f"`サーバー名: [{guild_name}] | チャンネル名: [{channel_name}]`\n" + content, timestamp=msg.created_at)

                            embed.set_author(name=f"メッセージの内容", url=f"https://discordapp.com/channels/{msg.guild.id}/{msg.channel.id}/{msg.id}", icon_url=msg.guild.icon_url)
                            embed.set_footer(text=f"送信元: [{author}]", icon_url=author.avatar_url)
                            await message.channel.send(embed=embed)
                            break

                    except discord.errors.Forbidden:
                        await message.author.send(embed=discord.Embed(description=f"{message.author.mention}\nメッセージを取得できませんでした。\nこのBotに閲覧権がないチャンネルのメッセージの可能性があります。", colour=discord.Color.dark_red()))
                        break

                    except discord.errors.NotFound:
                        await message.author.send(embed=discord.Embed(description=f"{message.author.mention}\nメッセージを取得できませんでした。\n既に削除された可能性があります。", colour=discord.Color.dark_red()))
                        break


def setup(bot):
    bot.add_cog(Url(bot))