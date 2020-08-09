import discord
from discord.ext import commands 
import traceback 
import asyncio
from discord.ext import tasks
import json

with open('setting.json', mode='r', encoding='utf-8') as sett:
    set_json = sett.read()
    set_json = str(set_json).replace("'", '"').replace('True', 'true').replace('False', 'false')
    token = json.loads(set_json)['bot_status']['token']
    prefix = json.loads(set_json)['bot_status']['prefix']
loop = asyncio.new_event_loop()

INITIAL_EXTENSIONS = [
    'info',
    'on_message',
    'pole',
    'translation',
    'url'
]

async def run():
    bot = MyBot()
    try:
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.logout()

class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(prefix), loop=loop)
        self.remove_command('help')

    async def on_ready(self):
        for extension in INITIAL_EXTENSIONS:
            try:
                self.load_extension(f"cogs.{extension}")
            except commands.ExtensionAlreadyLoaded:
                self.reload_extension(f"cogs.{extension}")
        await self.change_presence(activity=discord.Game(name=f"{prefix}about"))
    
    async def on_guild_join(self, _):
        await self.change_presence(activity=discord.Game(name=f"{prefix}about"))

    async def on_guild_remove(self, _):
        await self.change_presence(activity=discord.Game(name=f"{prefix}about"))

    async def on_command_error(self, ctx, error1):
        if isinstance(error1, (commands.CommandNotFound, commands.CommandInvokeError)):
            return

if __name__ == '__main__':
    try:
        print('-----')
        print('進捗だめです')
        print('-----')
        main_task = loop.create_task(run())
        loop.run_until_complete(main_task)
        loop.close()

    except Exception as error:
        print("エラー情報\n" + traceback.format_exc())
