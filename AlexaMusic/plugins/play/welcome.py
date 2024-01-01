import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Client, emoji 
from AlexaMusic import app
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ChatPermissions
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####  #            #####    
#           #    #    #          #     ##   #     #
#              #      #####   ######   #     #


@app.on_message(filters.new_chat_members)
async def wel__come(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"- نورت ياا فرتكهه😘🤝️ {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}",chat_id=chatid)
	
@app.on_message(filters.left_chat_member)
async def good_bye(client: Client, message: Message):
	chatid= message.chat.id
	await client.send_message(text=f"- مشيت ليه يوحش يلا بسلامات🥲👋\n│ \n└ʙʏ  {message.from_user.mention} ",chat_id=chatid)
	
	