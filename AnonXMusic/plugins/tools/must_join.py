from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AnonXMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/A1DIIU":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("A1DIIU", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/A1DIIU".isalpha():
                link = "https://t.me/A1DIIU"
            else:
                chat_info = await bot.get_chat("A1DIIU")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\n⌯︙قناة البوت: @A1DIIU .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("اضغط للأشتراك .", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat @A1DIIU !")
