
import telebot

host = "localhost"
port = 3307
user = "root"
password = "takeoff_2018"
db_name = "NFT_Sale"

# admin_list = [849231212, 493115134, 560945352]
# """ Еловский, Гозенко Артём, Гозенко Анатолий """

admin_list = [849231212, 485563456, 675564806]
""" Еловский, Краснов, Попов"""

# TON_NUMBER = "EQCA0vWJntuL61f1-xQB2EwMorKpI448L5sh9c1kC29f8D4V"

#main variables
TOKEN = "5590720904:AAHZe3EuakfrLjFI-3kChcaYdLjyh8I2Wss"
bot = telebot.TeleBot(TOKEN)

callback_capcha = ['👥', '👾', '🐰', '🍀', '🍌']
flag_capcha = False