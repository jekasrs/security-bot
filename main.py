<<<<<<< HEAD
import telebot
import cv2
import moviepy.editor as mp

from telebot import types
from utils import is_detected

path = '/home/pi/project/'
=======
# import telebot
# import time
# import os
# from PIL import Image
#
# from telebot import types
#
# import cv2
#
# TOKEN = '5777109239:AAF1zwW2BkCF5pwFVDQNVj2grLJGGUrJqSc'
# URL = 'https://api.telegram.org/bot'
#
# bot = telebot.TeleBot(TOKEN)
# keyboard = types.InlineKeyboardMarkup()
#
#
# def make_video():
#     stream = cv2.VideoCapture(0)
#     fps = 15.0
#     frame_width = int(stream.get(3))
#     frame_height = int(stream.get(4))
#
#     size = (frame_width, frame_height)
#     video_file = 'res.avi'
#     if not stream.isOpened():
#         print("No stream")
#         exit()
#
#     result = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'MJPG'), fps, size)
#
#     i = 0
#     while (True):
#         ret, frame = stream.read()
#         # if not ret:
#         #     print("No more stream:(")
#         #     break
#         result.write(frame)
#         time.sleep(0.05)
#         i = i + 1
#         if i > 75:
#             break
#
#     stream.release()
#     result.release()
#     cv2.destroyAllWindows()
#
#     return '/Users/evgenijsmirnov/PycharmProjects/SecurityBot/res.avi'
#
#
# def start_security(id):
#     # if noticed:
#     path = make_video()
#     bot.send_message(id, 'Attantion! Enime: detected')
#     bot.send_video(id, open(path, 'rb'), None, 'Text')
#
#
# def make_GIF():
#     pass
#     # Список для хранения кадров.
#     # frames = []
#
#     # for frame_number in range(1, 5):
#     #    # Открываем изображение каждого кадра.
#     #    frame = Image.open(f'~/project/pictures-{frame_number}.jpg')
#     #    frame = frame.rotate(270)
#     #    # Добавляем кадр в список с кадрами.
#     #    frames.append(frame)
#
#     ## Берем первый кадр и в него добавляем оставшееся кадры.
#     # frames[0].save(
#     #    '/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.gif',
#     #    save_all=True,
#     #    append_images=frames[1:],  # Срез который игнорирует первый кадр.
#     #    optimize=True,
#     #    duration=100,
#     #    loop=0
#     # )
#
#     # clip = mp.VideoFileClip("/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.gif")
#     # clip.write_videofile("/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.mp4")
#
#
# @bot.message_handler(commands=['start', 'help'])
# def start(message):
#     start_message = 'Привет! Это бот, который позволит тебе следить за своим пространством! \n\n' + \
#                     'Команды:\n\n' + \
#                     '/take_picture - Сделать фото \n' + \
#                     '/start_tracking - Начать отслеживание\n'
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key_picture = types.KeyboardButton(text='Сделать фото')
#     key_tracking = types.KeyboardButton(text='Начать отслеживание')
#     markup.add(key_picture, key_tracking)
#     bot.send_message(message.chat.id, start_message,
#                      reply_markup=markup)  # третий аргумент - меняем клавиатуру на кнопочную
#
#
# @bot.message_handler(commands=['back'])
# def back(message):
#     back_message = 'Команды:\n\n' + \
#                    '/take_picture - Сделать фото \n' + \
#                    '/start_tracking - Начать отслеживание\n'
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key_picture = types.KeyboardButton(text='Сделать фото')
#     key_tracking = types.KeyboardButton(text='Начать отслеживание')
#     markup.add(key_picture, key_tracking)
#     bot.send_message(message.chat.id, back_message, reply_markup=markup)
#
#
# @bot.message_handler(commands=['take_picture'])
# def get_picture(message):
#     bot.send_message(message.chat.id, 'Вот ваше фото!')
#     bot.send_video(message.chat.id,
#                    open('/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.mp4', 'rb'), None, 'Text')
#     back(message)
#
#
# @bot.message_handler(commands=['start_tracking'])
# def start_tracking(message):
#     back_message = 'Слежка происходит'
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key_stop_tracking = types.KeyboardButton(text='Завершить слежку')
#     markup.add(key_stop_tracking)
#     bot.send_message(message.chat.id, back_message, reply_markup=markup)
#     start_security(message.chat.id)
#
#
# def stop_tracking(message):
#     answer = 'Отслеживание завершено!'
#     if message.text == 'Завершить обработку':
#         bot.send_message(message.chat.id, answer)
#         back(message)
#     else:
#         stop_tracking(message)
#
#
# @bot.message_handler(content_types=['text'])  # обработка текстового сообщения
# def random_answers(message):
#     if message.text == 'Сделать фото':
#         get_picture(message)
#     if message.text == 'Начать отслеживание':
#         start_tracking(message)
#     if message.text == 'Завершить слежку':
#         answer = 'Отслеживание завершено!'
#         bot.send_message(message.chat.id, answer)
#         back(message)
#
#
# bot.polling(none_stop=True, interval=0)
#
# # clip = mp.VideoFileClip("/home/pi/project/res1.avi")
#
# # clip.write_videofile("/home/pi/project/res.mp4")
#
# #     os.popen("ffmpeg -y -i 'res.avi' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 'res.mp4'".format(input = '/home/pi/project/res.avi', output = '/home/pi/project/res.mp4'))
#

import telebot
import time
import os
from PIL import Image
import numpy as np
from datetime import datetime

from telebot import types
import moviepy.editor as mp

import cv2

>>>>>>> bc2e26bf9ba36342f1f5e884fee18d6c8ca5cfb9
TOKEN = '5777109239:AAF1zwW2BkCF5pwFVDQNVj2grLJGGUrJqSc'
URL = 'https://api.telegram.org/bot'

bot = telebot.TeleBot(TOKEN)
keyboard = types.InlineKeyboardMarkup()

backSub = cv2.createBackgroundSubtractorMOG2(50, 16, True)
stop_track = False
<<<<<<< HEAD
stream = None

print("1. Success: Telegram Bot запущен")


def start_security(id):
    global stop_track
    global stream
    stream = cv2.VideoCapture(0)

    if not stream.isOpened():
        print("ERROR: No stream")
        exit()
    print("Success: Камера захвачена")

    frame_width = int(stream.get(3))
    frame_height = int(stream.get(4))
    size = (frame_width, frame_height)
    video_file = 'res.avi'
=======

def make_video():
    stream = cv2.VideoCapture(0)
    fps = 15.0
    frame_width = int(stream.get(3))
    frame_height = int(stream.get(4))

    size = (frame_width, frame_height)
    video_file = 'res.avi'
    if not stream.isOpened():
        print("No stream")
        exit()

    result = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'MJPG'), fps, size)

    i = 0
    while (True):
        ret, frame = stream.read()
        # if not ret:
        #     print("No more stream:(")
        #     break
        result.write(frame)
        time.sleep(0.05)
        i = i + 1
        if i > 75:
            break

    stream.release()
    result.release()
    cv2.destroyAllWindows()

    clip = mp.VideoFileClip("/Users/evgenijsmirnov/PycharmProjects/SecurityBot/res.avi")
    clip.write_videofile("/Users/evgenijsmirnov/PycharmProjects/SecurityBot/res.mp4")

    return '/Users/evgenijsmirnov/PycharmProjects/SecurityBot/res.mp4'


def start_security(id):
    global stop_track
    stream = cv2.VideoCapture(0)
    frame_width = int(stream.get(3))
    frame_height = int(stream.get(4))
>>>>>>> bc2e26bf9ba36342f1f5e884fee18d6c8ca5cfb9
    stream.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    stream.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    stop_track = True

    while stop_track:
<<<<<<< HEAD
        _, frame = stream.read()
        if is_detected(frame):
            fps = 15.0
            result = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'MJPG'), fps, size)
            i = 0
            while True:
                ret, frame = stream.read()
                result.write(frame)
                i = i + 1
                if i > 74:
                    break

            result.release()
            clip = mp.VideoFileClip(path + 'res.avi')
            clip.write_videofile(path + 'res.mp4')
            bot.send_video(id, open(path + 'res.mp4', 'rb'), None, 'Text')

    stream.release()

=======

        # шаг 1: получить изображение
        _, frame = stream.read()

        # шаг 2: вычитание фона
        fg_mask = backSub.apply(frame)

        # шаг 3: бинаризация маски
        _, mask_thr = cv2.threshold(fg_mask, 100, 255, 0)  # с тенями

        # шаг 4: исключение мелкого шума
        kernel_open = np.ones((5, 5), np.uint8)
        mask_open = cv2.morphologyEx(mask_thr, cv2.MORPH_OPEN, kernel_open)

        # шаг 5: исключение мелких областей
        kernel_close = np.ones((9, 9), np.uint8)
        mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel_close)

        # шаг 6: поиск контуров
        contours, _ = cv2.findContours(mask_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # шаг 7: исключение контуров малой площади
        area_threshold = 100
        contours_sel = [cnt for cnt in contours if cv2.contourArea(cnt) > area_threshold]

        # шаг 8: расчет площади контуров
        total_area = 0
        for cnt in contours_sel:
            total_area += cv2.contourArea(cnt)
        rel_area = total_area / (frame.shape[0] * frame.shape[1]) * 100

        # шаг 9: проверка движения в кадре
        motion_threshold = 0.5

        if rel_area > motion_threshold:
            # cv2.destroyAllWindows()
            # stream.release()
            path = make_video()
            bot.send_message(id, 'Attantion! Enime: detected')
            bot.send_video(id, open(path, 'rb'), None, 'Text')
>>>>>>> bc2e26bf9ba36342f1f5e884fee18d6c8ca5cfb9

@bot.message_handler(commands=['start', 'help'])
def start(message):
    start_message = 'Привет! Это бот, который позволит тебе следить за своим пространством! \n\n' + \
                    'Команды:\n\n' + \
                    '/take_picture - Сделать фото \n' + \
                    '/start_tracking - Начать отслеживание\n'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_picture = types.KeyboardButton(text='Сделать фото')
    key_tracking = types.KeyboardButton(text='Начать отслеживание')
    markup.add(key_picture, key_tracking)
    bot.send_message(message.chat.id, start_message,
                     reply_markup=markup)  # третий аргумент - меняем клавиатуру на кнопочную


@bot.message_handler(commands=['back'])
def back(message):
    back_message = 'Команды:\n\n' + \
                   '/take_picture - Сделать фото \n' + \
                   '/start_tracking - Начать отслеживание\n'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_picture = types.KeyboardButton(text='Сделать фото')
    key_tracking = types.KeyboardButton(text='Начать отслеживание')
    markup.add(key_picture, key_tracking)
    bot.send_message(message.chat.id, back_message, reply_markup=markup)


@bot.message_handler(commands=['take_picture'])
def get_picture(message):
    bot.send_message(message.chat.id, 'Вот ваше фото!')
<<<<<<< HEAD
    global stream
    stream = cv2.VideoCapture(0)
    if not stream.isOpened():
        print("No stream")
        exit()
    frame_width = int(stream.get(3))
    frame_height = int(stream.get(4))
    stream.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    stream.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    res, pic = stream.read()
    stream.release()
    cv2.imwrite(path + 'photo.png', pic)
    bot.send_photo(message.chat.id, open(path + 'photo.png', 'rb'))
=======
    bot.send_video(message.chat.id,
                   open('/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.mp4', 'rb'), None, 'Text')
>>>>>>> bc2e26bf9ba36342f1f5e884fee18d6c8ca5cfb9
    back(message)


@bot.message_handler(commands=['start_tracking'])
def start_tracking(message):
    back_message = 'Слежка происходит'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_stop_tracking = types.KeyboardButton(text='Завершить слежку')
    markup.add(key_stop_tracking)
    bot.send_message(message.chat.id, back_message, reply_markup=markup)
    start_security(message.chat.id)


def stop_tracking(message):
    answer = 'Отслеживание завершено!'
    if message.text == 'Завершить обработку':
        bot.send_message(message.chat.id, answer)
        back(message)
    else:
        stop_tracking(message)


@bot.message_handler(content_types=['text'])  # обработка текстового сообщения
def random_answers(message):
    global stop_track
    if message.text == 'Сделать фото':
        get_picture(message)
    if message.text == 'Начать отслеживание':
        start_tracking(message)
    if message.text == 'Завершить слежку':
        stop_track = False
        answer = 'Отслеживание завершено!'
        bot.send_message(message.chat.id, answer)
        back(message)


bot.polling(none_stop=True, interval=0)
<<<<<<< HEAD
=======

# clip = mp.VideoFileClip("/home/pi/project/res1.avi")

# clip.write_videofile("/home/pi/project/res.mp4")

#     os.popen("ffmpeg -y -i 'res.avi' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 'res.mp4'".format(input = '/home/pi/project/res.avi', output = '/home/pi/project/res.mp4'))
>>>>>>> bc2e26bf9ba36342f1f5e884fee18d6c8ca5cfb9
