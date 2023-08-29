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

@app.on_message(command("ايما") & filters.group)
async def bottttt(client, message):
    selections = [f"{message.from_user.mention}\nعمرها لأيما", 
f"{message.from_user.mention}\nيا قلب ايمت",
f"{message.from_user.mention}\nصرعت راسها لأيما",
f"{message.from_user.mention}\nلك نعم يا عيوني",
f"{message.from_user.mention}\nتؤبرني معك",
f"{message.from_user.mention}\nتفضل عم أسمع واللهي نصرعت",
f"{message.from_user.mention}\nأختصر ؟",]
    bar = random.choice(selections)
    await message.reply_text(bar)
    
@app.on_message(command("بحبك") & filters.group)
async def bottttt(client, message):
    selections = [f"{message.from_user.mention}\nيخليلي قلبك", 
f"{message.from_user.mention}\nبحبك اكتر على فكرة!",
f"{message.from_user.mention}\nبتنفسك",
f"{message.from_user.mention}\nياعمري انااااا",
f"{message.from_user.mention}\nتفضل واطلب ايدي من @bbnnQ",
f"{message.from_user.mention}\nلا اله الا الله وانا بحبك",
f"{message.from_user.mention}\nخلص أستحي عيب",
f"{message.from_user.mention}\nخلاص يا مز خجلت",]
    bar = random.choice(selections)
    await message.reply_text(bar)

@app.on_message(command(["منرتبط","نرتبط"]) & filters.group)
async def bottttt(client, message):
    selections = ["طبعا منرتبط 🤍", 
f"{message.from_user.mention}\n اي عمࢪي!",
f"{message.from_user.mention}\nيلا جيب الشيخ!",
f"{message.from_user.mention}\nلك بخجل بخجل",
f"{message.from_user.mention}\nهه فشࢪت 🙂",
f"{message.from_user.mention}\nتࢪا انا بوت!",
f"{message.from_user.mention}\nبخجل وربي 🥺",
f"{message.from_user.mention}\nاممممم بفڪࢪ 🥲",]
    bar = random.choice(selections)
    await message.reply_text(bar)
@app.on_message(command(["مرحبا","هلو"]) & filters.group)
async def bottttt(client, message):
    selections = ["هلا بريحة هلي🤍", 
f"{message.from_user.mention}\n يهلا نوࢪت/ي!",
f"{message.from_user.mention}\nأهلين وسهلين بالحب 🙂",
f"{message.from_user.mention}\n🔥🥀",
f"{message.from_user.mention}\nشࢪفوا على هل ضيف",
f"{message.from_user.mention}\nكل الهلا",
f"{message.from_user.mention}\nنوࢪ الڪࢪوب 🥀",
f"{message.from_user.mention}\nشعشعت يا قلب قلبي 🤍🧚🏼‍♂️",]
    bar = random.choice(selections)
    await message.reply_text(bar)
@app.on_message(command("الاوامر"))
async def ahmad(client: Client, message: Message):
    await message.reply_text(f"""🧚🏼‍♂️🔥 أوامࢪ بوت إيما 🧚🏼‍♂️🔥:

‹: تشغيل - لتشغيل أغنية 🥀
‹: تخطي - لتخطي الأغنية 🥀
‹: انهاء - لانهاء تشغيل الاغنية 🥀
‹: تحميل - مع أسم الأغنية او الفيديو 🥀
‹: توقف - لايقاف التشغيل مؤقتاً 🥀
‹: تكميل - لتكميل الاغنية المتوقفة 🥀
‹: اللغه - لتغير لغة البوت 🥀
‹: تسريع - لتغيير سرعة الصوت 🥀
‹: ايما + السؤال (فقط في الخاص) 🥀
""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ اضافة الى مجموعة ›", url=f"https://t.me/EmCaMusicBot?startgroup=true"),
            ],
            ]
        ),
    )
@app.on_message(command(["المطور","المبرمج","السورس"]))
async def ahmad(client: Client, message: Message):
    await message.reply_text(f"- 𝐖ᴇʟᴄᴏᴍᴇ 𝐓ᴏ 𝐒ᴏụʀᴄᴇ 𝐄ᴍᴍᴀ 🥀\n- 𝐒ᴏụʀᴄᴇ 𝐃ᴇᴠᴇʟᴏᴘᴇʀ: @bbnnQ 🧑‍💻",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝐃ᴇᴠᴇʟᴏᴘᴇʀ", user_id=5866649827),
                InlineKeyboardButton("𝐒ᴏụʀᴄᴇ", url="t.me/cczza"),
            ],
            ]
        ),
    )
