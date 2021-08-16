from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 馃幍

Puedo reproducir música en la llamada de voz de su grupo. Desarrollado por [👑Fastmore Crak](https://t.me/fastmorecrak).

Agrégame a tu grupo y toca música libremente !**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "馃洜 Source Code 馃洜", url="https://fastmorecrak.github.io/Home/index.html")
                  ],[
                    InlineKeyboardButton(
                        "馃挰 Group", url="https://t.me/Supportfasting"
                    ),
                    InlineKeyboardButton(
                        "馃攰 Channel", url="https://t.me/FastmoreCrakyt"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🧲Cloner Bot", url="https://t.me/supporUnix/3"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "鉃� Add To Your Group 鉃�", url="https://t.me/animelife_HD?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Agregue Su Musica 鉁�**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "馃攰 Channel", url="https://t.me/FastmoreCrakyt")
                ]
            ]
        )
   )


