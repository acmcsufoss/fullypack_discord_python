import os
from dotenv import load_dotenv
import discord

# load token from .env
load_dotenv()
token = os.getenv("DISCORD_TOKEN")


class Client(discord.Client):

    # This function is called when the bot is ready to start
    async def on_ready(self: discord.Client):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    # This function is triggered on ALL messages
    async def on_message(self, message: discord.Message):

        # Ignore message if from bot
        if message.author.bot:
            return

        if message.__contains__(f'<@{self.client.user.id}'):
            message.reply("Pong!")


def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = Client(intents=intents)
    client.run(token)


if __name__ == "__main__":
    main()
