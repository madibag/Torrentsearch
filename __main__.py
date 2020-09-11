#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K


import os

import (
    TG_BOT_TOKEN
)
from pyrogram import (
    Client,
    filters
)
from pyrogram.handlers import (
    MessageHandler,
    CallbackQueryHandler
)
from bot import (
    magnet_link_s
)


if __name__ == "__main__" :
    # create download directory, if not exist
    #
    app = Client(
        ":memory:",
        bot_token=TG_BOT_TOKEN
    )
    #
    app.set_parse_mode("html")
    #
    # PURGE command
    incoming_message_handler = MessageHandler(
        magnet_link_s,
        filters=Filters.command(["Magnet"]) & Filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(incoming_message_handler)

    # run the APPlication
    app.run()
