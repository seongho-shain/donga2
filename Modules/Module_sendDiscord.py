from discord_webhook import DiscordWebhook

def sendDiscord(title, text):
    webhook = DiscordWebhook(
        url="https://ptb.discord.com/api/webhooks/1247907327546363934/ipGZN6er48caVdZJSe3_e_m2wGgJhyVHbO7q-YcVUBDBsnu_x5S7YM-SS3PitOCoG3yX", 
        content=f"# {title} \n{text}"
    )
    webhook.execute()