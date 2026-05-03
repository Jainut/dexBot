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

@bot.command()
async def uai(ctx:commands.Context, *, texto=""):
    if texto == "":
        numsRandom = random.randint(0, 9)

        if numsRandom == 0:
            await ctx.reply("Trem, sô")
        elif numsRandom == 1:
            await ctx.reply("BH é nós sô")
        elif numsRandom == 2:
            await ctx.reply("Nói num para não, nói só da um tempin")
        elif numsRandom == 3:
            await ctx.reply("Num viaja ni min não")
        elif numsRandom == 4:
            await ctx.reply("Cê vai tomar é na desnara sô")
        elif numsRandom == 5:
            await ctx.reply("Cola aqui pra nós toma um cafézin sô")
        elif numsRandom == 6:
            await ctx.reply("Ainda estou aqui")
        elif numsRandom == 7:
            await ctx.reply("Cê é fi de quem?")
        elif numsRandom == 8:
            await ctx.reply("Que que cê tá pegano viaji ni mim, sô?")
        elif numsRandom == 9:
            await ctx.reply("Que que pega, zé?")

    elif "desgraça" in texto or "desgraca" in texto or "Desgraça" in texto or "Desgraca" in texto:
        numsRandom = random.randint(0, 3)

        if numsRandom == 0:
            await ctx.reply("Ó o cara rasgando o nome mano")
        elif numsRandom == 1:
            await ctx.reply("Não rasga o nome da pelada não, sô")
        elif numsRandom == 2:
            await ctx.reply("Para de rasgá o nome, sô, ó")
        elif numsRandom == 3:
            await ctx.reply("Se ocê rasgá o nome de novo cê vai vê zé")
    
    elif ctx.message.mentions:
        user = ctx.message.mentions[0]
        await ctx.send(f"o {user.mention} é pagão")

    else:
        await ctx.reply(f"{texto} é coisa do demônio")


@bot.command() # comando abraço, que tem 50% de chance de responder "Ixi mano sai fora mano" ou "Ué, abraço"
async def abraço(ctx:commands.Context):
    zeroum = random.randint(0, 1)

    if zeroum == 0:
        await ctx.reply("Ixi mano sai fora mano")
    else:
        await ctx.reply("Ué, abraço")

@bot.command() # mostrar o tamanho da pingola
async def empatia(ctx:commands.Context):
    tamanho = random.randint(0, 101) # randomizando o tamanho e tals

    if (ctx.message.mentions): # se mencionar outra pessoa da o tamanho da pingola dela, se nao mencionar ninguem da o tamanho da pingola do proprio usuario
        user = ctx.message.mentions[0]

        if (tamanho <= 65):
            await ctx.reply(f"O {user.mention} é uma pessoa maléfica e que definitivamente não se importa com as outras pessoas, parabéns")
        else:
            await ctx.reply(f"O {user.mention} tem {tamanho}% de amor pelas pessoas, parabéns por ser empático e gentil") 
    else:
        user = ctx.author.mention

        if (tamanho <= 65):
            await ctx.reply(f"Você é uma pessoa maléfica e que definitivamente não se importa com as outras pessoas, parabéns")
        else:
            await ctx.reply(f"Você tem {tamanho}% de amor pelas pessoas, parabéns por ser empático e gentil") 

@bot.command() # Comando pra repetir o que o usuario mandar e tals
async def ping(ctx:commands.Context):
    await ctx.reply("Oi, tô aqui")

bot.run(TOKEN) # Rodando essa bomba... 🔥🔥🔥