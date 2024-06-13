'''import telebot
token='6507243138:AAEcPW7gIi4YLrpDdXsOQBrAlBBrVfj51r4'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет! ✌")
bot.infinity_poling()'''
import markup as markup
import telebot
from telebot import types
bot = telebot.TeleBot("6507243138:AAEcPW7gIi4YLrpDdXsOQBrAlBBrVfj51r4")

@bot.message_handler(content_types=['text'])
def sending(message):
    '''

    :param message:
    :return:
    '''
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Хочу учиться IT сфере", callback_data = 'item_1')
    button2 = types.InlineKeyboardButton("Хочу учиться Soft Skills сфере", callback_data = 'item_2')
    button3 = types.InlineKeyboardButton("Хочу учиться Проектной сфере", callback_data = 'item_3')
    button4 = types.InlineKeyboardButton("Хочу больше полезного контента", url='https://vk.com/procyonsocproject')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    bot.send_message(message.chat.id,
                     "Привет ✌, {0.first_name}! Выбери свою сферу обучения в Проционе".format(message.from_user),
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    markup1 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Язык программирования C# для начинающих",
                                         url='https://stepik.org/99426')
    button2 = types.InlineKeyboardButton("Adobe Illustrator: основы векторной графики",
                                         url='https://stepik.org/101857')
    button3 = types.InlineKeyboardButton("Геоинформатика: основы разработки геоинформационных технологий",
                                         url='https://stepik.org/100741')
    markup1.add(button1)
    markup1.add(button2)
    markup1.add(button3)

    markup2 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Soft skills: незаменимые жизненные навыки",
                                         url='https://stepik.org/105225')
    markup2.add(button1)

    markup3 = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Стартап с 0: Основы проектной деятельности",
                                         url='https://stepik.org/172021')
    markup3.add(button1)

    if call.message:
            if call.data == "item_1":
                bot.send_message(call.message.chat.id, "Для обучения доступны следующие онлайн-курсы:",reply_markup=markup1)
            elif call.data == "item_2":
                bot.send_message(call.message.chat.id, "Для обучения доступны следующие онлайн-курсы:",reply_markup=markup2)
            elif call.data == "item_3":
                bot.send_message(call.message.chat.id, "Для обучения доступны следующие онлайн-курсы:",reply_markup=markup3)



# RUN
bot.polling(non_stop=True)



