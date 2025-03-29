import os
from pyrogram import Client, filters, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config
from .fonts import Fonts
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
    owner_username = owner.username if owner.username else 'MUFAZTG_NEW'
    text = f"""👋 <b>Hey there, {m.from_user.mention(style='html')}!</b>\n\n✨ Welcome to <b>Stylish Font Bot</b> – your personal text styler!\n\n🔠 Send me any text, and I'll turn it into <b>cool & unique fonts</b> instantly.\n\n🎨 Try it out now and give your words a stylish touch!\n\n🚀 Made with ❤️ by <b>@{owner_username}</b>"""
    buttons = [[
        InlineKeyboardButton('🔰 𝗖𝗛𝗔𝗡𝗡𝗘𝗟', url=f"https://t.me/{AUTH_CHANNEL_USERNAME}"),
        InlineKeyboardButton('🎛️ 𝗖𝗥𝗘𝗔𝗧𝗢𝗥', url=f"https://t.me/{owner_username}")
    ]]
    await m.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex('^try_again'))
async def try_again(c, m):
    if not await is_subscribed(c, m.from_user.id):
        await m.answer("❌ You must join the channel first to continue!")
        return
    await m.message.edit("✅ You're now subscribed! Feel free to continue using the bot.")



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
         InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡', callback_data='style+cloud'),
        InlineKeyboardButton('H̆̈ă̈p̆̈p̆̈y̆̈', callback_data='style+happy'),
        InlineKeyboardButton('S̑̈ȃ̈d̑̈', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('🇸 🇵 🇪 🇨 🇮 🇦 🇱 ', callback_data='style+special'),
        InlineKeyboardButton('🅂🅀🅄🄰🅁🄴🅂', callback_data='style+squares'),
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
        InlineKeyboardButton('R҉a҉y҉s҉', callback_data='style+rays'),
        InlineKeyboardButton('B҈i҈r҈d҈s҈', callback_data='style+birds'),
        InlineKeyboardButton('S̸l̸a̸s̸h̸', callback_data='style+slash'),
        ],[
        InlineKeyboardButton('s⃠t⃠o⃠p⃠', callback_data='style+stop'),
        InlineKeyboardButton('S̺͆k̺͆y̺͆l̺͆i̺͆n̺͆e̺͆', callback_data='style+skyline'),
        InlineKeyboardButton('A͎r͎r͎o͎w͎s͎', callback_data='style+arrows'),
        ],[
        InlineKeyboardButton('ዪሀክቿነ', callback_data='style+qvnes'),
        InlineKeyboardButton('S̶t̶r̶i̶k̶e̶', callback_data='style+strike'),
        InlineKeyboardButton('F༙R༙O༙Z༙E༙N༙', callback_data='style+frozen')
        ],[
        InlineKeyboardButton("❌ 𝗖𝗟𝗢𝗦𝗘 ❌", callback_data="close")
        ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    font_styles = {
        'typewriter': Fonts.typewriter,
        'outline': Fonts.outline,
        'serif': Fonts.serief,
        'bold_cool': Fonts.bold_cool,
        'cool': Fonts.cool,
        'small_cap': Fonts.smallcap,
        'script': Fonts.script,
        'script_bolt': Fonts.bold_script,
        'tiny': Fonts.tiny,
        'comic': Fonts.comic,
        'sans': Fonts.san,
        'slant_sans': Fonts.slant_san,
        'slant': Fonts.slant,
        'sim': Fonts.sim,
        'circles': Fonts.circles,
        'circle_dark': Fonts.dark_circle,
        'gothic': Fonts.gothic,
        'gothic_bolt': Fonts.bold_gothic,
        'cloud': Fonts.cloud,
        'happy': Fonts.happy,
        'sad': Fonts.sad,
        'special': Fonts.special,
        'squares': Fonts.square,
        'squares_bold': Fonts.dark_square,
        'andalucia': Fonts.andalucia,
        'manga': Fonts.manga,
        'stinky': Fonts.stinky,
        'bubbles': Fonts.bubbles,
        'underline': Fonts.underline,
        'ladybug': Fonts.ladybug,
        'rays': Fonts.rays,
        'birds': Fonts.birds,
        'slash': Fonts.slash,
        'stop': Fonts.stop,
        'skyline': Fonts.skyline,
        'arrows': Fonts.arrows,
        'qvnes': Fonts.rvnes,
        'strike': Fonts.strike,
        'frozen': Fonts.frozen
    }

    if style in font_styles:
        new_text = font_styles[style](m.message.reply_to_message.text)

        # "Copy Text" and "Back" buttons
        buttons = [[
        InlineKeyboardButton("📋 𝗖𝗢𝗣𝗬 𝗧𝗘𝗫𝗧", callback_data=f"copy_text+{new_text}"),
        InlineKeyboardButton("🔙 𝗖𝗛𝗢𝗢𝗦𝗘 𝗔𝗡𝗢𝗧𝗛𝗘𝗥 𝗙𝗢𝗡𝗧", callback_data="back_to_fonts")]]
        try:
            await m.message.edit_text(new_text, reply_markup=InlineKeyboardMarkup(buttons))
        except:
            pass

@Client.on_callback_query(filters.regex('^copy_text'))
async def copy_text(c, m):
    await m.answer("✅ Text copied to clipboard!\n(Just long-press the text to copy it.)", show_alert=True)

@Client.on_callback_query(filters.regex('^back_to_fonts'))
async def back_to_fonts(c, m):
    await m.answer()
    await style_buttons(c, m, cb=True)  # Show the font selection buttons again



@Client.on_callback_query(filters.regex('^close'))
async def close_button(c, m):
    await m.message.delete()
