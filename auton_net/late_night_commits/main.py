"""
███╗░░░███╗░█████╗░██╗███╗░░██╗░░░██████╗░██╗░░░██╗
████╗░████║██╔══██╗██║████╗░██║░░░██╔══██╗╚██╗░██╔╝
██╔████╔██║███████║██║██╔██╗██║░░░██████╔╝░╚████╔╝░
██║╚██╔╝██║██╔══██║██║██║╚████║░░░██╔═══╝░░░╚██╔╝░░
██║░╚═╝░██║██║░░██║██║██║░╚███║██╗██║░░░░░░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░░░░╚═╝░░░
"""
async def updateBotStoredOpenConversation(self, context: CallbackContext) -> None:
        fprint("SCHEDULER//G_ACONV", "Gathering all active conversations!")
        context.bot_data["openConversations"] = RetrieveConversations.get_all_conversations({
            'host': context.bot_data["database_host"],
            'database': context.bot_data["database_database"],
            'username': context.bot_data["database_user"],
            'password': context.bot_data["database_password"]
        })
        fprint("SCHEDULER//G_ACONV", f"Successfully gathered all active conversations! There are currently {len(context.bot_data['openConversations'])} conversations")

    async def delete_message(self,context: CallbackContext) -> None:
        job = context.job
        try:
            # Attempt to delete the message
            fprint("GRBGE", f"Attempting to {job.name} | Data: {job.data}")
            await self.app.bot.delete_message(chat_id=job.data[0], message_id=job.name.split('_')[-1])
        except Exception as e:
            print(f"Failed to delete message: {e}")

    async def test_contact(self, update: Update, context: CallbackContext) -> None:
        args = context.args
        bot: Bot = context.bot
        fprint("MFPC","Confirming connection to " + str(args[0]))
        if len(args) == 1:
            fprint("MFPC","Sending message to " + str(args[0]))
            seller_stats = GetDeveloperInformation.get_developer_information(
                host=context.bot_data['database_host'],
                database=context.bot_data['database_database'],
                username=context.bot_data['database_user'],
                password=context.bot_data['database_password'],
                telegram_id=update.effective_user.id
            )
            message = await bot.send_message(
                chat_id=args[0],
                text=f"<code>{seller_stats[1][7]}</code> wants to talk with you?\nDo you accept?\n\n<strong>This message will automatically be deleted in 2 minutes!</strong>",
                parse_mode='HTML',
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(text="Yes", callback_data=f"create_conversation#IID>{update.effective_user.id}//PID#{args[0]}"),
                        InlineKeyboardButton(text="No", callback_data="delete_message#confirmation"),
                    ]
                ])
            )
            # Auto Delete message
            context.job_queue.run_once(
                callback=self.delete_message,
                when=120,  # Delay in seconds after which the message should be deleted
                data=[message.chat_id],  # Pass the chat_id as context to the callback function
                name=f"delete_message_{message.message_id}"  # A unique name for the job
            )
            if update.message is None:
                await update.callback_query.message.delete()
                await update.callback_query.message.reply_text(
                    text="Awaiting for a response from the other person",
                    parse_mode='HTML',
                )
            else:
                await update.message.delete()
                await update.message.reply_text(
                    text="Awaiting for a response from the other person",
                    parse_mode='HTML',
                )
