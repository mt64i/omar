# telegram: @bbnnQ ~ My channel: @ccooR حقوق.
import os
import random
import asyncio,time
from datetime import datetime
from pyrogram import Client, filters, enums
from pyrogram.enums import ChatAction, ParseMode
from strings.filters import command
from pyrogram.types import (Message,
InlineKeyboardMarkup,InlineKeyboardButton)
from typing import Union
from AnonXMusic import app

X = [
    [
        InlineKeyboardButton(text="شڪࢪ لـ", url=f"https://t.me/bbnnq"),
        
        InlineKeyboardButton(text=" التحديثات ", url=f"https://t.me/cczza"),
    ]
    ]

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
openai.api_key = "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" 
@app.on_message(command(["chatgpt","ai","سؤال"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "مثال:**\n\n`كم عدد سكان سوريا؟ `")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n Emma Call ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨وقت العمل {telegram_ping} \n\n🎉تم لواسطة @EmCaMusicBot", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**خطأ: {e} ")
