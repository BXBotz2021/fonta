import os
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .fonts import Fonts
from config import Config

# Set your channel ID here (use the numeric ID)
AUTH_CHANNEL_ID = -1002437864651  # Channel ID (use the full numeric ID, not the username)
AUTH_CHANNEL_USERNAME = "moviez_botz"  # Channel username for the button

async def check_force_subscription(client, user_id):
    """
    Function to check if a user has joined the required channel by ID.
    Returns True if the user is a member or owner, otherwise False.
    """
    try:
        user = await client.get_chat_member(AUTH_CHANNEL_ID, user_id)
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
                [InlineKeyboardButton("Join Channel", url=f"https://t.me/{AUTH_CHANNEL_USERNAME}")],
                [InlineKeyboardButton("Try Again", callback_data="try_again")]
            ]
            await m.reply_text(
                text=f"❌ You must join our channel to use this bot:\n\n👉 [Join Channel](https://t.me/{AUTH_CHANNEL_USERNAME})",
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

**Mα∂є Wιтʜ ❤️‍🔥 ву @{owner_username}**
"""

    buttons = [
        [
            InlineKeyboardButton('🔰 Cʜᴀɴɴᴇʟ', url=f"https://t.me/{AUTH_CHANNEL_USERNAME}"),
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
                text=f"❌ You must join our channel to use this bot:\n\n👉 [Join Channel](https://t.me/{AUTH_CHANNEL_USERNAME})",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{AUTH_CHANNEL_USERNAME}")]]
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
        InlineKeyboardButton('𝑪𝑶𝑴𝑰𝑪', callback_data='style+comic'),
        InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
        InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),
        ],[ 
        InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
        InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
        InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎ⓔ︎Ⓢ︎', callback_data='style+circles'),
        ],[ 
        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅨︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),
        ],[ 
        InlineKeyboardButton('C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡', callback_data='style+cloud'),
        InlineKeyboardButton('H̆̈ă̈p̆̈p̆̈y̆̈', callback_data='style+happy'),
        InlineKeyboardButton('S̑̈ȃ̈d̑̈', callback_data='style+sad'),
        ],[ 
        InlineKeyboardButton('Next ➡️', callback_data="nxt")
    ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex('^try_again'))
async def try_again(c, m):
    # When the user clicks "Try Again," check if they joined the channel again
    if not await check_force_subscription(c, m.from_user.id):
        await m.answer("❌ You must join the channel first to continue!")
        return

    # If they are subscribed, proceed with regular interaction
    await m.message.edit("✅ You're now subscribed! Feel free to continue using the bot.")

@Client.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    buttons = [[
        InlineKeyboardButton('🇸 🇵 🇪 🇨 🇮 🇦 🇱 ', callback_data='style+special'),
        InlineKeyboardButton('🅂🅀🅄🄰🅴🅂', callback_data='style+squares'),
        InlineKeyboardButton('🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎', callback_data='style+squares_bold'),
        ],[ 
        InlineKeyboardButton('ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ', callback_data='style+andalucia'),
        InlineKeyboardButton('爪卂几ᘜ卂', callback_data='style+manga'),
        InlineKeyboardButton('S̾t̾i̾n̾k̾y̾', callback_data='style+stinky'),
        ],[ 
        InlineKeyboardButton('B̥ͦu̥ͦb̥ͦb̥ͦl̥ͦe̥ͦs̥ͦ', callback_data='style+bubbles'),
        InlineKeyboardButton('U͟n͟d͟e͟r͟l͟i͟n͟e͟', callback_data='style+underline'),
        InlineKeyboardButton('꒒ꍏꀷꌩꌃꀎꁅ', callback_data='style+ladybug'),
        ],[ 
        InlineKeyboardButton('⬅️ Back', callback_data='style+back')
    ]]
    await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
