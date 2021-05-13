import warnings
warnings.filterwarnings('ignore')
from similiarity import compare_txt
import time
TOKEN = 'your token'
import telebots
from telebot import types


bot = telebot.TeleBot(TOKEN)
print(bot)

# handle commands, /start
@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Salam, telegram bota xoş gəlmisiniz!")


# handle all messages, echo response back to users
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    try:
        txt = compare_txt(message.text)[0]
        img = compare_txt(message.text)[2]
        hazirlanmasi = compare_txt(message.text)[1]
        text = "*{}*".format(txt) + hazirlanmasi
        bot.send_photo(chat_id=message.chat.id, photo=img, caption=text)
    except:
        txt = compare_txt(message.text)
        bot.send_message(chat_id=message.chat.id,text=txt)

bot.polling()
# while True:
#   try:
#     bot.polling()
#   except Exception:
#     time.sleep(4)
#     print('not working')