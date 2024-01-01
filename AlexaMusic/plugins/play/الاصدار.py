import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlexaMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["الاصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c4f9c850312c8891385a9.jpg",
        caption=f"""**اهلا بك عزيزي {message.from_user.mention} في اصدار سورس زد إي
★᚜ اسم سورس : زد إي

★᚜ نوع : ميوزك

★᚜ اللغه : اللغه العربيه ويدعم الانجليزيه 

★᚜ مجال العمل : بوتات تشغيل الموسيقى في الاتصال
★᚜ نظام التشغيل : كارولين بوت ميوزك
★᚜ الاصدار 1.0
★᚜ تاريخ التأسيس : 2023/11/20

★᚜ مؤسس زد إي : [ ⧛ 𓆩 𝑴𝒐𝒅𝒚 ➫ ⁽𝑆₎𝑻𝒆𝒂𝒎 ࿐ 𝑫 𝒆 𝒗 𝒊 𝒍 𓆪 ⧚](https://t.me/ELHYBA)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱", url=f"https://t.me/Source_Ze"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

