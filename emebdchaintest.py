# from embedchain import OpenSourceApp
# app = OpenSourceApp()

# # app.add("https://nav.al/agi", data_type="web_page")
# app.add("https://en.wikipedia.org/wiki/Elon_Musk", data_type="web_page")
# # print(app.chat('Can you tell me who Naval Ravikant is?', dry_run=True))
# print(app.count())
# print(app.query('ow many companies does Elon Musk run?'))


# while True:
#     print(app.query(input("ASK -> ")))

import sqlite3
print(sqlite3.sqlite_version_info)

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from embedchain import OpenSourceApp
from embedchain import App

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/ec ", intents=intents)
root_folder = os.getcwd()


def initialize_chat_bot():
    global chat_bot
    chat_bot = OpenSourceApp()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    initialize_chat_bot()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await send_response(ctx, "Invalid command. Please refer to the documentation for correct syntax.")
    else:
        print("Error occurred during command execution:", error)


@bot.command()
async def add(ctx, data_type: str, *, url_or_text: str):
    print(f"User: {ctx.author.name}, Data Type: {data_type}, URL/Text: {url_or_text}")
    try:
        chat_bot.add(data_type, url_or_text)
        await send_response(ctx, f"Added {data_type} : {url_or_text}")
    except Exception as e:
        await send_response(ctx, f"Failed to add {data_type} : {url_or_text}")
        print("Error occurred during 'add' command:", e)


@bot.command()
async def query(ctx, *, question: str):
    print(f"User: {ctx.author.name}, Query: {question}")
    try:
        response = chat_bot.chat(question)
        await send_response(ctx, response)
    except Exception as e:
        await send_response(ctx, "An error occurred. Please try again!")
        print("Error occurred during 'query' command:", e)


async def send_response(ctx, message):
    if ctx.guild is None:
        await ctx.send(message)
    else:
        await ctx.reply(message)


bot.run("OTc5NjQ3MTEwMTA0MzU4OTIy.GIu6Hp.rkPoy55gAbtl3l4DbQ4HzXHl_rlIbVNh83ZVws")