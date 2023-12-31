import telebot


bot = telebot.TeleBot("6544678909:AAF1GJM18z_YrjTaHyGi_9VnxucaN-ylTe0")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "1":
        bot.send_message(message.from_user.id, "12")
    elif message.text == "2":
        bot.send_message(message.from_user.id, "67")
    elif message.text == "3":
        bot.send_message(message.from_user.id, "29")
    elif message.text == "4":
        bot.send_message(message.from_user.id, "05")
    elif message.text == "5":
        bot.send_message(message.from_user.id, "81")
    elif message.text == "6":
        bot.send_message(message.from_user.id, "09")
    elif message.text == "7":
        bot.send_message(message.from_user.id, "54")
    elif message.text == "8":
        bot.send_message(message.from_user.id, "33")
    elif message.text == "9":
        bot.send_message(message.from_user.id, "40")
    elif message.text == "10":
        bot.send_message(message.from_user.id, "51")
    elif message.text == "11":
        bot.send_message(message.from_user.id, "19")
    elif message.text == "12":
        bot.send_message(message.from_user.id, "01")
    elif message.text == "13":
        bot.send_message(message.from_user.id, "91")
    elif message.text == "14":
        bot.send_message(message.from_user.id, "76")
    elif message.text == "15":
        bot.send_message(message.from_user.id, "14")
    else:
        bot.send_message(message.from_user.id, "Для такого пирожного нету пароля. Убедитесь что вы ввели правильный номер.")


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

