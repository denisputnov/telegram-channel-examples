import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# инициализация бота 
bot = telebot.TeleBot(os.getenv('TELEGRAM_API_TOKEN'))

# обработчик для команды /start
@bot.message_handler(commands=['start', 'старт'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет, <b>{message.chat.first_name}</b>, это тестовый бот канала @prog_way_blog. <b>Зачем?</b>\n\nОн нужен как тестовый образец для <a href="https://t.me/prog_way_blog/48">одного из последних постов</a>. Код бота открыт, его можно найти <a href="###">тут</a>.\n\nБот создан исключительно в обучающих целях и в скором времени будет отключен. Код останется всё так же доступен на github.\nАвтор: @grnbows', parse_mode="HTML", disable_web_page_preview=True)

    # ! Метод отправки фото.
    with open('./assets/images/pw.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption="Вот так вот бот может отправлять различные фоточки.")

    bot.send_message(message.chat.id, "Как ты видишь, на одну команду можно отправить сразу несколько сообщений.\n\nМожешь написать /help, чтобы увидеть полный список команд.")

# обработчик для команды /help
@bot.message_handler(commands=['help', 'помощь'])
def send_help(message):
    bot.send_message(message.chat.id, '/keyboard - клавиатура\n/chat_action - бот покажет анимацию отправки чего-либо\n/sticker - получить стикер от бота\n/voice - получить звуковое сообщение от бота\n/location - сообщение с локацией\n/document - бот отправит вам документ')

@bot.message_handler(commands=['keyboard'])
def send_keyboard(message):
    # ! Инициализация клавиатуры.
    keyboard = InlineKeyboardMarkup()

    # ! Создание кнопок для клавиатуры.
    channel = InlineKeyboardButton('Канал ProgWay', url='https://t.me/prog_way_blog')
    author = InlineKeyboardButton('Автор канала', url='https://t.me/grnbows')
    code = InlineKeyboardButton('Код бота на Github', url='###')
    
    # ! Добавление кнопок к клавиатуре.
    keyboard.add(channel, author)
    keyboard.add(code)
    
    # ! отправляем через обычный send_message. Клавиатуру прикрепляем через параметр "reply_markup".
    bot.send_message(message.chat.id, 'Кнопочки выглядят примерно так и это не единственный вариант их исполнения. Это лишь один из них, как пример.', reply_markup=keyboard)
    
    
@bot.message_handler(commands=['chat_action'])
def send_animation(message):
    bot.send_message(message.chat.id, 'Сейчас сверху появится анимация будто бот записывает голосовое сообщение.')
    with open('./assets/images/chat_action.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    # ! Показываем chat_action
    bot.send_chat_action(message.chat.id, 'record_audio')


@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    # ! Отдельный метод отправки стикеров.
    with open('./assets/stickers/love.tgs', 'rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)


@bot.message_handler(commands=['voice'])
def send_voice(message):
    # ! Метод для отправки голосовых сообщений. 
    with open('./assets/audio/voice.ogg', 'rb') as voice:
        bot.send_voice(message.chat.id, voice, caption="Примерно так может выглядеть голосовое сообщение от бота.")
    with open('./assets/audio/voice2.ogg', 'rb') as voice:
        bot.send_voice(message.chat.id, voice, caption="Для этого можно подключить какую-нибудь библиотеку с распознованием речи и, по сути, бот готов. Крайне простой и полезный концепт в современном мире)")


@bot.message_handler(commands=['location'])
def send_location(message):
    # ! Отправка геогокации по заданной широте и долготе.
    bot.send_location(message.chat.id, 25.204849, 55.270782)
    with open('./assets/images/google.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption='Дубае. Ориентировочно именно там находится штаб-квартира Телеграма. Ну, по крайней мере, я это прочитал по запросу в Гугле.')
    

@bot.message_handler(commands=['document'])
def send_document(message):
    # ! Метод отправки документа.
    with open('./assets/documents/document.txt', 'rb') as document:
        bot.send_document(message.chat.id, document, caption='Просто и со вкусом.')


# благодаря этой команде бот будет получать обновления от серверов телеграма
bot.polling(none_stop=True)