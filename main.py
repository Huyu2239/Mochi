import os
import discord
import json
from discord.ext import commands
import traceback
from dotenv import load_dotenv
load_dotenv()
if os.name == 'nt':
    data_directory = 'json\\'
else:
    data_directory = 'json/'


class Mochi(commands.Bot):
    def __init__(self, command_prefix, **options):
        self.prefix = commands.when_mentioned_or(command_prefix)
        allowed_mentions = discord.AllowedMentions(everyone=False, roles=False, users=True)
        intents = discord.Intents.all()
        super().__init__(command_prefix=self.prefix, intents=intents, allowed_mentions=allowed_mentions, **options)
        self.logch_id = 799621304303091762  # error-log
        # self.remove_command('help')
        self.data_directory = data_directory
        with open(f'{self.data_directory}expand.json') as f:
            self.expand = json.load(f)

    async def on_ready(self):
        for cog in os.listdir("./cogs"):
            if cog.endswith(".py"):
                try:
                    self.load_extension(f"cogs.{cog[:-3]}")
                except commands.ExtensionAlreadyLoaded:
                    self.reload_extension(f"cogs.{cog[:-3]}")
                except discord.ext.commands.errors.ExtensionFailed:
                    continue
        print('-----')
        print('起動')
        print('-----')
        await self.change_presence(activity=discord.Game(name="m?about"))

    async def on_command_error(self, ctx, error1):
        orig_error = getattr(error1, "original", error1)
        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        embed = discord.Embed(title='ERROR', color=discord.Colour.red())
        if isinstance(error, commands.CommandNotFound):
            embed.add_field(name='CommandNotFount', value=f'存在しないコマンドです\n```py{error_msg}```')
        await ctx.send('エラーが発生しました', embed=embed)
        print(error_msg)


if __name__ == '__main__':
    bot = Mochi(command_prefix="m?")
    bot.run(os.environ['TOKEN'])
