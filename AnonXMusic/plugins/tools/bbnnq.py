# telegram: @bbnnQ ~ My channel: @ccooR حقوق.
import os
import random
import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import (Message,
InlineKeyboardMarkup,InlineKeyboardButton)
from typing import Union
from AnonXMusic import app


@app.on_message(command("ايما"))
async def bottttt(client, message):
    selections = ["عمرها لأيما", 
"يا قلب ايما",
"صرعت راسها لأيما",
"لك نعم يا عيوني",
"تؤبرني معك",
"تفضل عم أسمع واللهي نصرعت",
"أختصر ؟",]
    bar = random.choice(selections)
    await message.reply_text(bar)
    
@app.on_message(command("بحبك"))
async def bottttt(client, message):
    selections = ["يخليلي قلبك", 
"بحبك اكتر على فكرة!",
"بتنفسك",
"ياعمري انااااا",
"تفضل واطلب ايدي من @bbnnQ",
"لا اله الا الله وانا بحبك",
"خلص أستحي عيب",
"خلاص يا مز خجلت",]
    bar = random.choice(selections)
    await message.reply_text(bar)

@app.on_message(command("الاوامر"))
async def ahmad(client: Client, message: Message):
    await message.reply_text(f"""**اليك أوامر بوت ايما**:

‹: تشغيل - لتشغيل أغنية 🎵
‹: تخطي - لتخطي الأغنية 🎵
‹: انهاء - لانهاء تشغيل الاغنية 🎵
‹: تحميل - مع أسم الأغنية او الفيديو 🎬
‹: توقف - لايقاف التشغيل مؤقتاً 🔇
‹: تكميل - لتكميل الاغنية المتوقفة 🔊
‹: اللغه - لتغير لغة البوت 🇦🇪
‹: تسريع - لتغيير سرعة الصوت 🎚
""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ اضافة الى مجموعة ›", url=f"https://t.me/EmCaMusicBot?startgroup=true"),
            ],
            ]
        ),
    )
