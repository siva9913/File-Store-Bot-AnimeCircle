#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╭━━━━━━━━━━━━━━━━━\n○ Creator : <a href='https://t.me/shidoteshika1'>The King 🜲</a>\n➖➖➖➖➖➖➖➖➖➖\n○ Language : <code>Python3</code>\n○ Library : Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://t.me/shidoteshika1'>Ask my Owner</a>\n➖➖➖➖➖➖➖➖➖➖\n○ Channel : <a href='https://t.me/animemoviesr'>infinity void ∞</a>\n○ Support Group : <a href='https://t.me/chatbox480'>Aɴɪᴍᴇ Cɪʀᴄʟᴇ 🜲</a>\n╰━━━━━━━━━━━━━━━━━</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

 
