import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b5e55f4cd31bd1da2abd3.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
BOT FAST LIKE FAST AS FUCK](@TEAM_VAMPIRES)
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : [𝗡𝗔𝗡𝗗𝗔𝗡 𝗩𝗔𝗠𝗣𝗜𝗥𝗘](https://t.me/NANDAN_VAMPIRE)
┣★ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 : [�𝗕𝗔𝗖𝗞𝗖𝗛𝗢𝗗𝗜 𝗣𝗢𝗜𝗡�𝗧 ](https://t.me/VAMPIRES_OFFICIAL)
┗━━━━━━━━━━━━━━━━━┛

━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       " ❰ 𝘼𝙙𝙙 𝙈𝙚 𝙄𝙣 𝙂𝙧𝙤𝙪𝙥 ❱", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "legend"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b5e55f4cd31bd1da2abd3.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "JOIN FOR BAKCHODI", url=f"https://t.me/TEAM_VAMPIRES")
                ]
            ]
        ),
    )
