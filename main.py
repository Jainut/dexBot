import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os # importando as biblioteca e pa

load_dotenv()
TOKEN = os.getenv("TOKEN") # puxando o token do .env e pa

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents) # pré definicao padrao do bot e tals

@bot.event # quando o bot estiver pronto, ele vai printar isso no terminal
async def on_ready():
    print("Essa bomba de bot ta rodando")

@bot.command() # comando chupa, que tem 50% de chance de responder "Ixi mano sai fora mano" ou "Ué, chupo"
async def chupa(ctx:commands.Context):
    zeroum = random.randint(0, 1)

    if zeroum == 0:
        await ctx.reply("Ixi mano sai fora mano")
    else:
        await ctx.reply("Ué, chupo")

@bot.command() # mostrar o tamanho da pingola
async def pingola(ctx:commands.Context):
    tamanho = random.randint(5, 35) # randomizando o tamanho e tals

    if (ctx.message.mentions): # se mencionar outra pessoa da o tamanho da pingola dela, se nao mencionar ninguem da o tamanho da pingola do proprio usuario
        user = ctx.message.mentions[0]

        if (tamanho <= 15):
            await ctx.reply(f"O {user.mention} tem clitoris, parabéns")
        else:
            await ctx.reply(f"O tamanho da pingola do {user.mention} é {tamanho}cm") 
    else:
        user = ctx.author.mention

        if (tamanho <= 15):
            await ctx.reply("Você tem clitoris, parabéns")
        else:
            await ctx.reply(f"O tamanho da sua pingola é {tamanho}cm") 

@bot.command() # Comando pra repetir o que o usuario mandar e tals
async def ping(ctx:commands.Context, *, texto=""):
    if (texto == ""):
        await ctx.send("Tem que escrever algo depois do comando bixo fei")
    else:
        await ctx.send(f"O que é {texto}?")

bot.run(TOKEN) # Rodando essa bomba... 🔥🔥🔥