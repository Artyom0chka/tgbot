import telebot
from telebot import types


bot = telebot.TeleBot('6379030655:AAFJ-mDOfa2hb_nsNCGE2dWla8AkKBiBQrA')

@bot.message_handler(commands=['start'])
def start(message):
    markup01 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button01 = types.KeyboardButton('ДА!')
    markup01.add(button01)
    bot.send_message(message.chat.id, text=f'Хей, мальчишка *{message.from_user.first_name}*, Хочешь похвастаться сакцесом?', parse_mode="Markdown", reply_markup=markup01)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == 'ДА!'):
        markup02 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn02 = types.KeyboardButton("Ретродроп")
        btn03 = types.KeyboardButton("Сладкий флип")
        markup02.add(btn02,btn03)
        bot.send_message(message.chat.id, text='Каким именно?', reply_markup=markup02)
        bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text == "Ретродроп" or "Сладкий флип":
        bot.send_message(message.chat.id, text='Отправь свой кошелек')


bot.polling(none_stop=True)
