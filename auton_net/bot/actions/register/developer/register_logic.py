import json
from datetime import datetime

import telegram
from telegram import Update
from telegram.ext import CallbackContext
from auton_net.bot.database import CreateDeveloperDatapoint


async def register_anonymous_logic(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data.split("dev_reg#anon>>")[1] == "yes":
        selection = True
    elif query.data.split("dev_reg#anon>>")[1] == "no":
        selection = False
    else:
        selection = False
    selection_readable = query.data.split("dev_reg#anon>>")[1]
    await query.answer()
    context.user_data['dev_reg#var><isAnon'] = selection
    context.user_data['dev_reg#var><isAnonReadable'] = selection_readable.capitalize()
    # Selection is Yes on remaining anonymous, ask for nickname
    if selection:
        context.user_data['dev_reg#anon#nickname#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'\nWhat nickname would you like to go by?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'\nWhat nickname would you like to go by?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
    else:
        # Selection is No on remaining anonymous, default nickname is TG name
        context.user_data['dev_reg#budget#min#awaiting'] = True
        context.user_data['dev_reg#var><nickname'] = update.effective_user.name
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'\nWhat is the lowest price you would accept? (In USD)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'\nWhat is the lowest price you would accept? (In USD)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )


async def register_nickname_logic(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data.split("dev_reg#nick#confirmation>>")[1] == "yes":
        selection = True
    elif query.data.split("dev_reg#nick#confirmation>>")[1] == "no":
        selection = False
    else:
        selection = False
    """
    if selection is True, show next menu, false show previous menu
    """
    if not selection:  # Selection is False, show previous menu.
        context.user_data['dev_reg#anon#nickname#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'\nWhat nickname would you like to go by?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'\nWhat nickname would you like to go by?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
    else:
        # Show next menu
        context.user_data['dev_reg#budget#min#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'\nWhat is the lowest price you would accept? (In USD)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'\nWhat is the lowest price you would accept? (In USD)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )


async def register_minimum_budget(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data.split("dev_reg#min_budget#confirmation>>")[1] == "yes":
        selection = True
    elif query.data.split("dev_reg#min_budget#confirmation>>")[1] == "no":
        selection = False
    else:
        selection = False
    """
    if selection is True, show next menu, false show previous menu
    """
    if not selection:  # Selection is False, show previous menu.
        context.user_data['dev_reg#budget#min#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'\nAre you sure this is the minimum accepted price you want?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'\nAre you sure this is the minimum accepted price you want?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
    else:
        # Show next menu
        context.user_data['dev_reg#budget#max#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'\nWhat is the highest price you would accept? (In USD)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'\nWhat is the highest price you would accept? (In USD)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )


async def register_maximum_budget(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data.split("dev_reg#max_budget#confirmation>>")[1] == "yes":
        selection = True
    elif query.data.split("dev_reg#max_budget#confirmation>>")[1] == "no":
        selection = False
    else:
        selection = False
    """
    if selection is True, show next menu, false show previous menu
    """
    if not selection:  # Selection is False, show previous menu.
        context.user_data['dev_reg#budget#max#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'\nAre you sure this is the maximum accepted price you want?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'\nAre you sure this is the maximum accepted price you want?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
    else:
        # Show next menu
        context.user_data['dev_reg#timeframe#min#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'\nWhat is the minimum timeframe you would accept? (In days)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'\nWhat is the minimum timeframe you would accept? (In days)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )


async def register_minimum_timeframe(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data.split("dev_reg#min_timeframe#confirmation>>")[1] == "yes":
        selection = True
    elif query.data.split("dev_reg#min_timeframe#confirmation>>")[1] == "no":
        selection = False
    else:
        selection = False
    """
    if selection is True, show next menu, false show previous menu
    """
    if not selection:  # Selection is False, show previous menu.
        context.user_data['dev_reg#budget#max#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'\nAre you sure this is the minimum accepted timeframe you want?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'\nAre you sure this is the minimum accepted timeframe you want?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
    else:
        # Show next menu
        context.user_data['dev_reg#timeframe#max#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'\nWhat is the maximum timeframe you would accept? (In days)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'\nWhat is the maximum timeframe you would accept? (In days)',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )


async def register_maximum_timeframe(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data.split("dev_reg#max_timeframe#confirmation>>")[1] == "yes":
        selection = True
    elif query.data.split("dev_reg#max_timeframe#confirmation>>")[1] == "no":
        selection = False
    else:
        selection = False
    """
    if selection is True, show next menu, false show previous menu
    """
    if not selection:  # Selection is False, show previous menu.
        context.user_data['dev_reg#budget#max#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'\nAre you sure this is the minimum accepted timeframe you want?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'\nAre you sure this is the minimum accepted timeframe you want?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
    else:
        # Show next menu
        context.user_data['dev_reg#wallet_addr#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                     f'\nWhat is the ethereum wallet address you want to link to this account?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                     f'\nWhat is the ethereum wallet address you want to link to this account?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )


async def register_wallet_address(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data.split("dev_reg#wallet_addr#confirmation>>")[1] == "yes":
        selection = True
    elif query.data.split("dev_reg#wallet_addr#confirmation>>")[1] == "no":
        selection = False
    else:
        selection = False
    """
    if selection is True, show next menu, false show previous menu
    """
    if not selection:  # Selection is False, show previous menu.
        context.user_data['dev_reg#wallet_addr#awaiting'] = True
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                     f'<strong>Ethereum Wallet Address</strong> <code>{context.user_data["dev_reg#var><eth_address"]}</code>\n' + \
                     f'\nWhat is the ethereum wallet address you want to link to this account?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
        else:
            await update.message.delete()
            await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                     f'<strong>Ethereum Wallet Address</strong> <code>{context.user_data["dev_reg#var><eth_address"]}</code>\n' + \
                     f'\nWhat is the ethereum wallet address you want to link to this account?',
                parse_mode='HTML',
                reply_markup=telegram.ForceReply()
            )
    else:
        # Show next menu
        context.user_data['dev_reg#wallet_addr#awaiting'] = False
        message = None
        if update.message is None:
            await update.callback_query.message.delete()
            await update.callback_query.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                     f'<strong>Ethereum Wallet Address</strong> <code>{context.user_data["dev_reg#var><eth_address"]}</code>\n' + \
                     f'\nRegistration in process...',
                parse_mode='HTML',
                reply_markup=None
            )
        else:
            await update.message.delete()
            message = await update.message.reply_text(
                text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                     f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                     f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                     f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                     f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                     f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                     f'<strong>Maximum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                     f'<strong>Ethereum Wallet Address</strong> <code>{context.user_data["dev_reg#var><eth_address"]}</code>\n' + \
                     f'\nRegistration in process...',
                parse_mode='HTML',
                reply_markup=None
            )
            st_time = datetime.now()
            try:
                user_data = (
                    1 if context.user_data["dev_reg#var><isAnonReadable"] == "Yes" else 0,  # U-0
                    context.user_data["dev_reg#var><nickname"],  # U-1
                    context.user_data["dev_reg#var><min_budget"],  # U-2
                    context.user_data["dev_reg#var><max_budget"],  # U-3
                    context.user_data["dev_reg#var><min_timeframe"],  # U-4
                    context.user_data["dev_reg#var><max_timeframe"],  # U-5
                    context.user_data["dev_reg#var><eth_address"]  # U-6
                )
                CreateDeveloperDatapoint.create_developer(
                    host=context.bot_data["database_host"],
                    database=context.bot_data["database_database"],
                    username=context.bot_data["database_user"],
                    password=context.bot_data["database_password"],
                    telegram_id=update.effective_user.id,
                    accepted_budget_min=user_data[2],
                    accepted_budget_max=user_data[3],
                    accepted_worktime_min=user_data[4],
                    accepted_worktime_max=user_data[5],
                    isAnonymous=user_data[0],
                    nickname=user_data[1],
                    wallet_address=user_data[6]
                )
            except Exception as e:
                raise e
            # After account creation edit the message that the account was created successfully
            if not message:
                raise Exception("Account creation message was not sent!")
            await message.edit_text(
                text= \
                    f"<strong>Successfully registered!<strong>\n\n" + \
                    f"<strong>Welcome to the AutonNET Seller Family!</strong>" + \
                    f"\n\nHere's some statistics for you to think about while we re-direct you\n" + \
                    f"to the seller panel we created for you!\n\n" + \
                    f"Your registration took roughly <strong>{datetime.now() - st_time} seconds</strong>!\n" + \
                    
            )


async def register_logic(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if 'devRegistration' in context.user_data:
        if context.user_data['devRegistration']:
            # Developer Registration
            if query.data.startswith("dev_reg#anon>>"):
                await register_anonymous_logic(update, context)
            # Nickname Registration Confirmation
            if query.data.startswith("dev_reg#nick#confirmation>>"):
                await register_nickname_logic(update, context)
            # Minimum Budget Confirmation
            if query.data.startswith("dev_reg#min_budget#confirmation>>"):
                await register_minimum_budget(update, context)
            # Maximum Budget Confirmation
            if query.data.startswith("dev_reg#max_budget#confirmation>>"):
                await register_maximum_budget(update, context)
            # Minimum Timeframe Confirmation
            if query.data.startswith("dev_reg#min_timeframe#confirmation>>"):
                await register_minimum_timeframe(update, context)
            # Maximum Timeframe Confirmation
            if query.data.startswith("dev_reg#max_timeframe#confirmation>>yes"):
                await register_maximum_timeframe(update, context)
            # Wallet Address Confirmation
            if query.data.startswith("dev_reg#wallet_addr#confirmation>>"):
                await register_wallet_address(update, context)
