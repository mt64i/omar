# telegram: @bbnnQ ~ My channel: @ccooR حقوق.
import os
import random
import asyncio
from pyrogram import Client,filters
from strings.filters import command
from pyrogram.types import (Message,
InlineKeyboardMarkup,InlineKeyboardButton)
from typing import Union
from AnonXMusic import app

@app.on_message(command([f"غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,258)
    url = f"https://t.me/zzzssvv/{rl}"
    await client.send_voice(message.chat.id,url,caption=f"🧚🏼‍♂️ ¦ تم أختياࢪ أغنية لك {message.from_user.mention}",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(command("الاوامر"))
async def ahmad(client: Client, message: Message):
    await message.reply_text(f"""🧚🏼‍♂️🔥 أوامࢪ بوت ميوزك 🧚🏼‍♂️🔥:

‹: تشغيل - لتشغيل أغنية 🥀
‹: تخطي - لتخطي الأغنية 🥀
‹: انهاء - لانهاء تشغيل الاغنية 🥀
‹: تحميل - مع أسم الأغنية او الفيديو 🥀
‹: توقف - لايقاف التشغيل مؤقتاً 🥀
‹: تكميل - لتكميل الاغنية المتوقفة 🥀
‹: اللغه - لتغير لغة البوت 🥀
‹: تسريع - لتغيير سرعة الصوت 🥀
‹: غنيلي - سترسل لك اغنية عشوائية 🥀
""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ اضفني الى مجموعتك ›", url=f"https://t.me/Xurtbot?startgroup&admin=post_messages+edit_messages+delete_messages+invite_users"),
            ],
            ]
        ),
    )
@app.on_message(command(["مطور","السورس","سورس","المطور","تيم"]))
async def ahmad(client: Client, message: Message):
    await message.reply_text(f"- تفضل حبيبي كول. @mt64i 🧑‍💻",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("المطور🤖", user_id=7101424391),
        
                InlineKeyboardButton("سورس 𝐦𝐭𝐚𝐞𝐦 ↑", url="https://t.me/E_A_1L"),
            ],
            ]
        ),
    )
