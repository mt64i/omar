import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from AnonXMusic import app

spam_chats = []


@app.on_message(command(["@all","تاغ للكل"])) 
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "يمڪنك أستخدام هذل الأمر في الڪروبات والقنوات فقط!!"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("فقط المشࢪفين يمڪنهم عمل التاغ!!")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("أعطني ڪلمة للتاغ!!")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "لا أستطيع ذكر الأعضاء للرسائل القديمة! (الرسائل التي يتم إرسالها قبل إضافتي إلى المجموعة)"
            )
    else:
        return await event.respond(
            "قم بالرد على رسالة أو أعطني بعض الرسائل النصية لأذكر الآخرين!"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(command(["الغاء التاغ","ايقاف"]))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("لا توجد عملية للتاغ؟")
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("فقط المشࢪف يمڪنه ايقاف التاغ")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("تم ايقاف التاغ بنجاح 🥀")


__mod_name__ = "Tᴀɢ Aʟʟ"
__help__ = """
*Only for admins*

❍ /tagall or @all '(reply to message or add another message) To mention all members in your group, without exception.'
"""
