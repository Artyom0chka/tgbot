import telebot
from telebot import types


bot = telebot.TeleBot('6379030655:AAFJ-mDOfa2hb_nsNCGE2dWla8AkKBiBQrA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Хей, мальчишка  *{message.from_user.first_name}*', parse_mode="Markdown")
    markup01 = types.InlineKeyboardMarkup()
    button01 = types.InlineKeyboardButton(text='ДА!', callback_data='delete')
    markup01.add(button01)
    bot.send_message(message.chat.id, 'Хочешь похвастаться сакцесом?', reply_markup=markup01)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(callback):
   if callback.data == 'delete':
       markup02 = types.InlineKeyboardMarkup()
       button02 = types.InlineKeyboardButton(text='Ретродроп', callback_data='retro')
       button03 = types.InlineKeyboardButton(text='Сладкий флип', callback_data='flip')
       markup02.add(button02,button03)
       bot.send_message(callback.message.chat.id, 'Каким именно?', reply_markup=markup02)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(callback1):
    if callback1.data == 'retro' or 'flip':
        bot.send_message(callback1.message.chat.id, 'Отправь свой кошелек')

bot.polling(none_stop=True)
