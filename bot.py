import discord 
import random
import os
from discord.ext import commands 
from bot_logic import gen_pass 
from bot_logic import gen_nick 
 
intents = discord.Intents.default() 
intents.message_content = True 
 
bot = commands.Bot(command_prefix='$', intents=intents) 
 
@bot.event 

async def on_ready(): 
    print(f'We have logged in as {bot.user}') 
 
@bot.command()                        #      $hello 
async def hello(ctx): 
    await ctx.send(f'Привет! Я бот {bot.user}! Вот команды которые у меня есть: $hello - приветствие, $pasw - генерация пароля, $mem - мем, $ng - генерация ника, $rch - рандомайзер чисел от 1 до 100') 
 
@bot.command()                       #           $pasw 
async def pasw(ctx): 
    await ctx.send(gen_pass(10))
    
@bot.command()                      #               $mem
async def mem(ctx):
    files = os.listdir("images")
    with open('images/' + random.choice(files), 'rb') as f:
        pic = discord.File(f)
    await ctx.send(file=pic)

@bot.command()                      #                   rch
async def rch(ctx):
    num = random.randint(1,100)
    await ctx.send(num)
@bot.command()                       #                      $ng 
async def ng(ctx): 
    await ctx.send(gen_nick(8))


    
 
bot.run("")
