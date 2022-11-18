import telebot
from PIL import Image

from TelegramBotAPI import types
from telebot import types
import moviepy.editor as mp

TOKEN = '5777109239:AAF1zwW2BkCF5pwFVDQNVj2grLJGGUrJqSc'
URL = 'https://api.telegram.org/bot'

bot = telebot.TeleBot(TOKEN)
keyboard = types.InlineKeyboardMarkup()

def make_GIF():
    # Список для хранения кадров.
    frames = []

    for frame_number in range(1, 5):
        # Открываем изображение каждого кадра.
        frame = Image.open(f'/Users/evgenijsmirnov/PycharmProjects/SecurityBot/pictures/picture-{frame_number}.jpg')
        frame = frame.rotate(270)
        # Добавляем кадр в список с кадрами.
        frames.append(frame)

    # Берем первый кадр и в него добавляем оставшееся кадры.
    frames[0].save(
        '/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.gif',
        save_all=True,
        append_images=frames[1:],  # Срез который игнорирует первый кадр.
        optimize=True,
        duration=100,
        loop=0
    )

    clip = mp.VideoFileClip("/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.gif")
    clip.write_videofile("/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.mp4")

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
    bot.send_message(message.chat.id, start_message, reply_markup=markup)  # третий аргумент - меняем клавиатуру на кнопочную

@bot.message_handler(commands=['back'])
def back(message):
    back_message =  'Команды:\n\n' + \
                    '/take_picture - Сделать фото \n' + \
                    '/start_tracking - Начать отслеживание\n'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_picture = types.KeyboardButton(text='Сделать фото')
    key_tracking = types.KeyboardButton(text='Начать отслеживание')
    markup.add(key_picture, key_tracking)
    bot.send_message(message.chat.id, back_message, reply_markup=markup)

@bot.message_handler(commands=['take_picture'])
def get_picture(message):
    make_GIF()
    bot.send_message(message.chat.id, 'Вот ваше фото!')
    bot.send_video(message.chat.id, open('/Users/evgenijsmirnov/PycharmProjects/SecurityBot/result-gifs/home.mp4', 'rb'), None, 'Text')
    back(message)
    #вывод фотки
    #bot.register_next_step_handler(message, get_title_of_stock)

@bot.message_handler(commands=['start_tracking'])
def start_tracking(message):
    back_message = 'Слежка происходит'
    # bot.send_message(message.chat.id, 'Слежка происходит!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_stop_tracking = types.KeyboardButton(text='Завершить слежку')
    markup.add(key_stop_tracking)
    bot.send_message(message.chat.id, back_message, reply_markup=markup)
    # bot.register_next_step_handler(message, stop_tracking)

def stop_tracking(message):
    answer = 'Отслеживание завершено!'
    if message.text == 'Завершить обработку':
        bot.send_message(message.chat.id, answer)
        back(message)
    else:
        stop_tracking(message)

@bot.message_handler(content_types=['text']) #обработка текстового сообщения
def random_answers(message):
    if message.text == 'Сделать фото':
        get_picture(message)
    if message.text == 'Начать отслеживание':
        start_tracking(message)
    if message.text == 'Завершить слежку':
        answer = 'Отслеживание завершено!'
        bot.send_message(message.chat.id, answer)
        back(message)


bot.polling(none_stop=True, interval=0)