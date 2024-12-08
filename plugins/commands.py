import os
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config
from .fonts import Fonts

# Replace 'CHANNEL_USERNAME' with your channel's username (without '@')
CHANNEL_USERNAME = "YourChannelUsername"

async def check_force_subscription(client, user_id):
    """
    Function to check if a user has joined the required channel.
    Returns True if the user is a member or owner, otherwise False.
    """
    try:
        user = await client.get_chat_member(CHANNEL_USERNAME, user_id)
        if user.status in ["member", "administrator", "creator"]:
            return True
    except UserNotParticipant:
        return False
    except Exception:
        return False
    return False

@Client.on_message(filters.command('start'))
async def start(c, m):
    owner_id = int(Config.OWNER_ID)

    # If the user is not the bot owner, check if they have joined the channel
    if m.from_user.id != owner_id:
        if not await check_force_subscription(c, m.from_user.id):
            # If the user is not a member, send a message with a "Try Again" button
            buttons = [
                [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
                [InlineKeyboardButton("Try Again", callback_data="try_again")]
            ]
            await m.reply_text(
                text=f"❌ You must join our channel to use this bot:\n\n👉 [Join Channel](https://t.me/{CHANNEL_USERNAME})",
                reply_markup=InlineKeyboardMarkup(buttons),
                disable_web_page_preview=True
            )
            return

    # If user is the owner or has joined, send the regular start message
    owner = await c.get_users(owner_id)
    owner_username = owner.username if owner.username else 'Movies_Botz'

    text = f"""**👋 Hello! {m.from_user.mention(style='md')},**

💡 I ᴀᴍ Sᴛʏʟɪsʜ Fᴏɴᴛ Bᴏᴛ

__I Can Help You To Get Stylish Fonts. Just Send Me Some Text And See The Magic✨🪄__

**Mα∂є Wιтһ ❤️‍🔥 ву @{owner_username}**
"""

    buttons = [
        [
            InlineKeyboardButton('🔰 Cʜᴀɴɴᴇʟ', url=f"https://t.me/{CHANNEL_USERNAME}"),
            InlineKeyboardButton('🎛️ Cʀᴇᴀᴛᴏʀ', url=f"https://t.me/{owner_username}")
        ]
    ]
    await m.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.private & filters.incoming & ~filters.command('start'))
async def handle_other_messages(c, m):
    owner_id = int(Config.OWNER_ID)

    if m.from_user.id != owner_id:
        if not await check_force_subscription(c, m.from_user.id):
            await m.reply_text(
                text=f"❌ You must join our channel to use this bot:\n\n👉 [Join Channel](https://t.me/{CHANNEL_USERNAME})",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")]]
                ),
                disable_web_page_preview=True
            )
            return

    await style_buttons(c, m)

@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛', callback_data='style+typewriter'),
        InlineKeyboardButton('𝕆𝕦𝕥𝕝𝕚𝕟𝕖', callback_data='style+outline'),
        InlineKeyboardButton('𝐒𝐞𝐫𝐢𝐟', callback_data='style+serif'),
        ],[ 
        InlineKeyboardButton('𝑺𝒆𝒓𝒊𝒇', callback_data='style+bold_cool'),
        InlineKeyboardButton('𝑆𝑒𝑟𝑖𝑓', callback_data='style+cool'),
        InlineKeyboardButton('Sᴍᴀʟʟ Cᴀᴘs', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('𝓈𝒸𝓇𝒾𝓅𝓉', callback_data='style+script'),
        InlineKeyboardButton('𝓼𝓬𝓻𝓲𝓹𝓽', callback_data='style+script_bolt'),
        InlineKeyboardButton('ᵗⁱⁿʸ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('ᑕOᗰIᑕ', callback_data='style+comic'),
        InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
        InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
        InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
        InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎ⓔ︎Ⓢ︎', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅨︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖤𝖳𝖧𝖨𝖢', callback_data='style+gothic_bolt'),
        ]
    ]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))

# Handle the "Try Again" button
@Client.on_callback_query(filters.regex('^try_again'))
async def try_again(c, m):
    if not await check_force_subscription(c, m.from_user.id):
        # If user is still not subscribed, resend the message with the "Try Again" button
        buttons = [
            [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
            [InlineKeyboardButton("Try Again", callback_data="try_again")]
        ]
        await m.answer("❌ You need to join our channel to use the bot.", show_alert=True)
        await m.message.edit_text(
            text=f"❌ You must join our channel to use this bot:\n\n👉 [Join Channel](https://t.me/{CHANNEL_USERNAME})",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True
        )
    else:
        # If the user has joined, send a success message
        await m.answer("✅ You're successfully subscribed! Now you can use the bot.")
        await m.message.edit_text(
            text=f"**Welcome!** {m.from_user.mention(style='md')}, You can now start using the bot!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('Start Using', callback_data='start_using')]]
            )
        )

@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    _, style = m.data.split('+')
    cls = getattr(Fonts, style, None)
    if cls:
        new_text = cls(m.message.reply_to_message.text)
        await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)

