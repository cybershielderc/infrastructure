from telegram.ext import CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


async def handle_seller_text_input(update: Update, context: CallbackContext) -> None:
    if 'dev_reg#anon#nickname#awaiting' in context.user_data:
        if context.user_data['dev_reg#anon#nickname#awaiting']:
            if update.message.reply_to_message:
                # Capture message
                user_input = update.message.text
                await update.message.delete()
                await update.message.reply_to_message.delete()
                fprint("RTXI", f"U-{update.effective_user.id} gave {user_input} as a nickname")
                fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                context.user_data['dev_reg#anon#nickname#awaiting'] = False
                context.user_data['dev_reg#var><nickname'] = user_input
                fprint("RTXI", f"U-{update.effective_user.id}>> Saved Nickname to user data until confirmation")
                fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                await update.message.reply_text(
                    text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                         f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                         f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                         f'\nAre you sure this is the nickname you want?',
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('✅ Yes', callback_data='dev_reg#nick#confirmation>>yes'),
                                InlineKeyboardButton('❌ No', callback_data='dev_reg#nick#confirmation>>no')
                            ]
                        ]
                    )
                )
    if 'dev_reg#budget#min#awaiting' in context.user_data:
        if context.user_data['dev_reg#budget#min#awaiting']:
            if update.message.reply_to_message:
                # Capture message
                user_input = update.message.text
                await update.message.delete()
                await update.message.reply_to_message.delete()
                fprint("RTXI", f"U-{update.effective_user.id} gave {user_input}$ as a min budget")
                fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                context.user_data['dev_reg#budget#min#awaiting'] = False
                context.user_data['dev_reg#var><min_budget'] = user_input
                fprint("RTXI",
                       f"U-{update.effective_user.id}>> Saved Min Budget to user data until confirmation")
                fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                await update.message.reply_text(
                    text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                         f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                         f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                         f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                         f'\nAre you sure this is the minimum accepted price you want?',
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('✅ Yes',
                                                     callback_data='dev_reg#min_budget#confirmation>>yes'),
                                InlineKeyboardButton('❌ No',
                                                     callback_data='dev_reg#min_budget#confirmation>>no')
                            ]
                        ]
                    )
                )
    if 'dev_reg#budget#max#awaiting' in context.user_data:
        if context.user_data['dev_reg#budget#max#awaiting']:
            if update.message.reply_to_message:
                # Capture message
                user_input = update.message.text
                await update.message.delete()
                await update.message.reply_to_message.delete()
                fprint("RTXI", f"U-{update.effective_user.id} gave {user_input}$ as a max budget")
                fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                context.user_data['dev_reg#budget#max#awaiting'] = False
                context.user_data['dev_reg#var><max_budget'] = user_input
                fprint("RTXI",
                       f"U-{update.effective_user.id}>> Saved Min Budget to user data until confirmation")
                fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                await update.message.reply_text(
                    text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                         f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                         f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                         f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                         f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                         f'\nAre you sure this is the maximum accepted price you want?',
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('✅ Yes',
                                                     callback_data='dev_reg#max_budget#confirmation>>yes'),
                                InlineKeyboardButton('❌ No',
                                                     callback_data='dev_reg#max_budget#confirmation>>no')
                            ]
                        ]
                    )
                )
    if 'dev_reg#timeframe#min#awaiting' in context.user_data:
        if context.user_data['dev_reg#timeframe#min#awaiting']:
            if update.message.reply_to_message:
                # Capture message
                user_input = update.message.text
                await update.message.delete()
                await update.message.reply_to_message.delete()
                fprint("RTXI", f"U-{update.effective_user.id} gave {user_input} as a min timeframe")
                fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                context.user_data['dev_reg#timeframe#min#awaiting'] = False
                context.user_data['dev_reg#var><min_timeframe'] = user_input
                fprint("RTXI",
                       f"U-{update.effective_user.id}>> Saved Min Timeframe to user data until confirmation")
                fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                await update.message.reply_text(
                    text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                         f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                         f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                         f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                         f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                         f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
 \
                         f'\nAre you sure this is the minimum accepted timeframe you want?',
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('✅ Yes',
                                                     callback_data='dev_reg#min_timeframe#confirmation>>yes'),
                                InlineKeyboardButton('❌ No',
                                                     callback_data='dev_reg#min_timeframe#confirmation>>no')
                            ]
                        ]
                    )
                )
    if 'dev_reg#timeframe#max#awaiting' in context.user_data:
        if context.user_data['dev_reg#timeframe#max#awaiting']:
            if update.message.reply_to_message:
                # Capture message
                user_input = update.message.text
                await update.message.delete()
                await update.message.reply_to_message.delete()
                fprint("RTXI", f"U-{update.effective_user.id} gave {user_input} as a max timeframe")
                fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                context.user_data['dev_reg#timeframe#max#awaiting'] = False
                context.user_data['dev_reg#var><max_timeframe'] = user_input
                fprint("RTXI",
                       f"U-{update.effective_user.id}>> Saved Min Timeframe to user data until confirmation")
                fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                await update.message.reply_text(
                    text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                         f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                         f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                         f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                         f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                         f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                         f'<strong>Maximum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                         f'\nAre you sure this is the maximum accepted timeframe you want?',
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('✅ Yes',
                                                     callback_data='dev_reg#max_timeframe#confirmation>>yes'),
                                InlineKeyboardButton('❌ No',
                                                     callback_data='dev_reg#max_timeframe#confirmation>>no')
                            ]
                        ]
                    )
                )
    if 'dev_reg#wallet_addr#awaiting' in context.user_data:
        if context.user_data['dev_reg#wallet_addr#awaiting']:
            if update.message.reply_to_message:
                # Capture message
                user_input = update.message.text
                await update.message.delete()
                await update.message.reply_to_message.delete()
                fprint("RTXI", f"U-{update.effective_user.id} gave {user_input} as a eth wallet timeframe")
                fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                context.user_data['dev_reg#wallet_addr#awaiting'] = False
                context.user_data['dev_reg#var><eth_address'] = user_input
                fprint("RTXI",
                       f"U-{update.effective_user.id}>> Saved Eth address to user data until confirmation")
                fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                await update.message.reply_text(
                    text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                         f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                         f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                         f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                         f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                         f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                         f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                         f'<strong>Ethereum Wallet Address</strong> <code>{context.user_data["dev_reg#var><eth_address"]}</code>\n' + \
                         f'\nAre you sure this is the ethereum wallet address you want linked to your account?',
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('✅ Yes',
                                                     callback_data='dev_reg#wallet_addr#confirmation>>yes'),
                                InlineKeyboardButton('❌ No',
                                                     callback_data='dev_reg#wallet_addr#confirmation>>no')
                            ]
                        ]
                    )
                )
