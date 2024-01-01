import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from AlexaMusic import app
import re
import sys

GAME_MESSAGE = "🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱. 🔱\n\n🐉¦ مرحبا بك عزيزي:\n🐉¦في قسم العاب زد إي\n\n🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱. 🔱"
GAME_BUTTONS = [
    [ 
        InlineKeyboardButton ('العاب 3D', callback_data= 'GAME1'),
        InlineKeyboardButton ('مميزات', callback_data= 'GAME2'),
        ],[
        InlineKeyboardButton ('🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱', url =f"https://t.me/Source_Ze")              
                 ],[
                InlineKeyboardButton(
                        "𝗁᥆ꪔᥱ", callback_data="close"),
               ],
          ]
    

nmla = []

@app.on_message(command("رفع نمله"))
async def rf3nmla(client, message):
  if not message.reply_to_message.from_user.mention in nmla:
    nmla.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")


@app.on_message(command("تنزيل نمله"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in nmla:
    nmla.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")


@app.on_message(command("المرفوعين نمل"))
async def nml(client, message):
  nq = ""
  for n in nmla:
      nq += n + "\n"
  await message.reply_text(nq)





@app.on_message(command("رفع صرصر"))
async def rf3srsar(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n صرصر 😂♥️")


@app.on_message(command("تنزيل صرصر"))
async def tnzelsrar(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n صرصر 😂♥️")


@app.on_message(command("رفع رقاصه"))
async def yasooo(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n رقاصه واحد يذب فلوس عليها 😂💃")


@app.on_message(command("تنزيل رقاصه"))
async def yaso(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n رقاصه تابت😂😔")
  
  
@app.on_message(command("رفع منيوج"))
async def bjoiuyjk(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n منيوج واحد يركبه 😂♥️")


@app.on_message(command("تنزيل منيوج"))
async def kamal(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n منيوج كواد تاب 😂♥️")
  
  
@app.on_message(command("رفع وصخ"))
async def fdsa(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n وصخ بنجاح  😂♥️")


@app.on_message(command("تنزيل وصخ"))
async def kophvc(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n الوصخ استحمي 😂♥️")
  
  
@app.on_message(command("رفع عار"))
async def roky(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n عار عالمجتمع 😂♥️")


@app.on_message(command("تنزيل عار"))
async def zerso(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n عار خلاص 😂♥️")
  
  
@app.on_message(command("رفع بقره"))
async def vvvtyy(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n صار بقره واحد يحلبه 🐄🤭")


@app.on_message(command("تنزيل بقره"))
async def tttryuh(client, message):
  await message.reply_text(f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n ما ضل حليب  😂")
  
  
@app.on_message(command("رفع قرد"))
async def uiipppl(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n قرد واحد ينطي موزه 😂🐒")


@app.on_message(command("تنزيل قرد"))
async def bjhupq(client, message):
  await message.reply_text(f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n القرد صار بشر🙊🧍")
  
  
@app.on_message(command("رفع قلبي"))
async def pooiejh(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n خلاص صرت گلبه 😂♥️")


@app.on_message(command("تنزيل قلبي"))
async def ttrqew(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nما بقيت گلبهو 😭💔")
  
  
@app.on_message(command("رفع خدام"))
async def qyui(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خدام تع خدم بالكروب    😂🤓")


@app.on_message(command("تنزيل خدام"))
async def klhj(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n الخدام ترك الشغل  😢🚶")
  
  
@app.on_message(command("رفع كواد"))
async def wqew(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n كواد الكروب  😂🤓")


@app.on_message(command("تنزيل كواد"))
async def ohho(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n الكواد صار زلمه   😂🧔")
  
  
@app.on_message(command("رفع ارمله"))
async def drsss(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  صرتي ارمله وزوجك مات 🥹")


@app.on_message(command("تنزيل ارمله"))
async def gkvdr(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  خلاص لا تصيرين حزينه رجلج عايش هياته 😂🫶🏻")
  
  
@app.on_message(command("رفع صاكه"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n يصاكه خدي بالك من نفسك 🥹❤️")


@app.on_message(command("تنزيل صاكه"))
async def hhhhug(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n انتي صدكتي صاكه ولا شنو اني جنت اشاقه 😂😝")
  
  
@app.on_message(command("رفع ابني"))
async def cbky(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  صرت ابنه وكل حياتو🥹🖤")


@app.on_message(command("تنزيل ابني"))
async def ccgy(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حتى عائلتك ما يريدوك ذبوك  بالشارع ")
  
  
@app.on_message(command("رفع خاينه"))
async def mkloo(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n  ي خاينه ي حقيره ")


@app.on_message(command("تنزيل خاينه"))
async def fkijbh(client, message):
  await message.reply_text(f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n منو غبي للي جان مفكر الكمر هاذا يطلع خاين 🥹🥹💕")  
  
  
@app.on_message(command("رفع بنتي"))
async def yuhhss(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n صرتي بنتي وقطعه من گلبي 🥹❤️❤️❤️")


@app.on_message(command("تنزيل بنتي"))
async def hloih(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nكنت بهزر اني مخلفتش لسه🤡😂  ")  
  
  
@app.on_message(command("رفع خاين"))
async def kloss(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خنتها  جم مره كول لتخاف يخاين")


@app.on_message(command("تنزيل خاين"))
async def fiihug(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n شنو هاذا طلع سوء تفاهم انت اشرف من الشرف 😂❤️")
  
  
@app.on_message(command("رفع كواد"))
async def dadr(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n 😂 كواد طول عمرك مو اول مره")


@app.on_message(command("تنزيل كواد"))
async def hjj7gv(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  هاي نزلتك لتعصب 🙂💕")
  
  
@app.on_message(command("رفع مطي"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاص صار مطي رسمي 😹")


@app.on_message(command("تنزيل مطي"))
async def cxxv(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاص جنه نشاقه وياك لا تصير فد نوب 😂😝")
  
  



@app.on_message(command("رفع غبي"))
async def polkij(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n غبي وراح تضل غبي😹🤞")


@app.on_message(command("تنزيل غبي"))
async def nbvcc(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n غبي وصار يفتهم😹🫶")
  
  
@app.on_message(command("رفع مريتي"))
async def ttttuhyp(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n مريتك خذ  وجيبلنه بيبي😹😽")


@app.on_message(command("تنزيل مريتي"))
async def xxxxt(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طلقتها شوف غيرها 😂😝")  
  
  
@app.on_message(command("رفع زبال"))
async def oooph(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n زبال تع  نضف الكروب😹")


@app.on_message(command("تنزيل زبال"))
async def zzzas(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n زبال تعب و استقال 😂😝")  
  
  
@app.on_message(command("رفع خدامه"))
async def ggggop(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خدامه تع اغسلي رجلي 😹🤞")


@app.on_message(command("تنزيل خدامه"))
async def vvvuu(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nخدامه نزلت اجازه😹🫶")  
  
  
@app.on_message(command("رفع جلب"))
async def mmmuy(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n جلب خذ عضمه😹🤞")


@app.on_message(command("تنزيل جلب"))
async def dfrewq(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاص جلب صار الانسان😿😹")  
  
  
@app.on_message(command("رفع طيز"))
async def ssoss(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طيز و جبيره هماتين😹🤞")


@app.on_message(command("تنزيل طيز"))
async def nobo(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طيز لا تزعل نزلتك😹🫶")  
  
  
@app.on_message(command("رفع حرامي"))
async def llok(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حرامي راح ابلغ عنه😹🚓")


@app.on_message(command("تنزيل حرامي"))
async def kaompj(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حرامي ربنا تاب عليه😂😔")
  

@app.on_message(
    command(["الالعاب","العاب","الالعاب. 🔱"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c4f9c850312c8891385a9.jpg",
        caption= GAME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(GAME_BUTTONS)
    )  
@app.on_callback_query()
async def callback_query(client, CallbackQuery):
          if CallbackQuery.data == "GAME1":
            
             GAME1_MESSAGE = "🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱. 🔱\n\nمرحبا بك في قسم العاب 3D\n\n🐉"

             GAME1_BUTTONS = [
                 [
                    InlineKeyboardButton(
                        "°فلابي بيرد°", url=f"http://t.me/awesomebot?game=FlappyBird"), 
                    InlineKeyboardButton (
                        "°تبديل النجوم°", url=f"http://t.me/gamee?game=Switchy"),
                ],[
                    InlineKeyboardButton (
                        "°موتسيكلات°" , url=f"http://t.me/gamee?game=motofx"),
                    InlineKeyboardButton (
                        "°اطلاق النار°" , url=f"http://t.me/gamee?game=NeonBlaster"),
                ],[
                    InlineKeyboardButton (
                        "°كرة القدم°" , url=f"http://t.me/gamee?game=Footballstar"),
                    InlineKeyboardButton (
                        "°تجميع الالوان°" , url=f"http://t.me/awesomebot?game=Hextris"),
                ],[        
                    InlineKeyboardButton (
                        "°المجوهرات°" , url=f"http://t.me/gamee?game=DiamondRows"),
                    InlineKeyboardButton (
                        "°ركل الكرة°" , url=f"http://t.me/gamee?game=KeepitUP"),
                ],[        
                    InlineKeyboardButton (
                        "°بطولة السحق°" , url=f"http://t.me/gamee?game=SmashRoyale"),
                    InlineKeyboardButton (
                        "°2048°" , url=f"http://t.me/awesomebot?game=g2048"),
                ],[        
                    InlineKeyboardButton (
                        "°كرة السلة°" , url=f"http://t.me/gamee?game=BasketBoy"),
                    InlineKeyboardButton (
                        "°القط المجنون°" , url=f"http://t.me/gamee?game=CrazyCat"),
                ],[
                    InlineKeyboardButton (
                        "𝗁᥆ꪔᥱ" , callback_data= 'GAME')
                  ],
             ]
             await CallbackQuery.edit_message_text( 
                 GAME1_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME1_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱. 🔱\n\n🐉¦مرحبا بك في قسم العاب ze\n🐉¦اختار ما تشاء من الالعاب مسليه وستمتع بها\n\n🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱. 🔱" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('🕷¦العاب 3D', callback_data= 'GAME1'),
                      InlineKeyboardButton ('🔱¦العاب', callback_data= 'GAME2')
                      ],[
        InlineKeyboardButton ('🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱', url =f"https://t.me/Source_Ze")              
                 ],[
                InlineKeyboardButton(
                        "𝗁᥆ꪔᥱ", callback_data="close"),
               ],
          ]
     
               await CallbackQuery.edit_message_text( 
                 RETURN_GAME ,
                 reply_markup = InlineKeyboardMarkup(RETURN_BUTTON) 
                    )
          elif CallbackQuery.data == "GAME2":
               
               SOURCE_GAME = "🔱\n\n العاب زد إي nكت\nتويت\nاسال\nصراحه\nاني منو\nبايو\nمنو في الكول\nسورس\nزخرفه\nاذكار\nانصحني\nكتبات\nافلام\nغنيلي\nرفع\nذكاء\nنكته\nكشف\nايدي\nميديا\nتحويل ملصق\n🔱." 

               SORGAM_BUTTON = [
                    [ 
                      InlineKeyboardButton ('🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱', url =f"https://t.me/Source_Ze")
                      ],[
                         InlineKeyboardButton ('𝗁᥆ꪔᥱ', callback_data= 'GAME')
                    ]
               ]    
               await CallbackQuery.edit_message_text( 
                 SOURCE_GAME ,
                 reply_markup = InlineKeyboardMarkup(SORGAM_BUTTON) 
                    )
    
