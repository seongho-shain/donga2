from discord_webhook import DiscordWebhook, DiscordEmbed

def sendDiscord(url, title, text):
    webhook = DiscordWebhook(
        url=url,
        username="코드코리아배 BSSM 이스포츠 대회",
        content=f"# {title} \n{text}"
    )
    webhook.execute()

def sendDiscordEmbed(url, title, datetimeInfo, discordInfo, predictionInfo, teamInfo):
    webhook = DiscordWebhook(
        url=url, 
        username="코드코리아배 BSSM 이스포츠 대회"
    )

    embed = DiscordEmbed(title=title, description=f"> **코드코리아배 BSSM 이스포츠 대회 일정 안내** \n\n날짜: {datetimeInfo} \n\n디스코드: {discordInfo} \n\n승부예측: {predictionInfo}", color="2DD9FF")
    embed.set_author(name="코드코리아배 BSSM 이스포츠 대회", url="http://kodekorea.kr/", icon_url="https://yt3.googleusercontent.com/ytc/AIdro_maECWNIJe5j4Mxxd9Nbw6cRgT9Hp_rHiBWJxR6g76g3w=s176-c-k-c0x00ffffff-no-rj")
    embed.set_timestamp()
    embed.add_embed_field(name="대결 A팀", value=teamInfo[0], inline=True)
    embed.add_embed_field(name="대결 B팀", value=teamInfo[1], inline=True)

    webhook.add_embed(embed)
    webhook.execute()