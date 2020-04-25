from discord.ext import tasks
import discord
import youtube_test2

client = discord.Client()

channel_sent = None

url_list = ["https://www.youtube.com/watch?v=U8R3AUV3uzQ"]

TOKEN = "NzAzNDU0MTc5NjI0MDkxNjU4.XqO1EA.FeMp29dm_uMbMzycocArNW5zlio"

@tasks.loop(seconds=30)
async def send_message_every_30sec():
    #ゴブリングレートの動画検索
    channel_sent = client.get_channel(602741325778911273)
    Y = youtube_test2.Youtube("ゴブリングレート",result=0)
    TF = Y.search() in url_list
    if TF == False :
        url_list.append(Y.search())
        await channel_sent.send(Y.search())
    else:
        print(Y.search())

    #グリフォンの動画検索
    channel_sent = client.get_channel(581092204815056908)
    Y = youtube_test2.Youtube("ワイルドグリフォン",result=0)
    TF = Y.search() in url_list
    if TF == False :
        url_list.append(Y.search())
        await channel_sent.send(Y.search())
    else:
        print(Y.search())

    #メガラパーンの動画検索
    channel_sent = client.get_channel(547287618543681536)
    Y = youtube_test2.Youtube("メガラパーン",result=0)
    TF = Y.search() in url_list
    if TF == False :
        url_list.append(Y.search())
        await channel_sent.send(Y.search())
    else:
        print(Y.search())

    #トライロッカーの動画検索
    channel_sent = client.get_channel(614016779294867467)
    Y = youtube_test2.Youtube("トライロッカー",result=0)
    TF = Y.search() in url_list
    if TF == False :
        url_list.append(Y.search())
        await channel_sent.send(Y.search())
    else:
        print(Y.search())


    #ミノタウロスの動画検索
    channel_sent = client.get_channel(614016856956862482)
    Y = youtube_test2.Youtube("ミノタウロス",result=0)
    TF = Y.search() in url_list
    if TF == False :
        url_list.append(Y.search())
        await channel_sent.send(Y.search())
    else:
        print(Y.search())

@client.event
async def on_ready():
    global channel_sent
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

    send_message_every_30sec.start()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
