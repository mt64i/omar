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

@app.on_message(command([f"غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,122)
    url = f"https://t.me/EmmaBotVoice/{rl}"
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
‹: غنيلي - سترسل لك اغنية عشوائية 🥀
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
