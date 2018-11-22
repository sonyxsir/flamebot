import random
import telebot

print('FlameBot started...')

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

groanings = ( 'I’ll give you a winter prediction: It’s gonna be cold, it’s gonna be grey, and it’s gonna last you for the rest of your life (с)',
              'Солнце, в Вавилоне Солнце!',
              'В Вавилоне снег с дождём!',
              'Тьма, пришедшая со Средиземного моря...',
              'Мрак, тлен, боль и безысходность',
              'Над всей Испанией безоблачное небо',
              "It's raining cats and dogs")
swear_words = ('хуй', 'пизд', 'пидар', 'гондон', 'мудак', 'бляд', 'блять',
               'ебать', 'ебуч', 'блиа', 'пидор', 'ебис', 'хуе', 'хуи', 'хуя')

# print(bot.get_updates(-1, ['sticker'])[0])

@bot.message_handler(commands=['weather'])

def weather(message):
    bot.send_message(message.chat.id, random.choice(groanings))

@bot.message_handler(commands=['sticker'])

def sticker(message):
    bot.send_sticker(message.chat.id, 'CAADAgADZQoAAkKvaQABQcJ2gX98C_EC')

@bot.message_handler(commands=['help'])

def help(message):
    bot.send_message(message.chat.id, 'Я бот для mstu.flame. Меня создали совсем недавно, и так как мой хозяин - редкостный лентяй, то я пока ещё почти ничего не умею. Ну разве что по мере сил поддерживаюю культуру. Обратиться ко мне можно "бот!"')

@bot.message_handler(content_types=['sticker'])

def sticker_by_user(message):
   bot.send_message(message.chat.id, '{name} отправил стикер'.format(name=message.from_user.first_name))
   bot.send_sticker(message.chat.id, message.sticker.file_id)

@bot.message_handler(commands=['start'])

def start(message):
    sent = bot.send_message(message.chat.id, 'Как твоё имя, начинающий флямер?')
    bot.register_next_step_handler(sent, hello)
def hello(message):
    bot.send_message(
        message.chat.id,
        'Приветствую тебя, {name}. Не балуй тут!'.format(name=message.text))

@bot.message_handler(func=lambda message: True, content_types=['text'])

def echo_msg(message):
    msg = ''
    for c in swear_words:
        if c in message.text.lower():
            msg = 'Конечно, это флям, но ругаться всё равно нехорошо'
            break
        elif ('бот!' in message.text.lower()) or ('бот?' in message.text.lower()):
            msg = 'Слышу, слышу. Но я ещё тупой)'
        else:
            msg = 'Хорошая попытка, флямер! Так держать!\nКоличество символов в сообщении: ' + str(len(message.text)) + '; количество слов: ' + str(len(message.text.split()))
    if msg is not '':
        bot.reply_to(message, msg)

bot.polling(none_stop=True)

