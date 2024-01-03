from AlexaMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message
import requests


@app.on_message(filters.regex(r"^(طقس)"))
async def __(_: Client, message: Message):
    data = message.text.split(maxsplit=1)
    if len(data) < 2: return await message.reply("- خطأ في البيانات.\n- طقس + المدينه", reply_to_message_id=message.id)
    try: return await message.reply(_weather(data[1]), reply_to_message_id=message.id)
    except KeyError: await message.reply("- City Not Found.", reply_to_message_id=message.id)

def _weather(query):
    params = {
        "q": query,
        "APPID": "eedbc05ba060c787ab0614cad1f2e12b",
        "units": "metric"
    }
    response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params).json()
    name = f"- Name: {response['name']}\n╰───○ ● Country: {response['sys']['country']}\n\n"
    weather = f"- Weather: {response['weather'][0]['main']}\n╰───○ ● Description: {response['weather'][0]['description']}\n\n"
    temp = f"- Temperature: {response['main']['temp']}\n╰───○ ● Human feels: {response['main']['feels_like']}\n\n"
    wind = f"- Wind speed: {response['wind']['speed']}\n╰───○ ● Degree: {response['wind']['deg']}\n\n"
    humidity = f"- humidity: {response['main']['humidity']}"
    caption = f"{name}{weather}{temp}{wind}{humidity}"
    return caption
