from config import config
from YandexAPI import YandexAPI
from RCon import RCon
import telebot
import subprocess
from backup import create_backup

from locale import LOCALE
lang = LOCALE['LANGUAGES'][config['language']]
bot = telebot.TeleBot(config['telegram_token'])

def auth(message):
    chat_id = message.chat.id
    if str(chat_id) in config['allowed_chats']:
        return True
    else:
        return False

@bot.message_handler(commands=['start'])
def handle_start(message):
    if not(auth(message)):  return bot.send_message(message.chat.id, LOCALE['ACCESS_DENIED'][lang] + str(message.chat.id))

    connection = YandexAPI(config['instance_id'])
    connection.get_token()
    r = connection.start()
    if r == True:
        bot.send_message(message.chat.id, LOCALE['SERVER_STARTED'][lang])
    elif r == False:
        bot.send_message(message.chat.id, LOCALE['SERVER_ALREADY_RUNNING'][lang])
    else:
        bot.send_message(message.chat.id, LOCALE['SERVER_ERROR'][lang])


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    if not(auth(message)):  return bot.send_message(message.chat.id, LOCALE['ACCESS_DENIED'][lang] + str(message.chat.id))

    connection = YandexAPI(config['instance_id'])
    connection.get_token()
    r = connection.stop()
    if r == True:
        bot.send_message(message.chat.id, LOCALE['SERVER_STOPPED'][lang])
    elif r == False:
        bot.send_message(message.chat.id, LOCALE['SERVER_ALREADY_STOPPED'][lang])
    else:
        bot.send_message(message.chat.id, LOCALE['SERVER_ERROR'][lang])

@bot.message_handler(commands=['status'])
def handle_status(message):
    if not(auth(message)):  return bot.send_message(message.chat.id, LOCALE['ACCESS_DENIED'][lang] + str(message.chat.id))
    connection = YandexAPI(config['instance_id'])
    connection.get_token()
    r = connection.status()
    status_text = 'Server: ' + r + '\nBackup HTTP Server: RUNNING\n'
    if r == 'RUNNING':
        try:
            connection = RCon(config['ip'], config['rcon_port'], config['rcon_password'])
            connection.command('/list')
            status_text+="Minecraft: RUNNING\n"+connection.command('/list')
        except Exception as error:
            print(error) 
            status_text += 'Minecraft: DOWN'
    bot.send_message(message.chat.id, status_text)

@bot.message_handler(commands=['backup'])        
def handle_backup(message):
    if not(auth(message)):  return bot.send_message(message.chat.id, LOCALE['ACCESS_DENIED'][lang] + str(message.chat.id))
    connection = YandexAPI(config['instance_id'])
    connection.get_token()
    r = connection.status()
    if r == 'RUNNING':
        bot.send_message(message.chat.id, LOCALE['BACKUP_IN_PROGRESS'][lang])
        try:
            create_backup()
            bot.send_message(message.chat.id, LOCALE['BACKUP_SUCCESS'][lang])
        except Exception as error:
            print(error)
            bot.send_message(message.chat.id, LOCALE['SERVER_ERROR'][lang])
    else:
        bot.send_message(message.chat.id, LOCALE['UNABLE_TO_BACKUP'][lang])


@bot.message_handler(commands=['backup_and_stop'])  
def handle_backupandstop(message):
    handle_backup(message)
    handle_stop(message)

@bot.message_handler(commands=['help'])
def handle_info(message):
     bot.send_message(message.chat.id, LOCALE['HELP'][lang])

bot.polling(none_stop=True, interval=0)
