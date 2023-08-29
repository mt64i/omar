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
    selections = [f"عمرها لأيما 🤍🧚🏼‍♂️ {message.from_user.mention}", 
f"يا قلب ايما ♥ {message.from_user.mention}",
f"صرعت راسها لأيما 🙈 {message.from_user.mention}",
f"لك نعم يا عيوني {message.from_user.mention}",
f"تؤبرني معك {message.from_user.mention}",
f"تفضل عم أسمع واللهي نصرعت 🙂 {message.from_user.mention}",
f" أختصر ؟ 💕 {message.from_user.mention}",]
    bar = random.choice(selections)
    await message.reply_text(bar)
    
@app.on_message(command("بحبك") & filters.group)
async def bottttt(client, message):
    selections = [f"يخليلي قلبك 🤍 {message.from_user.mention}", 
f"بحبك أڪتࢪ ؏ فڪࢪة ♥! {message.from_user.mention}",
f"بتنفسك ♥ {message.from_user.mention}",
f"ياعمري انااا تعا لقلببييي {message.from_user.mention}",
f"تفضل واطلب ايدي من @bbnnQ 🧚🏼‍♂️ {message.from_user.mention}",
f"لا اله الا الله وانا بحبك 🥺 {message.from_user.mention}",
f"خلص أستحي عيب 😒 {message.from_user.mention}",
f"خلاص يا مز خجلت 🙂 {message.from_user.mention}",]
    bar = random.choice(selections)
    await message.reply_text(bar)

@app.on_message(command(["منرتبط","نرتبط"]) & filters.group)
async def bottttt(client, message):
    selections = [f"طبعا منرتبط 🤍 {message.from_user.mention}", 
f"اي عمࢪي 🤍{message.from_user.mention}",
f"يلا جيب الشيخ 🔥! {message.from_user.mention}",
f"لك بخجل بخجل 🙂 {message.from_user.mention}",
f"هه فشࢪت 🙂 {message.from_user.mention}",
f"تࢪا انا بوت ♥! {message.from_user.mention}",
f"بخجل وربي 🥺 {message.from_user.mention}",
f"اممممم بفڪࢪ 🥲 {message.from_user.mention}",]
    bar = random.choice(selections)
    await message.reply_text(bar)
@app.on_message(command(["مرحبا","هلو"]) & filters.group)
async def bottttt(client, message):
    selections = [f"هلا بريحة هلي 🤍 {message.from_user.mention}", 
f"يهلا نوࢪت/ي 🧚🏼‍♂️🤍 {message.from_user.mention}",
f"أهلين وسهلين بالحب 🙂 {message.from_user.mention}",
f"🔥🥀 {message.from_user.mention}",
f"شࢪفوا على هل ضيف 😹💔 {message.from_user.mention}",
f"كل الهلا {message.from_user.mention}",
f"نوࢪ الڪࢪوب 🥀 {message.from_user.mention}",
f"شعشعت يا قلب قلبي 🤍🧚🏼‍♂️ {message.from_user.mention}",]
    bar = random.choice(selections)
    await message.reply_text(bar)
@app.on_message(command(["منتحاسب"]) & filters.group)
async def bottttt(client, message):
    selections = [f"خفت تࢪا 😹💔 {message.from_user.mention}",
f"يعني هلأ أبڪي؟ {message.from_user.mention}",]
    bar = random.choice(selections)
    await message.reply_text(bar)

@app.on_message(command(["غنيلي"]) & filters.group)
async def bottttt(client: Client, message: Message):
    selections = [f"https://t.me/c/1892532627/3 {message.from_user.mention}", 
f"https://t.me/c/1892532627/4 {message.from_user.mention}",
f"https://t.me/c/1892532627/5 {message.from_user.mention}",
f"https://t.me/c/1892532627/6 {message.from_user.mention}",
f"https://t.me/c/1892532627/7 {message.from_user.mention}",
f"https://t.me/c/1892532627/9 {message.from_user.mention}",
f"https://t.me/c/1892532627/10 {message.from_user.mention}",
f"https://t.me/c/1892532627/11 {message.from_user.mention}",
f"https://t.me/c/1892532627/12 {message.from_user.mention}",
f"https://t.me/c/1892532627/13 {message.from_user.mention}",
f"https://t.me/c/1892532627/14 {message.from_user.mention}",
f"https://t.me/c/1892532627/15 {message.from_user.mention}",
f"https://t.me/c/1892532627/16 {message.from_user.mention}",
f"https://t.me/c/1892532627/17 {message.from_user.mention}",
f"https://t.me/c/1892532627/18 {message.from_user.mention}",
f"https://t.me/c/1892532627/19 {message.from_user.mention}",
f"https://t.me/c/1892532627/20 {message.from_user.mention}",
f"https://t.me/c/1892532627/21 {message.from_user.mention}",
f"https://t.me/c/1892532627/22 {message.from_user.mention}",
f"https://t.me/c/1892532627/23 {message.from_user.mention}",
f"https://t.me/c/1892532627/24 {message.from_user.mention}",
f"https://t.me/c/1892532627/25 {message.from_user.mention}",
f"https://t.me/c/1892532627/26 {message.from_user.mention}",
f"https://t.me/c/1892532627/27 {message.from_user.mention}",
f"https://t.me/c/1892532627/28 {message.from_user.mention}",
f"https://t.me/c/1892532627/29 {message.from_user.mention}",
f"https://t.me/c/1892532627/30 {message.from_user.mention}",
f"https://t.me/c/1892532627/31 {message.from_user.mention}",
f"https://t.me/c/1892532627/32 {message.from_user.mention}",
f"https://t.me/c/1892532627/33 {message.from_user.mention}",
f"https://t.me/c/1892532627/34 {message.from_user.mention}",
f"https://t.me/c/1892532627/35 {message.from_user.mention}",
f"https://t.me/c/1892532627/36 {message.from_user.mention}",
f"https://t.me/c/1892532627/37 {message.from_user.mention}",
f"https://t.me/c/1892532627/38 {message.from_user.mention}",
f"https://t.me/c/1892532627/39 {message.from_user.mention}",
f"https://t.me/c/1892532627/40 {message.from_user.mention}",]
    bar = random.choice(selections)
    client.send_voice(bar)

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
