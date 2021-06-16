import discord
import random
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from PIL import Image
from datetime import datetime as dt
from datetime import timedelta as td
import imageio

chill_list = [
    'Ты чего такой злой :rage: :rage: братишка?\nЗабомби дарксайдика поплотнее :smirk: :dash: для\nуспокоения :relaxed: :relaxed: накумарит так, что\nкайфанешь :drooling_face: :drooling_face: сразу подобреешь :innocent: :innocent: \nпроверено) :grinning: :point_up_2:',
    'Братулец, не злись :smiling_imp: лучше пыхни\nколяндуполы :dash: и плохое настроение как\nрукой :thumbsup: снимет на хороший покур и \nсолнце  :sun_with_face: ярче и небо :milky_way: яснее  :stuck_out_tongue_winking_eye: дыши \nполной жизню, живи яркой грудью :face_with_monocle:',
    'Братка :point_up:, че за агресия(agression):disappointed:\nпопыхти :wind_blowing_face: калумбаху два яблочка :apple: :green_apple: и \nрасслабся :smiling_imp: :kissing_heart: \nДым твоему дому  :house: брат']

id_list = {'maxl1245#8177': '218495855',
           'DarkSoules#8541': '290164262',
           'AskoldoFFF#6716': '387772909'}


def chill_msg():
    random.seed()
    return random.choice(chill_list)


def hello_msg(ctx):
    author = ctx.author
    if str(author) == 'Іван Мазепа#8567':
        return 'Руся лох'
    elif str(author) == 'DarkSoules#8541':
        return 'Добрый день господин!\nhttps://tenor.com/view/youre-welcome-pleasure-keanu-reeves-its-a-pleasure-thank-you-gif-18395277'
    elif str(author) == 'Хомячок💀Backstab💀#0110':
        return 'Доров ВИТЮША'
    else:
        return f'Пошел нахуй , {author.mention}!'


def dotastat_msg(ctx, num_game):
    author = ctx.author
    if num_game > 15:
        return 'Пошел нахуй ' + author.mention + ', макимум 15 матчей.'
        num = 15
    else:
        num = num_game

    id = id_list[str(author)]
    print(id_list[str(author)])

    html = requests.get("https://ru.dotabuff.com/players/" + id + "/matches?enhance=overview&page=1",
                        headers={'User-agent': 'your bot 0.1'}).text
    soup = BeautifulSoup(html, 'html5lib')
    games = soup('div', 'content-inner')[0]('section')[2]('tbody')[0]('tr')
    table = [['Герой', 'Результат', 'Тип', 'Длительность', 'УСП', 'Дата']]
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
    return f'`{tabulate(table)}`'


def anekdot_msg(length):
    max_len = 199

    while True:
        msg = ''
        html = requests.get("https://baneks.site/random", headers={'User-agent': 'your bot 0.1'}).text
        soup = BeautifulSoup(html, 'html5lib')
        split_1 = str(soup('section')[0]).split('<')[2:-2]
        split_2 = [i.split('>')[1] for i in split_1]
        for line in split_2:
            msg += line + '\n'
        if length == 'normal' or (length == 'small' and len(msg) < max_len) or (length == 'big' and len(msg) > max_len):
            break

    print(msg)
    if len(msg) > max_len:
        ind_tts = False
    else:
        ind_tts = True
    return msg, ind_tts


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


def create_koefs(koef):
    maxk = 256
    res = np.zeros(4)
    num1 = koef / 2.5
    num2 = (maxk - koef) / 2.5

    res[0] = num1
    res[1] = num1 * 2
    res[2] = res[1] + (num1 / 2) + (num2 / 2)
    res[3] = res[2] + num2

    return res


def points_msg(ctx, metod, koef):
    url = ctx.message.attachments[0].url
    print(url)

    # downolad img
    braile = '⠁⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿'
    way = 'D:\\DiscordBot\\png\\img.'

    p = requests.get(url)
    out = open(way + 'png', "wb")
    out.write(p.content)
    out.close()

    im = Image.open(way + 'png')
    rgb_im = im.convert('RGB')
    rgb_im.save(way + 'jpg')

    resize_image(way + 'jpg', way + 'jpg')

    with cbook.get_sample_data(way + 'jpg') as image_file:
        image = plt.imread(image_file)

    image = image[0:len(image) - (len(image) % 4)]
    image = image[:, 0:len(image[0]) - (len(image[0]) % 2)]
    height, width = image.shape[0], image.shape[1]

    # black or white
    lst = []

    if koef < 0 or koef > 255:
        koef = image.mean()

    if metod == 1:
        koefs = create_koefs(koef)
        print(koefs)
        for i in range(0, height, 2):
            lst.append([])
            lst.append([])
            for j in range(0, width, 2):
                means = np.array([np.mean(image[i][j]), np.mean(image[i][j + 1]), np.mean(image[i + 1][j]),
                                  np.mean(image[i + 1][j + 1])])
                mean = np.mean(means)

                if mean < koefs[0]:  # 4
                    lst[i].append(1)
                    lst[i].append(1)
                    lst[i + 1].append(1)
                    lst[i + 1].append(1)
                elif mean < koefs[1]:  # 3
                    index = means.argmax()
                    lst[i].append(0 if index == 0 else 1)
                    lst[i].append(0 if index == 1 else 1)
                    lst[i + 1].append(0 if index == 2 else 1)
                    lst[i + 1].append(0 if index == 3 else 1)

                elif mean < koefs[2]:  # 2
                    index1 = means.argmax()
                    means[index1] = 0
                    index2 = means.argmax()
                    lst[i].append(0 if index1 == 0 or index2 == 0 else 1)
                    lst[i].append(0 if index1 == 1 or index2 == 1 else 1)
                    lst[i + 1].append(0 if index1 == 2 or index2 == 2 else 1)
                    lst[i + 1].append(0 if index1 == 3 or index2 == 3 else 1)

                elif mean < koefs[3]:  # 1
                    index = means.argmin()
                    lst[i].append(1 if index == 0 else 0)
                    lst[i].append(1 if index == 1 else 0)
                    lst[i + 1].append(1 if index == 2 else 0)
                    lst[i + 1].append(1 if index == 3 else 0)

                else:  # 0
                    lst[i].append(0)
                    lst[i].append(0)
                    lst[i + 1].append(0)
                    lst[i + 1].append(0)
    else:
        for i in range(height):
            lst.append([])
            for j in range(width):
                mean = np.mean(image[i][j])
                if mean > koef:
                    lst[i].append(0)
                else:
                    lst[i].append(1)

    lst = np.array(lst)

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
                num += d_arr[d] * 2 ** d

            msg += braile[num]
        msg += '\n'
    return msg


def get_time(time):
    hm = [int(i) for i in time.split(':')]
    return hm[0], hm[1]


def create_weather_gif(time, folder):
    msg = ''
    first_id = 0
    num_img = 17
    data2 = dt.today()

    html = requests.get("https://meteo.gov.ua/ua/33345/radar", headers={'User-agent': 'your bot 0.1'},
                        verify=False).text
    soup = BeautifulSoup(html, 'html5lib')
    data_range = [[line.get('value'), line.text] for line in soup('option')]

    if len(time) > 0:
        h1, m1 = get_time(time)
        d = 0
        if h1 > data2.hour:
            d = 1
        data2 -= td(days=d, hours=data2.hour, minutes=data2.minute) - td(hours=h1, minutes=m1) + td(hours=3)
        for i in range(len(data_range)):
            data_i = dt.strptime(data_range[i][0], '%Y-%m-%d %H-%M-%S')
            if data_i < data2:
                first_id = i
                break

    last_id = first_id + num_img
    # print(data2)
    msg += data_range[last_id][1] + ' - ' + data_range[first_id][1]

    images = []
    filename = 'D:\\DiscordBot\\png\\weather.png'
    for i in range(last_id, first_id, -1):
        data_i = data_range[i][0].split()
        url = 'https://meteo.gov.ua/radars/Ukr_J%20' + data_i[0] + '%20' + data_i[1] + '.jpg'
        # print(url)
        p = requests.get(url, verify=False)
        out = open(filename, "wb")
        out.write(p.content)
        out.close()

        for _ in range(1):
            images.append(imageio.imread(filename))

    imageio.mimsave(folder, images)
    return msg


def weather_msg(ctx, time):
    folder_gif = 'D:\\DiscordBot\\gifs\\weather.gif'
    folder_info = 'D:\\DiscordBot\\png\\weather_info.png'
    folder_shuiali = 'D:\\DiscordBot\\png\\weather_shuiali.png'
    print(time)
    if time == 'info':
        return 'Info:', discord.File(folder_info)
    elif time == 'схуяли.задержка.40.минут?':
        return 'Info:', discord.File(folder_shuiali)
    else:
        msg = create_weather_gif(time, folder_gif)
        return msg, discord.File(folder_gif)

