from telethon import Button

from Himawari import telethn
from Himawari.events import register

PHOTO = "https://graph.org/file/49ccd6c3fd1ab3a8d2701.mp4"


@register(pattern=("Good morning"))
async def awake(event):
    MEOW = f"Wᴇʟᴄᴏᴍᴇ 🥀  ᴛʜɪꜱ ʙᴇᴀᴜᴛɪꜰᴜʟ ᴍᴏʀɴɪɴɢ ᴡɪᴛʜ ᴀ ꜱᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ꜰᴀᴄᴇ. ɪ ʜᴏᴘᴇ ʏᴏᴜ'ʟʟ ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴅᴀʏ ᴛᴏᴅᴀʏ. ᴡɪꜱʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ! {event.sender.first_name}"
    BUTTON = [
        [
            Button.url("Mᴇᴇᴛ ᴍᴇ Hᴇʀᴇ ✨", "https://telegram.dog/Mega_Bots_Support"),
        ]
    ]
    await telethn.send_file(event.chat_id, PHOTO, caption=MEOW, buttons=BUTTON)
