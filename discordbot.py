from discord.ext import commands
from discord.ext import tasks
import youtube_test2
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channel_sent = None

@bot.event
async def on_ready():
    send_message_every_30sec.start()
    
@tasks.loop(seconds=30)
async def send_message_every_30sec():
    #ゴブリングレートの動画検索
    channel_sent = client.get_channel(703516958028726285)
    Y = youtube_test2.Youtube("ゴブリングレート",result=0)
    TF = Y.search() in url_list
    if TF == False :
        url_list.append(Y.search())
        await channel_sent.send(Y.search())
    else:
        await channel_sent.send("失敗しました")

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
