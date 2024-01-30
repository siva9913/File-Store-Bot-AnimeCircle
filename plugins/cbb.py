#(©)Codexbotz

from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
                        text = f"<b>About this Bot:\n\n  A Telegram Bot for storing posts or files that can be accessed via a Special Link.\n\n👨‍💻 Modified by @Shidoteshika1</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("○ My Owner ○", url = "https://t.me/Shidoteshika1")
                    ],[
                        InlineKeyboardButton('Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ', url = 'https://t.me/Animemoviesr'),
InlineKeyboardButton('Aɴɪᴍᴇ Gʀᴏᴜᴘ', url = 'https://t.me/ChatBox480')
                    ],[
                        InlineKeyboardButton("🔒 Close 🔒", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

 
