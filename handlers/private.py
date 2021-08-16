from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

Puedo reproducir m��sica en la llamada de voz de su grupo. Desarrollado por [�9�5Fastmore Crak](https://t.me/fastmorecrak).

Agr��game a tu grupo y toca m��sica libremente !**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://fastmorecrak.github.io/Home/index.html")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Supportfasting"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/FastmoreCrakyt"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "�0�6Cloner Bot", url="https://t.me/supporUnix/3"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➄1�7 Add To Your Group ➄1�7", url="https://t.me/animelife_HD?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Agregue Su Musica ✄1�7**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/FastmoreCrakyt")
                ]
            ]
        )
   )


