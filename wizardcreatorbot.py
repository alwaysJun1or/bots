from telegram.ext import Updater, MessageHandler, Filters


# Function to handle messages and print the chat ID
def handle_message(update, context):
    # Print the full update object for debugging
    print(f"Full update: {update}")  # This will show the whole update object in the console

    # Check if the message object exists
    if update.channel_post.text:
        chat_id = update.channel_post.sender_chat.id
        print(f"Received a message in chat ID: {chat_id}")  # Debugging print
        # Send back the chat ID to the user
        update.channel_post.reply_text(f"Your chat ID is: {chat_id}")
    else:
        print("No message found in the update.")


def main():
    # Replace with your bot's token
    API_TOKEN = '7382406875:AAFqs3_zRZ7khUYmMDjLFTM5JXkssi7F-1I'

    # Create the Updater and dispatcher
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add the handler to respond to any text message (prints chat ID)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start polling for updates
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()