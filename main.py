import telebot
import os

TOKEN = os.getenv("TOKEN") 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "👑 RIKZ OTP FAST AKTIF!\n\nKetik /stok")

@bot.message_handler(commands=['stok'])
def stok(m):
    bot.reply_to(m, "Stok: INDO WA 1200 pcs")

bot.infinity_polling()
