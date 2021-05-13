import telebot
import TOKEN
import random, glob
 
from telebot import types
 
bot = telebot.TeleBot(TOKEN.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/AnimatedSticker.tgs', 'rb')
    print('REGISTR_USER | ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Архитектура")
    item2 = types.KeyboardButton("Пейзажи")
    item3 = types.KeyboardButton("Еда")
    item4 = types.KeyboardButton("Животные")
    item5 = types.KeyboardButton("Люди")
    item6 = types.KeyboardButton("Природа")
    item7 = types.KeyboardButton("Спорт")
    item8 = types.KeyboardButton("Автомобили")

 
    markup.add(item1,item2,item3,item4,item5,item6,item7,item8)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы показывать чудесные фотографии.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id,"Какую вы хотите фотографию?")
        
 
@bot.message_handler(content_types=['text'])
def start(message):
    if message.chat.type == 'private':
        if message.text == 'Архитектура':
            bot.send_message(message.chat.id, 'Отправляю фотографию...')
            files = glob.glob('photo/item1/*.jpg')
            with open(random.choice(files), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
                print('Photo: ', photo , '|  User: ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))

        if message.text == 'Пейзажи':   
            bot.send_message(message.chat.id, 'Отправляю фотографию...')
            files = glob.glob('photo/item2/*.jpg')
            with open(random.choice(files), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
                print('Photo: ', photo , '|  User: ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))
        
        if message.text == 'Еда':   
            bot.send_message(message.chat.id, 'Отправляю фотографию...')
            files = glob.glob('photo/item3/*.jpg')
            with open(random.choice(files), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
                print('Photo: ', photo , '|  User: ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))
        
        if message.text == 'Животные':   
            bot.send_message(message.chat.id, 'Отправляю фотографию...')
            files = glob.glob('photo/item4/*.jpg')
            with open(random.choice(files), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
                print('Photo: ', photo , '|  User: ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))
        
        if message.text == 'Люди':   
            bot.send_message(message.chat.id, 'Отправляю фотографию...')
            files = glob.glob('photo/item5/*.jpg')
            with open(random.choice(files), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
                print('Photo: ', photo , '|  User: ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))

        if message.text == 'Природа':   
            bot.send_message(message.chat.id, 'Отправляю фотографию...')
            files = glob.glob('photo/item6/*.jpg')
            with open(random.choice(files), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
                print('Photo: ', photo , '|  User: ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))

        if message.text == 'Спорт':   
            bot.send_message(message.chat.id, 'Отправляю фотографию...')
            files = glob.glob('photo/item7/*.jpg')
            with open(random.choice(files), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
                print('Photo: ', photo , '|  User: ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))

        if message.text == 'Автомобили':   
            bot.send_message(message.chat.id, 'Отправляю фотографию...')
            files = glob.glob('photo/item8/*.jpg')
            with open(random.choice(files), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
                print('Photo: ', photo , '|  User: ', message.chat.id, " |  {0.first_name}".format(message.from_user, bot.get_me()))

    else:
        	bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
    	

# RUN
bot.polling(none_stop=True)