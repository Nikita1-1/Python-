import telebot
import requests
from pprint import pprint 

#you will need this if your create different file with api_telegram_bot key and name it API_KEY
#then import it from file name bot_key variable API_KEY
from bot_key import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)


# @bot.message_handler(func=lambda msg: True)
# def echo_all(msg):
#     bot.reply_to(msg, msg.text)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to my botchat!  Here are the available commands:\n/horoscope - Get your daily horoscope\n/news - Get the latest news\n/help - See the list of available commands")')

@bot.message_handler(content_types = ["photo", "sticker"])
def send_content_message(msg):
    print(msg)
    bot.reply_to(msg, "i see what you mean!")

#The sign_zodiac function is registered as a handler for the /horoscope command. 
#This function asks the user for their zodiac sign using a Markdown-formatted message, 
#and then registers the day_handler function as the next step in the conversation.
@bot.message_handler(commands=['horoscope'])
def sign_zodiac(message):
    text = 'What is your zodiac sign?\n Choose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*.'
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    #register_next_step_handler takes 2 param = msg send by user and day 
    bot.register_next_step_handler(sent_msg, day_handler)

#In the context of the day_handler function, 
#this line is executed after the user has provided their zodiac sign in response to the bot's prompt. 
#When the user sends a message to the bot, the message is passed to the day_handler function as an argument named message.
def day_handler(message):
    sign = message.text
    text = 'What do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD.'
    sent_msg = bot.send_message(message.chat.id, text, parse_mode='Markdown')
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign.capitalize())

def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_zodiac(sign,day)
    data = horoscope['data']
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, 'Here is your horocope')
    bot.send_message(message.chat.id, horoscope_message, parse_mode='Markdown')
    check_again(message)


def get_zodiac(sign, day):
    url = 'https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily'
    params = {'sign' : sign, 'day': day}
    response = requests.get(url, params)

    return response.json()


def check_again(message):
    again_message = 'Do you want to check another zodiac sign?\nChoose one: *Yes*, *No*'
    sent_msg = bot.send_message(message.chat.id, again_message, parse_mode='Markdown')
    bot.register_next_step_handler(sent_msg, handle_again)

def handle_again(message):
    response = message.text.lower()
    if response == 'yes':
        sign_zodiac(message)
    elif response == 'no':
        bot.send_message(message.chat.id, 'Okay, see you later!')
    else: 
        bot.send_message(message.chat.id, "Sorry, I didn't understand your response. Please choose one: *Yes* or *No*.")
        check_again(message)

@bot.message_handler(commands=['news'])
def get_news(message):
    url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=ad9c96fe27a74157b22dca016a1e1561'
    response = requests.get(url)
    data = response.json()
    
    articles = data['articles']
    
    text = ''
    for i in range(8):
        article = articles[i]
        text += f'{i+1}. {article["title"]}\n{article["url"]}\n\n'
        
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['leave_a_message'])
def direct_msg(message):
    msg = bot.send_message(message.chat.id, 'What note would you like to leave?')
    bot.register_next_step_handler(msg, send_it)
def send_it(message):
    mssg = message.text
    bot.send_message(chat_id='YOUR_ID', text=mssg)

bot.polling()