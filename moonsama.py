import discord
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext.commands import Bot
from discord.utils import get # New import
from discord.ext import commands # New import

token = "Discord Tokenhere"

intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT

bot = commands.Bot(command_prefix='=', intents=intents)

config = []
with open('config.txt', 'r') as c:
    for con in c:
        con = con.replace('\n', '')
        con = con.split()
        config.append(float(con[1]))


URL = 'https://mcapi.moonsama.com/game/minecraft-carnage-2022-11-27/carnage-stats/result/leaderboard?player='


@bot.command()

async def earned(ctx, contents: str):
    fullURL = URL + contents
    try:
        page = requests.get(fullURL)
    except:
        await ctx.send("Try another username!")
        return
    info = page.json()

    for item in info['leaderboards']:
        if item['itemId'] == 'sama':
            sama = item['leaderboard'][0]['amount']
        if item['itemId'] == 'mobidium':
            mobidium = item['leaderboard'][0]['amount']
        if item['itemId'] == 'blood_crystals':
            blood_crystals = item['leaderboard'][0]['amount']
        if item['itemId'] == 'dna':
            dna = item['leaderboard'][0]['amount']
        if item['itemId'] == 'stone':
            stone = item['leaderboard'][0]['amount']
        if item['itemId'] == 'wood':
            wood = item['leaderboard'][0]['amount']
        if item['itemId'] == 'iron':
            iron = item['leaderboard'][0]['amount']
        if item['itemId'] == 'gold':
            gold = item['leaderboard'][0]['amount']
        if item['itemId'] == 'fish_specimen':
            fish_specimen = item['leaderboard'][0]['amount']
    total_earned = 0
    msg = ""

    msg = msg + "CustomEmojiID " + str(sama) + "\n"
    total_earned = total_earned + int(sama) * config[0]
    msg = msg + "CustomEmojiID " + str(mobidium) + "\n"
    total_earned = total_earned + int(mobidium) * config[1]
    msg = msg + "CustomEmojiID " + str(blood_crystals) + "\n"
    total_earned = total_earned + int(blood_crystals) * config[2]
    msg = msg + "CustomEmojiID " + str(dna) + "\n"
    total_earned = total_earned + int(dna) * config[3]

    msg = msg + "CustomEmojiID " + str(stone) + "\n"
    total_earned = total_earned + int(stone) * config[4]

    msg = msg + "CustomEmojiID " + str(wood) + "\n"
    total_earned = total_earned + int(wood) * config[5]

    msg = msg + "CustomEmojiID " + str(iron) + "\n"
    total_earned = total_earned + int(iron) * config[6]

    msg = msg + "CustomEmojiID " + str(gold) + "\n"
    total_earned = total_earned + int(gold) * config[7]

    msg = msg + "CustomEmojiID " + str(fish_specimen) + "\n"
    total_earned = total_earned + int(fish_specimen) * config[8]

    msg = msg + "Total Earned: $" + str(round(total_earned, 2))
    embed = discord.Embed(title=contents+"'s stats", description=msg, color=0x87CEEB)
    embed.set_footer(text="minecraft-carnage-20.11.2022\n", icon_url="https://i.postimg.cc/hvJMBXtk/moonsama-moonsama-nft.gif")
    await ctx.channel.send(embed=embed)

bot.run(token)
