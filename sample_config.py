import os


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
    # The Telegram API things