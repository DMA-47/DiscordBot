# -*- coding: utf8 -*-
# 1
import sys
import time

sys.path.insert(0, 'D:/DiscordToken')
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from config import settings
from func import *


bot = commands.Bot(command_prefix=settings['prefix'])
slash = SlashCommand(bot, sync_commands=True)
#slash = SlashCommand(bot)


@bot.command()
async def hello(ctx, name=''):
    msg, file = hello_msg(ctx, name)
    await ctx.send(msg, file=file)


@slash.slash(name='hello', description='Бот поприветствует вас')
async def hello_slash(ctx, name=''):
    msg, file = hello_msg(ctx, name)
    await ctx.send(msg, file=file)


@bot.command()
async def gimn(ctx):
    await ctx.send(f'https://youtu.be/qmj2m4UlEiE')


@slash.slash(name='gimn', description='Гимн республики')
async def gimn_slash(ctx):
    await ctx.send(f'https://youtu.be/qmj2m4UlEiE')


@bot.command()
async def dotastat(ctx, num_game=1):
    await ctx.send(dotastat_msg(ctx, num_game))


@slash.slash(name='dotastat', description='Статистика последних игр в доте',
             options=[
               create_option(
                 name="num_game",
                 description="Количество последних игр (не больше 15).",
                 option_type=4,
                 required=False
               )])
async def dotastat_slash(ctx, num_game=1):
    print(num_game)
    await ctx.send(dotastat_msg(ctx, num_game))


@bot.command()
async def chill(ctx):
    await ctx.send(chill_msg())


@slash.slash(name="chill", description="chill massage")
async def chill_slash(ctx):
    await ctx.send(chill_msg())


@bot.command()
async def anekdot(ctx, length='normal'):
    msg, ind = anekdot_msg(length)
    await ctx.send(msg, tts=ind)


@slash.slash(name="anekdot", description="Бот расскажет ахуенный анекдот",
             options=[
                 create_option(
                     name="length",
                     description="Розмер анекдота",
                     option_type=3,
                     required=False,
                     choices=[
                         create_choice(
                             name="Любой размер",
                             value="normal"
                         ),
                         create_choice(
                             name="Малый размер (зачитает вслух)",
                             value="small"
                         ),
                         create_choice(
                             name="Большой размер (нихуя не зачитает)",
                             value="big"
                         )
                     ]
                 )
             ])
async def anekdot_slash(ctx, length='normal'):
    print(length)
    msg, ind = anekdot_msg(length)
    await ctx.send(msg, tts=ind)


@bot.command()
async def points(ctx, metod=1, koef=-1):
    await ctx.send(points_msg(ctx, metod, koef))


@slash.slash(name="points", description="Рисунок из точек (работает только через \"+\")", options=[
               create_option(
                 name="metod",
                 description="Выбор метода (1 или 2)",
                 option_type=4,
                 required=False
               ), create_option(
                 name="koef",
                 description="Среднее значение пикселей (0..256)",
                 option_type=4,
                 required=False)])
async def points_slash(ctx, metod=1, koef=-1):
    await ctx.send(points_msg(ctx, metod, koef))


@bot.command()
async def weather(ctx, time1=''):
    msg, file = weather_msg(ctx, time1)
    await ctx.send(msg, file=file)


@slash.slash(name="weather", description="Информация про погоду с радара", options=[
               create_option(
                 name="time1",
                 description="Время в формате (ЧЧ:ММ) или \'info\' для получения легенды",
                 option_type=3,
                 required=False
               )])
async def weather_slash(ctx, time1=''):
    await ctx.defer()
    msg, file = weather_msg(ctx, time1)
    await ctx.send(msg, file=file)


bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
