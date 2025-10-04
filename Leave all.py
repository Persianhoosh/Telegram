
#Fallow me on:
#https://T.me/AiHoma
#https://github.com/Aihoma
#https://medium.com/@AiHoma


from telethon import TelegramClient, functions, types
import asyncio

# Replace these with your own API ID, API Hash, and Phone Number
API_ID = 'YOUR_API_ID'  # Your Telegram API ID
API_HASH = 'YOUR_API_HASH'  # Your Telegram API Hash
PHONE_NUMBER = '+YOUR_PHONE_NUMBER'  # Your registered phone number with international format

# Create a Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

async def leave_all_groups_and_channels():
    """
    Leave all Telegram groups and channels for the logged-in user.
    """
    # Start the client
    await client.start(phone=PHONE_NUMBER)
    
    # Fetch all dialogs (chats, groups, and channels)
    dialogs = await client.get_dialogs()
    
    for dialog in dialogs:
        # Check if the dialog is a group or a channel
        if isinstance(dialog.entity, (types.Chat, types.Channel)):
            try:
                if isinstance(dialog.entity, types.Chat):
                    # Leave a basic group
                    await client(functions.messages.DeleteChatUserRequest(
                        chat_id=dialog.entity.id,
                        user_id='me'
                    ))
                    print(f'✅ Left group: {dialog.name or dialog.title}')
                elif isinstance(dialog.entity, types.Channel):
                    # Leave a supergroup or channel
                    await client(functions.channels.LeaveChannelRequest(
                        channel=dialog.entity
                    ))
                    print(f'✅ Left channel/supergroup: {dialog.name or dialog.title}')
            except Exception as e:
                print(f'❌ Failed to leave {dialog.name or dialog.title}: {e}')
        else:
            # Skip private chats
            print(f'⏩ Skipped private chat: {dialog.name or dialog.title}')
    
    # Disconnect the client
    await client.disconnect()

# Run the function
if __name__ == '__main__':
    asyncio.run(leave_all_groups_and_channels())
