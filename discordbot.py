from discord.ext import commands
from discord.ext import tasks
import youtube_test2
import os
import traceback

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
channel_sent = None

@client.event
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
        
client.run(token)
