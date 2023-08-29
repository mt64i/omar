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
    selections = [f"{message.from_user.mention} عمرها لأيما", 
f"{message.from_user.mention} يا قلب ايمت",
f"{message.from_user.mention} صرعت راسها لأيما",
f"{message.from_user.mention} لك نعم يا عيوني",
f"{message.from_user.mention} تؤبرني معك",
f"{message.from_user.mention} تفضل عم أسمع واللهي نصرعت",
f"{message.from_user.mention} أختصر ؟",]
    bar = random.choice(selections)
    await message.reply_text(bar)
    
@app.on_message(command("بحبك") & filters.group)
async def bottttt(client, message):
    selections = [f"{message.from_user.mention} يخليلي قلبك", 
f"{message.from_user.mention} بحبك أڪتࢪ ؏ فڪࢪة!",
f"{message.from_user.mention} بتنفسك",
f"{message.from_user.mention} ياعمري انااا تعا لقلببييي",
f"{message.from_user.mention} تفضل واطلب ايدي من @bbnnQ",
f"{message.from_user.mention} لا اله الا الله وانا بحبك",
f"{message.from_user.mention} خلص أستحي عيب",
f"{message.from_user.mention} خلاص يا مز خجلت",]
    bar = random.choice(selections)
    await message.reply_text(bar)

@app.on_message(command(["منرتبط","نرتبط"]) & filters.group)
async def bottttt(client, message):
    selections = [f"{message.from_user.mention} طبعا منرتبط 🤍", 
f"{message.from_user.mention} اي عمࢪي!",
f"{message.from_user.mention} يلا جيب الشيخ!",
f"{message.from_user.mention} لك بخجل بخجل",
f"{message.from_user.mention} هه فشࢪت 🙂",
f"{message.from_user.mention} تࢪا انا بوت!",
f"{message.from_user.mention} بخجل وربي 🥺",
f"{message.from_user.mention} اممممم بفڪࢪ 🥲",]
    bar = random.choice(selections)
    await message.reply_text(bar)
@app.on_message(command(["مرحبا","هلو"]) & filters.group)
async def bottttt(client, message):
    selections = [f"{message.from_user.mention} هلا بريحة هلي🤍", 
f"{message.from_user.mention} يهلا نوࢪت/ي!",
f"{message.from_user.mention} أهلين وسهلين بالحب 🙂",
f"{message.from_user.mention} 🔥🥀",
f"{message.from_user.mention} شࢪفوا على هل ضيف",
f"{message.from_user.mention} كل الهلا",
f"{message.from_user.mention} نوࢪ الڪࢪوب 🥀",
f"{message.from_user.mention} شعشعت يا قلب قلبي 🤍🧚🏼‍♂️",]
    bar = random.choice(selections)
    await message.reply_text(bar)
@app.on_message(command(["منتحاسب"]) & filters.group)
async def bottttt(client, message):
    selections = [f"{message.from_user.mention} خوفتني ترا 😔",
f"{message.from_user.mention} اي منتحاسب هه زلمة 😂",]
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
