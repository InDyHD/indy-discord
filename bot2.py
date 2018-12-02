import discord
from discord.ext import commands

TOKEN = "NTE4NzQwOTkxODI2NTkxNzY0.DuVLRA.15L6qM3H00oACIcsZZ7xxJLanj4"

client = commands.Bot(command_prefix = "_")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="twitch.tv/indypt"))
    print('Logado em:')
    print(client.user.name)
    print(client.user.id)
    print('----------')
    print("Bot Ready!")

client.run(TOKEN)
