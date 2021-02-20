import telebot
import time
bot = telebot.TeleBot('1558655939:AAEjqzITJd0A-WVyF2HammsZZRtO66LHaqg')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Дохід', 'Розхід', "Борги", "Коментарі")


@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, я сподіваюсь, що ти не витрачаєш кошти даремно)\n\
Що у нас сьогодні?', reply_markup=keyboard1)



bot.polling()