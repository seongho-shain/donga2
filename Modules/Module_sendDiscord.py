from discord_webhook import DiscordWebhook

def sendDiscord(title, text):
    webhook = DiscordWebhook(
        url="https://ptb.discord.com/api/webhooks/1248676050679107716/U8mg4ZrawIEkSoj88Ygzl8Nz8WQw6VWyolebm5TuMyk5krLKAhl-phn2iwWidVDxD9z_", 
        content=f"# {title} \n{text}"
    )
    webhook.execute()