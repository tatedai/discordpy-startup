#coding UTF-8
import discord
from googletrans import Translator
import random

TOKEN = '704186530461384754'

client = discord.Client()
translator = Translator()

@client.event
async def on_ready():
    print('--------------')
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print('--------------')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('!trans'):
        say = message.content
        say = say[7:]
        if say.find('-') == -1:
            str = say
            detact = translator.detect(str)
            before_lang = detact.lang
            if before_lang == 'ja':
                convert_string = translator.translate(str, src=before_lang, dest='en')
                embed = discord.Embed(title='変換結果', color=0xff0000)
                embed.add_field(name='Before', value=str)
                embed.add_field(name='After', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
            else:
                convert_string = translator.translate(str, src=before_lang, dest='ja')
                embed = discord.Embed(title='変換結果', color=0xff0000)
                embed.add_field(name='Before', value=str)
                embed.add_field(name='After', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
        else:
            trans, str = list(say.split('='))
            before_lang, after_lang = list(trans.split('-'))
            convert_string = translator.translate(str, src=before_lang, dest=after_lang)
            embed = discord.Embed(title='変換結果', color=0xff0000)
            embed.add_field(name='Before', value=str)
            embed.add_field(name='After', value=convert_string.text, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith('!detect'):
        say = message.content
        s = say[8:]
        detect = translator.detect(s)
        m = 'この文字列の言語はたぶん ' + detect.lang + ' です。'
        await message.channel.send(m)

    if message.content.startswith('%help'):
        await message.channel.send('翻訳botを使いましょう \n[使い方] \n1.テキストチャンネルの #翻訳専用 へ行きます \n2.!transと打ち、半角スペースを入力します \n3.あとは知りたい単語を入力すれば日→英、英→日への変換ができます。')

    if message.content.startswith('ロケットは？'):
        await message.channel.send('wkwkさん！')

    if message.content.startswith('わぶんのせき'):
        await message.channel.send('足したもの分の掛けたもの！')


    if message.content.startswith('今日のご飯はどうだった？'):
        await message.channel.send('それはとても甘くてクリーミーな味でした')

    if message.content.startswith('今日の天気は？'):
        await message.channel.send('ggrks')

    if message.content == "眠い":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention} 寝てクレメンス")  # f文字列（フォーマット済み文字列リテラル）

    elif message.content == "投票":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたはうんちですか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "ダーツの旅":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="都道府県", description=f"{message.author.mention}さんの今日の都道府県は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[都道府県] ", value=random.choice(("北海道", "青森", "岩手", "秋田", "山形", "宮城", "福島","新潟","茨木","栃木","グンマー帝国","だ埼玉","東京","千葉","神奈川",
                      "静岡","長野","富山","石川","山梨","岐阜","愛知","滋賀","京都","三重","和歌山","大阪","兵庫","広島","岡山","鳥取",
                      "島根","山口","徳島","香川","高知","愛媛","福岡","宮崎","佐賀","長崎","熊本","鹿児島","大分","沖縄")), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!ダイレクトメッセージ":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんにダイレクトメッセージ")

#トークン記入
client.run("NzA2NDAzMTEyMDA4ODEwNTI2.Xq6qdQ.Avmvg39_rm9OSFOoUyovdURo3VY")