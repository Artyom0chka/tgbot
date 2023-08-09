import telebot
from telebot import types


bot = telebot.TeleBot('6379030655:AAFJ-mDOfa2hb_nsNCGE2dWla8AkKBiBQrA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Хей, мальчишка  *{message.from_user.first_name}*', parse_mode="Markdown")
    markup = types.InlineKeyboardMarkup()
    button01 = types.InlineKeyboardButton(text='ДА!', callback_data='delete')
    markup.add(button01)
    bot.reply_to(message.chat.id, 'Мальчишка', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(callback):
   if callback.data == 'delete':
       bot.send_message(callback.message.chat.id, 'Хочешь похвастаться сакцесом?',)

bot.polling(none_stop=True)
