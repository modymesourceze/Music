from AlexaMusic import app 
from pyrogram.types import ChatMemberUpdated
import pyrogram
from pyrogram import Client
from strings.filters import command 

@app.on_chat_member_updated(filters = lambda _, update: update.old_chat_member)
async def __(_, update: ChatMemberUpdated):
    user_id = update.from_user.id
    try:await update.chat.ban_member(user_id)
    except pyrogram.errors.exceptions.bad_request_400.UserAdminInvalid:...


