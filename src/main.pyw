# -*- coding: utf8 -*-
#1
import discord
from discord.ext import commands, tasks
from config import settings
import asyncio
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from urllib.request import urlopen
from PIL import Image



id_list = {'maxl1245#8177': '218495855',
          'DarkSoules#8541': '290164262',
          'AskoldoFFF#6716': '387772909'}

list2 = {'Іван Мазепа#8567': 'Руся лох'}

chill_list = ['Ты чего такой злой :rage: :rage: братишка?\nЗабомби дарксайдика поплотнее :smirk: :dash: для\nуспокоения :relaxed: :relaxed: накумарит так, что\nкайфанешь :drooling_face: :drooling_face: сразу подобреешь :innocent: :innocent: \nпроверено) :grinning: :point_up_2:',
              'Братулец, не злись :smiling_imp: лучше пыхни\nколяндуполы :dash: и плохое настроение как\nрукой :thumbsup: снимет на хороший покур и \nсолнце  :sun_with_face: ярче и небо :milky_way: яснее  :stuck_out_tongue_winking_eye: дыши \nполной жизню, живи яркой грудью :face_with_monocle:',
              'Братка :point_up:, че за агресия(agression):disappointed:\nпопыхти :wind_blowing_face: калумбаху два яблочка :apple: :green_apple: и \nрасслабся :smiling_imp: :kissing_heart: \nДым твоему дому  :house: брат'] 


bot = commands.Bot(command_prefix = settings['prefix']) # Так как мы указали префикс в settings, обращаемся к словарю с ключом prefix.

@bot.command() 
async def s(ctx, *args):  
    await ctx.send('https://cdn.discordapp.com/attachments/791596556297830422/799677669363941407/unknown.png')
    min_profit = 100 if len(args) == 0 else int(args[0])
    print(min_profit)
    num_page = 3
    num_stonks = 0
    msg = '---------------------------------------'
    for page in range(1, num_page + 1):
            html = requests.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=1068&ItemNamePattern=Камень+душ&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=&page=" + str(page) + "&SortBy=LastSeen&Order=desc&lang=ru-RU", headers = {'User-agent': 'your bot 0.1'}).text
            soup = BeautifulSoup(html, 'html5lib')
            sell_list = soup('tr', 'cursor-pointer')
            for i in range(10):
                if num_stonks >= 8:
                    break
                    
                id_now = int(sell_list[i].get('data-on-click-link').split('/')[-1])
                loc = sell_list[i]('td', 'hidden-xs')[1]('div')[0].text.strip() if len(sell_list[i]('td', 'hidden-xs')[1]('div')) > 0 else 'None'
                guild = sell_list[i]('td', 'hidden-xs')[1]('div')[1].text.strip() if len(sell_list[i]('td', 'hidden-xs')[1]('div')) > 0 else 'None'
                price_one = float(str(sell_list[i]('td', 'gold-amount bold')[0]).split()[6].replace(',', ''))
                num_goods = int(str(sell_list[i]('td', 'gold-amount bold')[0]).split()[14])
                all_price = str(sell_list[i]('td', 'gold-amount bold')[0]).split()[22]
                last_time = int(sell_list[i]('td', 'bold hidden-xs')[0].get('data-mins-elapsed'))

                profit =  (30 * num_goods) - (price_one * num_goods)
                if profit >= min_profit:
                    num_stonks += 1
                    msg += '\nЛокация:   ' + loc
                    msg += '\nГильдия:   ' + guild
                    msg += '\nЗа 1:   ' + str(price_one) + 'g'
                    msg += '\nШтук:   ' + str(num_goods)
                    msg += '\nВсего:   ' + str(all_price) + '(' + str(price_one * num_goods) + ') g'
                    msg += '\nПрибыль:   ' + str(profit) + 'g'
                    msg += '\nКогда замечено:   ' + str(last_time) + 'мин. назад'
                    msg += '\n---------------------------------------'
            if num_stonks >= 8:
                break
    print(msg if msg != '---------------------------------------' else 'None')
    await ctx.send(msg if msg != '---------------------------------------' else 'https://tenor.com/view/not-stonks-profit-down-sad-frown-arms-crossed-gif-15684535')


@bot.command() 
async def hello(ctx):
    author = ctx.message.author
    if str(author) == 'Іван Мазепа#8567':
        await ctx.send('Руся лох')
    elif str(author) == 'DarkSoules#8541':
        await ctx.send('Добрый день господин!')
        await ctx.send('https://tenor.com/view/youre-welcome-pleasure-keanu-reeves-its-a-pleasure-thank-you-gif-18395277')
    elif str(author) == 'Хомячок💀Backstab💀#0110':
        await ctx.send('Доров ВИТЮША')
    else:
        await ctx.send(f'Пошел нахуй , {author.mention}!')
    

@bot.command() 
async def putin(ctx):
    await ctx.send(f'⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⡀\n⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⡇⠄⠄⠄⠄⠄ ')


@bot.command() 
async def gimn(ctx):
    await ctx.send(f'https://youtu.be/qmj2m4UlEiE')
    

@bot.command() 
async def dotastat(ctx, *args):
    author = ctx.message.author
    num = 1 
    if len(args) > 0:
        if int(args[0]) > 15:
            await ctx.send('Пошел нахуй ' + author.mention + ', макимум 15 матчей.')
            num = 15
        else:
            num = int(args[0])
        
    id = id_list[str(author)]
    print(id_list[str(author)])
    
    html = requests.get("https://ru.dotabuff.com/players/" + id + "/matches?enhance=overview&page=1", headers = {'User-agent': 'your bot 0.1'}).text
    soup = BeautifulSoup(html, 'html5lib')
    games = soup('div', 'content-inner')[0]('section')[2]('tbody')[0]('tr')
    table = [['Герой', 'Результат','Тип','Длительность','УСП','Дата']]
    for i in range(num):
        line = []
        line.append('{}'.format(games[i].find('td', 'cell-large').a.text))
        line.append('{}'.format(games[i].find_all('td')[3].a.text))
        type2 = games[i].find_all('td', 'r-none-mobile')[1].find('div', 'subtext').text
        line.append('{}'.format(games[i].find_all('td', 'r-none-mobile')[1].text[:-len(type2)] + ': ' + type2))
        line.append('{}'.format(games[i].find_all('td')[5].text))
        line.append('{}'.format(games[i].find_all('td')[6].text))
        line.append('{}'.format(games[i].find_all('td')[3].time.get('title')[:-6]))
        table.append(line)
    print(f'{tabulate(table)}')
    await ctx.send(f'`{tabulate(table)}`')


@bot.command() 
async def chill(ctx):
    random.seed()
    await ctx.send(random.choice(chill_list))


@bot.command() 
async def anekdot(ctx, *args):  
    html = requests.get("https://baneks.site/random", headers = {'User-agent': 'your bot 0.1'}).text
    soup = BeautifulSoup(html, 'html5lib')
    split_1 = str(soup('section')[0]).split('<')[2:-2]
    split_2 = [i.split('>')[1] for i in split_1]
    msg = ''
    for line in split_2:
        msg += line + '\n'
    print(msg)
    await ctx.send(msg)


@bot.command() 
async def points(ctx, *args):
    def resize_image(input_image_path, output_image_path):
        n = 120
        size = [n, n]
        original_image = Image.open(input_image_path)
        width, height = original_image.size
        print('The original image size is {wide} wide x {height} high'.format(wide=width, height=height))
        
        if width > height:
            size[1] = int(height * n / width)
        else:
            size[0] = int(width * n / height)
            
        resized_image = original_image.resize(size)
        width, height = resized_image.size
        print('The resized image size is {wide} wide x {height} high'.format(wide=width, height=height))
        resized_image.save(output_image_path)
        
    url = ctx.message.attachments[0].url
    print(url)
    # downolad img
    braile = '⠁⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿'


    p = requests.get(url)
    out = open('D:\\DiscordBot\\png\\img.png', "wb")
    out.write(p.content)
    out.close()

    im = Image.open('D:\\DiscordBot\\png\\img.png')
    rgb_im = im.convert('RGB')
    rgb_im.save('D:\\DiscordBot\\png\\img.jpg')

    resize_image('D:\\DiscordBot\\png\\img.jpg', 'D:\\DiscordBot\\png\\img.jpg')

    with cbook.get_sample_data('D:\\DiscordBot\\png\\img.jpg') as image_file:
        image = plt.imread(image_file)
    
    # black or white
    lst = []
    koef = image.mean()
    if len(args) > 0:
        koef = int(args[0])
        
    for i in range(len(image)):
        lst.append([])
        for j in range(len(image[i])):
            mean = np.mean(image[i][j])
            if mean > koef:
                lst[i].append(0)
            else:
                lst[i].append(1)

    lst = np.array(lst)
    lst = lst[0:len(lst)-(len(lst)%4)]
    lst = lst[:, 0:len(lst[0])-(len(lst[0])%2)]
    print(lst)
    # create msg
    msg = ''

    for i in range(0, len(lst), 4):
        for j in range(0, len(lst[i]), 2):
            d_arr = []
            num = 0
            d_arr.append(lst[i, j])
            d_arr.append(lst[i + 1, j])
            d_arr.append(lst[i + 2, j])
            d_arr.append(lst[i, j + 1])
            d_arr.append(lst[i + 1, j + 1])
            d_arr.append(lst[i + 2, j + 1])
            d_arr.append(lst[i + 3, j])
            d_arr.append(lst[i + 3, j + 1])
            
            for d in range(8):
                num += d_arr[d] * 2**d
                
            msg += braile[num]
        msg += '\n'
    print(msg)
    await ctx.send(msg)
    
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена

