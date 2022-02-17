#Can't find the number yet? In the Telegram robot @for_Fart_old_men_bot

import telebot
from random import randrange
random_int = randrange(21)
print(random_int)
guess = 0


token = '2009459621:AAEWPKIntpiAMFakFDpKw0fM52qg6wsq14U'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, '👋Hi, this bot has just reached adulthood and has found its number. Play with this bot, maybe you will find the number too.')

@bot.message_handler(func=lambda message: True)
def send_normal_message(message):
    if message == 'hi':
        bot.reply_to(message, 'Hello my friend')
    elif message == 'How to play?':
        bot.reply_to (message, "Very easy. Tell me the number, I'm saying you're right or not, do not worry, I'm guiding you more or less ")
    else:
        bot.reply_to (message, "I said puberty, but I do not know how to speak! Let's play.")
        find()

def find():
    while True:
    try:
        var1 = int(input('Guess the number... '))
        if var1 != random_int:
            print('Wrong answer, try again')
        else:
            print(':D Right answer')
            break
        guess += 1
        print(f'{guess} guess is used, and', 3 - guess, ' guess is left')
        if guess == 3:
            print('\nNo guess is left, let us break')
            break
    except ValueError:
        print('Wrong character, try with numbers')
        guess += 1
        print(f'{guess} guess is used, and', 3 - guess, ' guess is left')
        if guess == 3:
            print('\nNo guess is left, let us break')
            break


bot.polling()