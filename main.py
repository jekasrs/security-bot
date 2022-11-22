import telebot
import cv2
import moviepy.editor as mp

from telebot import types
from utils import is_detected

path = '/home/pi/project/'
TOKEN = '5777109239:AAF1zwW2BkCF5pwFVDQNVj2grLJGGUrJqSc'
URL = 'https://api.telegram.org/bot'

bot = telebot.TeleBot(TOKEN)
keyboard = types.InlineKeyboardMarkup()

backSub = cv2.createBackgroundSubtractorMOG2(50, 16, True)
stop_track = False
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
    stream.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    stream.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    stop_track = True

    while stop_track:
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
