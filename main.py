from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: Load token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

client = Client(intents=Intents.default())

# STEP 2: Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# STEP 3: Handling Startup for your bot:
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# STEP 4: Handling Incoming Messages:
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    user_message = message.content
    if isinstance(user_message, str):
        await send_message(message, user_message)
    else:
        print('Received non-string message content')

client.run(TOKEN)