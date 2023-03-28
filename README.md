# Discord_Python FullyPack

> A premade Discord bot using discord.py!

- [Discord_Python FullyPack](#discord_python-fullypack)
  - [About FullyPacks 🐘🎁](#about-fullypacks-)
  - [About discord.py](#about-discordpy)
  - [How to Run Locally](#how-to-run-locally)
  - [Generating an invite link](#generating-an-invite-link)
  - [Resources](#resources)

## About FullyPacks 🐘🎁

Welcome to `fullypack_discord_python`, one of a [_curated collection of Github templates_](https://github.com/orgs/acmcsufoss/repositories?q=fullypack_&type=all&sort=stargazers) designed to kickstart your project and help you get up and running in no time!

## About [discord.py](https://discordpy.readthedocs.io/en/stable/)

Discord.py is a Python library for building Discord bots. It provides an easy-to-use interface for interacting with the Discord API, allowing developers to create bots that can perform a wide range of tasks, such as moderating channels, automating tasks, and responding to user commands.

Using discord.py, developers can create custom commands, event listeners, and message handlers to interact with the Discord API. They can also integrate external APIs, such as weather APIs or news APIs, to provide additional functionality to their bots.

## How to Run Locally

1. Install Python 3.8 or later
2. Create a virtual environment:

   ```terminal
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   Linux

   ```terminal
   source venv/bin/activate
   ```

   Windows

   ```terminal
   venv/scripts/activate
   ```

4. Install dependencies:

   ```terminal
   pip install -r requirements.txt
   ```

5. Run the app:

   ```terminal
   python3 src/client.py
   ```

## Generating an invite link

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select your bot application.

2. Navigate to the **OAuth2** tab on the left-hand side of the screen.

3. Under the **OAuth2 URL Generator** section, select the **bot** checkbox under the **Scopes** section.

4. Scroll down to the **Bot Permissions** section and select the permissions you want your bot to have.

5. Copy the generated OAuth2 URL under the **Scopes** section.

6. Paste the generated URL into your browser and authorize the bot to join your server.

## Resources

- [discord.py documentaton](https://discordpy.readthedocs.io/en/stable/)
