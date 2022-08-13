import discord
import os
from dotenv import load_dotenv

from IntegrationTut import Integral

load_dotenv()
client = discord.Client()

TOKEN = os.getenv("DISCORD_TOKEN"
                  ""
                  "")


@client.event
async def on_ready():
    print("{0.user} has logged in.".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!integrate'):

        oritoIntegrate = message.content[10:]
        toIntegrate = oritoIntegrate.replace("-", "+-")
        toIntegrate = toIntegrate.replace(" ", "")
        print(toIntegrate)

        integral = Integral(polynomial=toIntegrate, a=0, b=5, N=5000)
        solution = ("The integral " + oritoIntegrate + " evaluates to " + "%.4f" % integral.integratePolynomial())
        embed = discord.Embed(title='Solution',
                              description=solution, color=0xFF5733)

        await message.channel.send(embed=embed)


client.run(TOKEN)
