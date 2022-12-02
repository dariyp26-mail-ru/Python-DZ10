import telebot

bot = telebot.TeleBot("5888185813:AAGLttnlk6bQYwGDbj2EfBBy4FrZrerj2U4")


def send_answer(answer, count):
    data = open('user_id.txt', 'r', encoding='utf-8')
    users_id = data.readlines()
    a = users_id[count]
    bot.send_message(a, f'{answer}')
    data.close()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    def Help(message):
        user_id = str(message.from_user.id) + '\n'
        data = open('user_id.txt', 'a', encoding='utf-8')
        data.writelines(user_id)
        data.close()
        messageText = str(message.text) + '\n'
        data = open('user_message.txt', 'a', encoding='utf-8')
        data.writelines(messageText)
        data.close()
        bot.send_message(
            message.chat.id, 'Спасибо, ответим в ближайшее время.')

    r = bot.send_message(message.chat.id, 'Здравствуйте, ' +
                         message.from_user.first_name + '. Чем могу помочь?')
    bot.register_next_step_handler(r, Help)


bot.infinity_polling()
