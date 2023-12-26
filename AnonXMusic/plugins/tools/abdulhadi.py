import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
import re
import sys
from pyrogram import filters
import config
from AnonXMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)

@app.on_message(
    command(["المطور","مطور السورس","مطور"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5338950085)
    name = usr.first_name
    user = await client.get_chat(5338950085)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5338950085, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""𝙉𝙖𝙢𝙚 | - [{usr.first_name}](https://t.me/aaaqqq) 🕷
                        
𝙐𝙨𝙚𝙧 | - @AAAQQQ 🕷
                           
𝘽𝙞𝙤 | - {Bio} 🕷 """,                                    

reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/AAAQQQ"),
          ],[
              InlineKeyboardButton("‹ برود ›", url=f"https://t.me/zzSvv"),
            ],               
          ]              
       )              
    )                     
                    
