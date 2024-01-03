from AlexaMusic import app 
from pyrogram import Client, filters 
from pyrogram.types import Message, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button
from pyrogram.errors import exceptions
from pyrogram.enums import ParseMode
from math import sqrt
from typing import Union



@app.on_message(filters.regex(r"^(الحاسبه|الحاسبة|الآله الحاسبه|الآلة الحاسبة|الآله|الآلة)$"))
async def start(_: Client, message: Message) -> None:
   user_id: int = message.from_user.id
   caption: str = "- ادخل عمليتك...\n|"
   info = await app.get_chat(6581896306)
   markup: Keyboard = Keyboard([
       [Button("AC", "c"), Button("DEL", "DEL"), Button(info.first_name, url=f"{info.username}.t.me")], 
       [Button("√", "sqrt("), Button("^", "**"), Button("(", "("), Button(")", ")")],
       [Button("7", "7"), Button("8", "8"), Button("9", "9"), Button("÷", "/")],
       [Button("4", "4"), Button("5", "5"), Button("6", "6"), Button("×", "*")],
       [Button("1", "1"), Button("2", "2"), Button("3", "3"), Button("-", "-")],
       [Button(".", "."), Button("0", "0"), Button("=", "="), Button("+", "+")],
       [Button("- Hide Calculator -", f"d {user_id}")]
   ])
   await message.reply(caption, reply_markup=markup, reply_to_message_id=message.id)


@app.on_callback_query(filters.regex(r"^(c)$"))
async def clear(_: Client, callback: CallbackQuery) -> None:
    user_id: int = callback.from_user.id 
    caption: str = "- ادخل عمليتك...\n|"
    markup: Keyboard = callback.message.reply_markup
    if int(markup.inline_keyboard[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    try:await callback.edit_message_text(caption, reply_markup=markup)
    except exceptions.bad_request_400.MessageNotModified:await callback.answer("- لايوجد مدخلات لحذفها..\n|")


@app.on_callback_query(filters.regex(r"^(DEL)$"))
async def rm(_: Client, callback: CallbackQuery):
    user_id: int = callback.from_user.id 
    text: str = callback.message.text
    markup: Keyboard = callback.message.reply_markup
    if int(markup.inline_keyboard[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    elif text.endswith("|"): return await callback.answer("- لا شئ ليتم حذفه.")
    caption: str = text[:-1] if len(text.split("\n")[1]) > 1 else text[:-1] + "|"
    return await callback.edit_message_text(caption, reply_markup=markup)


@app.on_callback_query(filters.regex(r"^(0|1|2|3|4|5|6|7|8|9)$"))
@app.on_callback_query(filters= lambda _, callback: callback.data in "+**/-sqrt()^.=")
async def _input(_: Client, callback: CallbackQuery) -> None:
    user_id: int = callback.from_user.id
    markup: Keyboard = callback.message.reply_markup.inline_keyboard
    if int(markup[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    elif callback.data == "=": return await callback.answer("- أدخل عمليه أولا...\n|", show_alert=True)
    caption: str = f"{callback.message.text.replace('|', '')}{callback.data}"
    markup[-2][-2].callback_data = "result " + caption.split('\n', 1)[-1]
    await callback.edit_message_text(caption, reply_markup=Keyboard(markup), parse_mode=ParseMode.HTML)


@app.on_callback_query(filters.regex(r"^(result)"))
async def _result(_: Client, callback: CallbackQuery) -> None:
    user_id: int = callback.from_user.id
    data: str = callback.data
    markup: Keyboard = callback.message.reply_markup
    if int(markup.inline_keyboard[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    markup.inline_keyboard[-2][-2].callback_data = "="
    try:result: Union[int, float] = eval(data.split(maxsplit=1)[1])
    except ZeroDivisionError: return await callback.answer("- لا يمكنك القسمه على صفر", show_alert=True)
    except SyntaxError: return await callback.answer("- تأكد من كتابة العمليه بشكله صحيح", show_alert=True)
    caption: str = f"- ناتج العمليه...\n{result}"
    await callback.edit_message_text(caption, reply_markup=markup)


@app.on_callback_query(filters.regex(r"^(d )"))
async def d(_: Client, callback: CallbackQuery) -> None:
    user_id: int = callback.from_user.id
    markup: Keyboard = callback.message.reply_markup
    if int(markup.inline_keyboard[-1][0].callback_data.split()[1]) != user_id: return await callback.answer("- هذه الواجهه ليست لك.", show_alert=True)
    await callback.message.delete()

    
if __name__=="__main__": app.run()