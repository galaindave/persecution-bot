import discord
from discord.ext import commads

bot = commads.Bot(commads_prefix='[')


@bot.event
async def on_ready():
    print("星爆")

bot.run('NzE5OTYyOTU1MDUxMDQwODQw.Xt_EFQ.XH4qxAHEWdkCnQCfYBjcW2qdix4')