import asyncio

import telegram.constants
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, MessageHandler, CallbackContext, \
    ContextTypes
from telegram.ext import filters  # Correct import
import re
import time
from ..modules.cryptocurrency import Cryptocurrency,Constants,CouldNotConnect,ChecksumAddress

# Initiated when started
cryptocurrency: Cryptocurrency = None

class MyTelegramBot:
    def __init__(self, token: str, cryptomodule: Cryptocurrency):
        self.token = token
        self.cryptocurrency = cryptomodule
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> ApplicationBuilder:
        app = ApplicationBuilder().token(self.token).build()
        app.add_handler(CallbackQueryHandler(self.button))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.text_input))
        app.add_handler(CommandHandler("start", self.start))
        return app
    async def start(self, update: Update, context: CallbackContext, message: str = None) -> None:
        caption = f'<strong>{message}</strong>' if message else f'<strong>Hi {update.effective_user.name}!</strong>'
        """Sends a message with three inline buttons attached."""
        keyboard = [
            [InlineKeyboardButton("💸 Wallet & Balance 💸", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Connect Wallet", callback_data="wallet_connect"),
                InlineKeyboardButton("$CSL Balance (WIP)", callback_data="csl_balance"),
                InlineKeyboardButton("My Wallet", callback_data="display_wallet_address")
            ],
            [InlineKeyboardButton("🛠️ Services & Invoices 🧾", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("My Services (WIP)", callback_data="wallet_connect"),
                InlineKeyboardButton("Order Service (WIP)", callback_data="csl_balance"),
                InlineKeyboardButton("My Invoices (WIP)", callback_data="3")
            ],
            [InlineKeyboardButton("🧾 Info, Roadmap and Whitepaper 📑", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Bot Info", callback_data="bot_info"),
                InlineKeyboardButton("Roadmap", url="https://whitepaper.csl.sh/development-roadmap"),
                InlineKeyboardButton("Whitepaper", url="https://whitepaper.csl.sh")
            ],
            [InlineKeyboardButton("🔎 Open Source Intelligence Gathering (OSINT) 🔍", callback_data="ignore_0xdead")],
            #[InlineKeyboardButton("Option 3", callback_data="3")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        if update.message is None:
            await update.callback_query.message.reply_photo(
                caption=caption,
                parse_mode='HTML',
                photo=open("bots/images/banner.jpg", "rb"),
                reply_markup=reply_markup
            )
        else:
            await update.message.reply_photo(
                caption=caption,
                parse_mode='HTML',
                photo=open("bots/images/banner.jpg", "rb"),
                reply_markup=reply_markup
            )

    async def ask_for_input(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Prompt user to input data"""
        # Remove existing inline keyboard
        #a#wait update.callback_query.message.edit_reply_markup(reply_markup=None)
        # Send a new message prompting user to input data
        await update.callback_query.message.reply_text("Enter Wallet Address")

    async def ask_address_confirmation(self, update: Update, context: ContextTypes.DEFAULT_TYPE, wallet_address: str) -> None:
        """Ask the user if the wallet address is correct."""
        keyboard = [
            [
                InlineKeyboardButton("Yes!", callback_data="address_correct"),
                InlineKeyboardButton("No, I want to change it", callback_data="change_address"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            f"Is the address correct?\n\n<b>{wallet_address}</b>",
            reply_markup=reply_markup,
            parse_mode='HTML'
        )

    async def handle_wallet_input(self, update: Update, context: CallbackContext) -> None:
        """Handle user's wallet address input"""
        while True:
            wallet_address = update.message.text
            if wallet_address.lower() == 'c':
                # If the user cancels, inform them and return
                await update.message.reply_text("Operation cancelled.")
                return

            if re.match(r'^0x[a-fA-F0-9]{40}$', wallet_address):
                # Set the wallet address in user_data
                context.user_data['wallet_address'] = wallet_address
                # Here you can process the wallet address input
                await self.ask_address_confirmation(update, context, wallet_address)
                # Transition to the state where we expect TxHash input
                context.user_data['state'] = 'waiting_txhash_input'
                break  # Break out of the loop since a valid address is provided
            else:
                # If the wallet address is invalid, inform the user and ask for a new input
                await update.message.reply_text(
                    "Invalid address! Please enter a valid Ethereum wallet address, or 'c' to cancel.")
                # Wait for the next message
                try:
                    update = await context.bot.get_updates(offset=update.update_id + 1, timeout=20).result()[0]
                except AttributeError:
                    update = await context.bot.get_updates(offset=update.update_id + 1, timeout=20)

    async def handle_address_confirmation(self, update: Update, context: CallbackContext, wallet_address: str) -> None:
        """Handle the user's response to the address confirmation."""
        query = update.callback_query
        if query.data == "address_correct":
            await query.answer()
            await query.edit_message_text("Great! Your wallet address is valid!")
            # Print the address to the terminal
            print(f"Wallet Address: {wallet_address}")
            # Now you can continue with your bot logic
            context.user_data['state'] = 'waiting_txhash_input'
            await self.ask_txhash_input(update, context)  # Prompt user to input TxHash
        elif query.data == "change_address":
            await query.answer()
            await self.ask_for_input(update, context)  # Prompt user to input new wallet address
            # Transition to the state where we expect wallet address input
            context.user_data['state'] = 'waiting_wallet_input'

    async def ask_txhash_input(self, update: Update, context: CallbackContext) -> None:
        """Prompt user to input transaction hash (TxHash)"""
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="Enter Transaction Hash (TxHash)")

    async def ask_txhash_confirmation(self, update: Update, context: CallbackContext, txhash: str) -> None:
        """Ask the user if the transaction hash is correct."""
        if update:
            wallet_address = context.user_data.get('wallet_address', '')
            if wallet_address:
                keyboard = [
                    [
                        InlineKeyboardButton("Verify Address", callback_data="verify_address"),
                        InlineKeyboardButton("Cancel", callback_data="cancel_verification"),
                    ]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                message_text = (
                    f"The verification process will use the following addresses!\n\n"
                    f"<b>Wallet Address:</b> <code>{wallet_address}</code>\n"
                    f"<b>TxHash Address:</b> <code>{txhash}</code>\n\n"
                    "Click <strong>Verify Address</strong> to proceed or <strong>Cancel</strong> to abort."
                )
                await update.message.reply_text(
                    text=message_text,
                    reply_markup=reply_markup,
                    parse_mode='HTML'
                )
            else:
                await update.message.reply_text("Sorry, wallet address not found. Please try again.")
        else:
            await update.message.reply_text("Sorry, something went wrong. Please try again.")

    async def handle_txhash_input(self, update: Update, context: CallbackContext) -> None:
        """Handle user's transaction hash (TxHash) input"""
        txhash = update.message.text
        # Store the TxHash in user_data
        context.user_data['txhash'] = txhash
        # Ask for confirmation
        await self.ask_txhash_confirmation(update, context, txhash)

    async def handle_txhash_confirmation(self, update: Update, context: CallbackContext, txhash: str) -> None:
        """Handle the user's response to the TxHash confirmation."""
        query = update.callback_query
        if query.data == "txhash_correct":
            await query.answer()
            await query.edit_message_text("Great! Your transaction hash is correct!")
            print(txhash)
            # Continue with your bot logic
        elif query.data == "change_txhash":
            await query.answer()
            await self.ask_txhash_input(update, context)  # Prompt user to input new TxHash
            # Transition to the state where we expect TxHash input
            context.user_data['state'] = 'waiting_txhash_input'

    async def clear_chat_and_send_menu(self, update: Update, context: CallbackContext) -> None:
        """Clear all messages in the chat and resend the menu."""
        chat_id = update.effective_chat.id
        message_id = update.effective_message.message_id
        await context.bot.delete_message(chat_id, message_id)

        # Send the start menu again
        await self.start(update, context)

    async def verify_address(self, update: Update, context: CallbackContext) -> None:
        wallet_address = context.user_data.get('wallet_address')
        txHash = context.user_data.get('txhash')

        if wallet_address is None or txHash is None:
            await update.callback_query.answer("Wallet address or TxHash is missing.")
            return

        verification_response = self.cryptocurrency.verify_address(txHash, wallet_address)
        if verification_response[0]:
            await update.callback_query.message.reply_text(verification_response[1], parse_mode='HTML')
        else:
            await update.callback_query.message.reply_text(verification_response[1], parse_mode='HTML')

        await asyncio.sleep(1.5)
        await self.clear_chat_and_send_menu(update, context)

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Parses the CallbackQuery and updates the message text."""
        query = update.callback_query
        if query.data == "ignore_0xdead": await query.answer()
        if query.data == "wallet_connect":
            await self.ask_for_input(update, context)  # Prompt user to input wallet address
            # Transition to the state where we expect wallet address input
            context.user_data['state'] = 'waiting_wallet_input'
        elif query.data == "address_correct":
            await self.handle_address_confirmation(update, context, context.user_data['wallet_address'])  # Pass the wallet address
        elif query.data == "txhash_correct":
            await self.handle_txhash_confirmation(update, context, context.user_data['txhash'])  # Pass the wallet address
        elif query.data == "cancel_verification":
            await self.clear_chat_and_send_menu(update,context)
        elif query.data == "verify_address":
            await self.verify_address(update,context)
        else:
            await query.answer()  # Answer other callback queries

    async def text_input(self, update: Update, context: CallbackContext) -> None:
        """Handle user's text input"""
        # Check if the user is in the state of waiting for wallet input or TxHash input
        if context.user_data.get('state') == 'waiting_wallet_input':
            await self.handle_wallet_input(update, context)
            # Reset the conversation state
            del context.user_data['state']
        elif context.user_data.get('state') == 'waiting_txhash_input':
            await self.handle_txhash_input(update, context)
            # Reset the conversation state
            del context.user_data['state']
        else:
            await update.message.reply_text("I'm not expecting any input at the moment.")

    def run(self):
        """Run the bot"""
        self.app.run_polling()

def test_functions():
    print("Running CryptoAddrValidation v1.0 Test")
    _addrs = [
    [
        "0x66D485bF61adE6E20F7B73B6645E18cd1c66eC00", # Fake
        "0x5076Ad3b087BA6CA688173474e9eAc2D121a2c75",
        "0xbB53Db33351Ee6eeFf52e8EDdD5EE87e3613b900", # Fake
        "0xe656DA3623E4C9192Ba45a787909BEE4D1702F90",
        "0x28621aFF0d68F44BF3B0F49c999b0224b5f20e00", # Fake
        "0x13B25bCE83B203623EaC145DCE97abCC78FA01Cd",
        "0x590aC463b0a0309D26CC5E015b31C691aAD95700", # Fake
        "0xa574564EF3aBD9D75B485aae1243A6563cAa7037",
        "0x1c30b60f5c3C2f7C233A232528C5788A2d45b300", # Fake
        "0x5f1278829111dbFbd7F37CAcCf85820B7F655EF3",
    ]]

    for i in range(len(_addrs)):
        print(f"Testing ETH wallet addresses.")
        for addr in _addrs[i]:
            _st = time.time()
            try:
                if Cryptocurrency.is_address(addr):
                    print(f"{addr} is Valid | Time took: {time.time() - _st}ms")
                else:
                    print(f"{addr} is Invalid | Time took: {time.time() - _st}ms")
            except Exception as e:
                print(f"{addr} is Invalid | Time took: {time.time() - _st}ms")



def run_app(token: str, cryptomodule: Cryptocurrency) -> ApplicationBuilder:
    test_functions()
    bot = MyTelegramBot(token, cryptomodule)
    bot.run()