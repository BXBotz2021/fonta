import os
from pyrogram import Client, filters, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config

# Temporary dictionary to store requesters
temp = {"REQUESTERS": {}}

# Channel configuration
AUTH_CHANNEL = "-1002693207322"  # Use numeric channel ID
AUTH_CHANNEL_USERNAME = "Bot_Resurge"  # Channel username

async def is_subscribed(bot, user_id):
    try:
        member = await bot.get_chat_member(AUTH_CHANNEL, user_id)
        return member.status in [enums.ChatMemberStatus.MEMBER, enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]
    except UserNotParticipant:
        return False
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@Client.on_message(filters.command('start'))
async def start(c, m):
    owner_id = int(Config.OWNER_ID)
    if m.from_user.id != owner_id and not await is_subscribed(c, m.from_user.id):
        buttons = [
            [InlineKeyboardButton("Join Channel", url=f"https://t.me/{AUTH_CHANNEL_USERNAME}")],
            [InlineKeyboardButton("Try Again", callback_data="try_again")]
        ]
        await m.reply_text(
            text=f"❌ You must join our channel to use this bot:\n\n👉 [Join Channel](https://t.me/{AUTH_CHANNEL_USERNAME})",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True
        )
        return
    
    owner = await c.get_users(owner_id)
    owner_username = owner.username if owner.username else 'Movies_Botz'
    text = f"""**👋 Hello! {m.from_user.mention(style='md')},**\n\n💡 I am a Stylish Font Bot.\n\n__Send me text and see the magic ✨🪄__\n\n**Made with ❤️‍🔥 by @{owner_username}**"""
    
    buttons = [[
        InlineKeyboardButton('🔰 Channel', url=f"https://t.me/{AUTH_CHANNEL_USERNAME}"),
        InlineKeyboardButton('🎛️ Creator', url=f"https://t.me/{owner_username}")
    ]]
    await m.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex('^try_again'))
async def try_again(c, m):
    if not await is_subscribed(c, m.from_user.id):
        await m.answer("❌ You must join the channel first to continue!")
        return
    await m.message.edit("✅ You're now subscribed! Feel free to continue using the bot.")
