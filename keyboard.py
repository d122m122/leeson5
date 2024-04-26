from telebot import types


def generate_main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="Share contact", request_contact=True)
    keyboard.row(btn)
    return keyboard

def laptop_manu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="Laptop")
    keyboard.row(btn)
    return keyboard


def buy_laptop():
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Batafsil", url='https://asaxiy.uz/product/noutbuk-hp-15s-fq5004-core-i3-1215u-ddr4-4gb-ssd-256gb-156hd-silver')
    keyboard.row(btn)
    return keyboard