# Moein Moatali
""" Telegram bot """

import random
import datetime
import datetime
from persiantools import jdatetime
import qrcode
import gtts
import telebot
from telebot import types

bot = telebot.TeleBot("6773978154:AAHUAbh_tf7oIykyHrdvA82J5tjTHreWLrI", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
item_markup1 = telebot.types.KeyboardButton("Game")
item_markup2 = telebot.types.KeyboardButton("Age")
item_markup3 = telebot.types.KeyboardButton("Voice")
item_markup4 = telebot.types.KeyboardButton("Max")
item_markup5 = telebot.types.KeyboardButton("Argmax")
item_markup6 = telebot.types.KeyboardButton("QRcode")
item_markup7 = telebot.types.KeyboardButton("Help")
markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f" Welcome, {user_name} 🤩🥳", reply_markup=markup)

@bot.message_handler(func= lambda m : True)
def Main_Func(message) :

    if message.text == "Game" :
        Start_Game(message)
    elif message.text == "New game" :
        New_Game(message)
    elif message.text == "Home" :
        ...
    elif message.text == "Age" :
        Get_Birthday(message)
    elif message.text == "Voice" :
        Voice_Text(message)
    elif message.text == "Max" : 
        Get_Numbers(message)
    elif message.text == "Argmax":
        Get_Numbers_2(message)
    elif message.text =="QRcode" :
        QRCode_Text(message)
    elif message.text == "Help":
        Help(message)
    
    



Number = random.randint(1, 100)
chat_id = None
Counter = 0

def Home(message):

    
    markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
    item_markup1 = telebot.types.KeyboardButton("Game")
    item_markup2 = telebot.types.KeyboardButton("Age")
    item_markup3 = telebot.types.KeyboardButton("Voice")
    item_markup4 = telebot.types.KeyboardButton("Max")
    item_markup5 = telebot.types.KeyboardButton("Argmax")
    item_markup6 = telebot.types.KeyboardButton("QRcode")
    item_markup7 = telebot.types.KeyboardButton("Help")
    markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)
    
    lst = ["باشه","چشم مهندس","حله"]
    bot.reply_to(message,random.choice(lst), reply_markup=markup)

def Start_Game(message):
        
        global chat_id
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(row_width=1)
        item_markup1 = types.KeyboardButton("New game")
        item_markup2 = types.KeyboardButton("Home")
        markup.add(item_markup1)
        markup.add(item_markup2)
        msg = bot.send_message(chat_id, "بین 1 تا 100 یک عدد انتخاب گن", reply_markup=markup)
        bot.register_next_step_handler(msg, Guess_Number)

def Guess_Number(message):

    global Number
    global Counter

    if message.text == "صفحه اصلی" :
        Home(message)
    elif message.text == "بازی جدید" :
        New_Game(message)
    else: 
        guess = int(message.text)
        if guess > Number:
            Counter += 1
            msg = bot.send_message(chat_id, "بزرگ حدس زدی  👇🏼")
            bot.register_next_step_handler(msg, Guess_Number)
        elif guess < Number:
            Counter += 1
            msg = bot.send_message(chat_id, "کم گفتی برو بالاتر ☝🏼")
            bot.register_next_step_handler(msg, Guess_Number)
        elif guess == Number:
            bot.send_message(chat_id, f"بعد از {Counter + 1} درست حدس زدی عزیزم 🤩🤩  ")
            markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)
            Counter = 0
        

def New_Game(message):

    global Counter
    global Number
    Number = random.randint(1, 100)
    msg = bot.send_message(chat_id, "یک عدد بین 1 تا 100 بگو")
    bot.register_next_step_handler(msg, Guess_Number)


def Get_Birthday(message):
    msg = bot.send_message(message.chat.id, "Please give me your bitrhday in Solar year like this 1365-06-16")
    bot.register_next_step_handler(msg, Calculate_Age)

def Calculate_Age(message):
    birthday_year, birthday_month, birthday_day = map(int, message.text.split("-"))
    miladi_date = jdatetime.JalaliDate(birthday_year, birthday_month, birthday_day).to_gregorian()
    age_timedelta = datetime.date.today() - miladi_date
    age_years = age_timedelta.days // 365
    bot.send_message(message.chat.id, f"You are {age_years} years old")


def Voice_Text(message):
    msg = bot.send_message(message.chat.id, "یک متن به زبان انگلیسی تایپ کن")
    bot.register_next_step_handler(msg, Text_To_Voice)

def Text_To_Voice(message):
    user_text = message.text
    voice = gtts.gTTS(user_text, lang="en", slow=False)
    voice.save("Pylearn7\Assignment 9/voice.mp3")
    with open("Pylearn7\Assignment 9/voice.mp3", "rb") as voice_file:
      bot.send_voice(message.chat.id, voice_file)


def Get_Numbers(message):
    msg = bot.send_message(message.chat.id, "یک لیست این مدلی از اعداد بگو 14,7,78,15,8,19,20")
    bot.register_next_step_handler(msg, Show_Max)

def Show_Max(message):
    Numbers = list(map(int, message.text.split(",")))
    Max_Number = max(Numbers)
    bot.send_message(message.chat.id, f" بزرگ ترین عدد {Max_Number}")


def Get_Numbers_2(message):
    msg = bot.send_message(message.chat.id, "یک لیست از اعداد به این صورت درست کن 14,7,78,15,8,19,20")
    bot.register_next_step_handler(msg, Show_Max_Arg)


def Show_Max_Arg(message):
    Numbers = list(map(int, message.text.split(",")))
    Max_Index = Numbers.index(max(Numbers))
    bot.send_message(message.chat.id, f"بزرگ ترین خونه این است {Max_Index}")

def QRCode_Text(message):
    msg = bot.send_message(message.chat.id, "یک متن تایپ کن")
    bot.register_next_step_handler(msg, Create_QRCode)

def Create_QRCode(message):
    qr_img = qrcode.make(message.text)
    qr_img.save("Pylearn7\Assignment 9/qrcode.png")
    with open("Pylearn7\Assignment 9/qrcode.png", "rb") as qr_file:
        bot.send_photo(message.chat.id, qr_file)


def Help(message):

    bot.reply_to(message, "میخوام بهت کمک کنم ")

    bot.send_message(message.chat.id, "QRcode: Make a QRcode with your text\n"
                                    "\nGame: Start a guess number game\n"
                                    "\nAge: Calculate your age\n"
                                    "\nVoice: Convert your sentence to voice\n"
                                    "\nMax: Return the maximum number of a list of numbers\n"
                                    "\nArgmax: Retrun the index of the maximum number of a list of numbers\n"
                                    )

bot.infinity_polling()