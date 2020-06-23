import discord
from discord.ext import commands
import asyncio
from datetime import datetime 
from discord.ext import tasks
from googletrans import Translator
import os
import traceback

bot = commands.Bot(command_prefix='M?',help_command=None)
bot.remove_command("help")

@bot.listen()
async def on_ready():
    print("にゃーん")
    now=datetime.now().strftime('%Y/%m/%d %H:%M')
    print(now)
    await bot.change_presence(activity=discord.Game(name=f"M?help | {len(bot.guilds)}guilds"))

@bot.command()
async def help(ctx):
    await ctx.send('未実装')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.listen()
@commands.guild_only()
async def on_message(message):
    if message.author.id==721265051729657879:
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
    if message.channel.id==721270505621028926:
        await client.get_channel(689098603871862833).send(message.content)


@bot.event
async def on_reaction_add(reaction, user):
#all
    if reaction.emoji == '\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER A}':
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

@bot.listen()
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    error_msg = "```py\n" + error_msg + "\n```"
    await ctx.send(error_msg)

firstad = '2020/06/14 20:00'
@tasks.loop(seconds=60)
async def loop():
    if not bot.is_ready():
        return
    now=datetime.now().strftime('%Y/%m/%d %H:%M')
loop.start()
bot.run("NzIxMjY1MDUxNzI5NjU3ODc5.XuSA7Q.idN0voFd_DnBM8t2nZDKPdURPlc")