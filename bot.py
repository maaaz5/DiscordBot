import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()


# Intents definition
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Slash command: How are you?


@bot.slash_command(name='hru', description='Check how the bot is doing.')
async def hru(ctx):
    await ctx.send('Good!')


@bot.slash_command(name='hola', description='spanish bot :)')
async def hola(ctx):
    await ctx.send('hola mi hermano!')


@bot.slash_command(name='ping', help='Check the bot\'s latency')
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert to milliseconds
    await ctx.send(f'Pong! Latency: {latency}ms')


@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    await ctx.send(f"Result: {result}")
# Event: Respond to messages


@bot.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent an infinite loop
    if message.author == bot.user:
        return

    # Check if the message content contains "hello"
    if 'hello' in message.content.lower():
        # Respond with a greeting
        await message.channel.send(f'Hi {message.author.mention}!')

    # Allow other events to be processed
    await bot.process_commands(message)

# Run the bot with the token
bot.run(os.getenv('BOT_TOKEN'))
