# Copyright (C) 2023 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2023 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import sys

from pyrogram import Client
import config
from ..logging import LOGGER
from pyrogram.enums import ChatMemberStatus


class AlexaBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"**• البوت بدا بالعمل الان ✅**")
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "**- تم بدء البوت بنجاح الان**"
            )
        except:
            LOGGER(__name__).error(
                "فشل الروبوت في الوصول إلى مجموعة السجل. تأكد من إضافة الروبوت الخاص بك إلى قناة السجل الخاصة بك وترقيته كمسؤول!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("يرجى رفع البوت مشرف في مجموعة السجل")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"بدأ البوت كـ {self.name}")
