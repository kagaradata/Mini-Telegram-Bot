import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    # adding buttons in bot
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("rundom number")
    item2 = types.KeyboardButton("how are you?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "welcome!", reply_markup=markup)

# skills
@bot.message_handler(content_types=['text'])
def lalala(message):
    
    if message.chat.type == 'private':
        if message.text == 'random number':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        
        elif message.text == 'how are you?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("good", callback_data='good')
            item2 = types.InlineKeyboardButton("not good", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'right! and you?', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'i dont know')


# possible answer to our message
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'right!)')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'dont worry..')

            # the disappearance of the buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.chat.id, text="how are you?",
                                  reply_markup=None)

            # trial notification
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="123")

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
