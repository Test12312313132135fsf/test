from config import admin_id
from config import users_id
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import Message
from oauth2client.service_account import ServiceAccountCredentials
import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor
import gspread
from google.oauth2.service_account import Credentials
from config import API_TOKENs

API_TOKEN = API_TOKENs
logging.basicConfig(level=logging.INFO)
GOOGLE_SHEETS_CREDENTIALS_FILE = 'rrtt.json'
SPREADSHEET_NAME = 'AdmHelp'
SPREADSHEET_ID = '1ulIRe2rF92XzXU79gTNYkegueByl451gMYVmWyPDMts'
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('rrtt.json', scope)
client = gspread.authorize(credentials)
SHEET_NAME = 'adw'
SHEETS_NAME = 'rree'
CREDENTIALS_FILE = 'rrtt.json'

# Замените '1ulIRe2rF92XzXU79gTNYkegueByl451gMYVmWyPDMts' на ключ вашей таблицы
SPREADSHEET_KEY = '1ulIRe2rF92XzXU79gTNYkegueByl451gMYVmWyPDMts'

# Подключение к Google Sheets
credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)
spreadsheet = gc.open_by_key(SPREADSHEET_KEY)
sheet = spreadsheet.worksheet('456')  # Работаем с листом 'adw'
async def check_user_id(user_id):
    # Получаем данные из столбца B
    users_id = sheet.col_values(1)  # 2 указывает на столбец B (нумерация начинается с 1)

    # Проверяем наличие user_id в списке
    return str(user_id) in users_id



сredentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)
spreadsheet = gc.open_by_key(SPREADSHEET_KEY)
sheet = spreadsheet.worksheet('qwe')  # Работаем с листом 'qwe'
async def check_admin_id(user_id):
    # Получаем данные из столбца B
    admin_id = sheet.col_values(1)  # 2 указывает на столбец B (нумерация начинается с 1)

    # Проверяем наличие user_id в списке
    return str(user_id) in users_id















SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = 'rrtt.json'  # Путь к файлу с учетными данными
SHEET = 'nlist'  # Название листа на котором содержатся данные

help_comands = """
📌Команды для руководства📌
/stats - узнать количество администрации/агентов поддержки/лидеров.
/zovv - сделать рассылку
/myadmins Nick - выводит статистику Администратора

📌Команды для Главных Следящих📌
/myhelpers Nick - выводит статистику Агента Поддержки  

📌Команды для администраторов📌
/mystats - статистика администратора
/nlist - ники и вк всех администраторов
/sledak - контакты следящих

📌Прочие команды📌
/start - обновить бота/начать работу заново.
/help - список команд.
/id - узнать свой id в telegram.
"""
contactsruk = """
Состав руководства и их контакты:

Главный администратор Rival_Sopko:
VK: https://vk.com/id164894947
Telegram: https://t.me/rivalnepidr

Основной Заместитель Главного Администратора Skay_Eagle:
VK: https://vk.com/id432296014
Telegram: https://t.me/skayeagle

Заместитель Главного Администратора Nikita_Zavgorodnij:
VK: https://vk.com/id703477397
Telegram: https://t.me/nekitpooon

Куратор администрации Lisa_Luger:
VK: https://vk.com/id235757929
Telegram: https://t.me/sonnetsi

Куратор администрации Vana_Ozuk:
VK: https://vk.com/id204965668
Telegram: https://t.me/Valerch1ik
"""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

gc = gspread.service_account(filename=GOOGLE_SHEETS_CREDENTIALS_FILE)
sh = gc.open(SPREADSHEET_NAME)
worksheet = sh.get_worksheet(0)
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Админ-раздел').add('Контакты руководства').add('Команды').add('Список администрации и их VK')


async def check_admin_id(user_id):
    # Получаем данные из столбца B
    admin_id_list = sheet.col_values(1)  # 2 указывает на столбец B (нумерация начинается с 1)

    # Проверяем наличие user_id в списке
    return str(user_id) in admin_id_list

@dp.message_handler(commands=['stats'])
async def send_max_number(message: Message):
    spreadsheet_id = '1ulIRe2rF92XzXU79gTNYkegueByl451gMYVmWyPDMts'
    sheet = client.open_by_key(spreadsheet_id).get_worksheet(2)
    range_names = 'E118:F118'
    range_name2 = 'E119:F119'
    range_name = 'E120:F120'

    values1 = sheet.get(range_names)
    values2 = sheet.get(range_name2)
    values3 = sheet.get(range_name)

    # Находим максимальное число в полученных данных
    admins = max([int(cell) for row in values1 for cell in row])
    helpers = max([int(cell) for row in values2 for cell in row])
    max_number = max([int(cell) for row in values3 for cell in row])
    user_id = message.from_user.id
    if await check_admin_id(user_id):
        await bot.send_message(message.chat.id,
                               f"Количество администраторов: {admins} \nКоличество агентов поддержки: {helpers} \nКоличество лидеров: {max_number}")
    else:
        await message.answer("Ты не являешься членом руководства")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if await check_user_id(user_id):
        await message.reply("Привет,меня зовут PLATINUM MANAGER,введи /help для ознакомления с моим функционалом.",
                            reply_markup=main)
    else:
        await message.reply("Твой аккаунт не внесен в white list.")


@dp.message_handler(commands=['id'])
async def id(message: types.Message):
    await message.answer(f'{message.from_user.id}')


# Обработчик команды /chat_id
@dp.message_handler(commands=['chat_id'])
async def send_chat_id(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, f"Chat ID: {chat_id}")


@dp.message_handler(text='Контакты руководства')
async def contactruc(message: types.Message):
    user_id = message.from_user.id
    if await check_user_id(user_id):
     await message.answer(text=contactsruk)
    else:
     await message.answer("Вы не являетесь администратором")


@dp.message_handler(text='Команды')
async def contactruc(message: types.Message):
    user_id = message.from_user.id
    if await check_user_id(user_id):
     await message.answer(text=help_comands)
    else:
     await message.answer("Вы не являетесь администратором")


@dp.message_handler(text='Список администрации и их VK')
async def contactruc(message: types.Message):
    user_id = message.from_user.id
    if await check_user_id(user_id):
       await get_nlist(message)
    else:
       await message.answer("Вы не являетесь администратором")


@dp.message_handler(commands=['gg'])
async def coinflip(message: types.Message):
    outcome = random.choice(["Снят", "Не снят"])
    user_id = message.from_user.id
    if await check_user_id(user_id):
      await message.answer(outcome)
    else:
     await message.answer("Вы не являетесь администратором")


@dp.message_handler(text='Админ-раздел')
async def contactruc(message: types.Message):
    user_id = message.from_user.id
    if await check_user_id(user_id):
        await bot.send_message(message.chat.id,
                               f"Не реализовано")
    else:
        await message.answer("Вы не являетесь администратором")


@dp.message_handler(commands=['help'])
async def command1(message: types.Message):
    user_id = message.from_user.id
    if await check_user_id(user_id):
        await message.reply(text=help_comands)
    else:
        await message.reply("Твой аккаунт не внесен в white list.")


@dp.message_handler(commands=['mystats'])
async def check_user_info(message: types.Message):
    chat_id = message.chat.id

    sheet = client.open("AdmHelp").worksheet(SHEET_NAME)

    records = sheet.get_all_records()

    user_info = None
    for row in records:
        if str(row['user_id']) == str(chat_id):
            user_info = row
            break

    if user_info:
        response_text = f"Твоя статистика:"
        for key, value in user_info.items():
            if key != 'user_id':
                response_text += f"{key} {value}\n"
        await message.answer(response_text)
    else:
        await message.answer("Вы не являетесь администратором")


@dp.message_handler(Command("myhelpers"))
async def cmd_gg(message: types.Message):
    gc = gspread.authorize(credentials)
    spreadsheet = gc.open_by_key(SPREADSHEET_ID)
    sheet = spreadsheet.get_worksheet(0)
    # Перечислите разрешенные user_id
    allowed_user_ids = {1331138032, 1123923238, 1283697883}

    # Проверяем, что user_id отправителя команды входит в разрешенный список
    if message.from_user.id not in allowed_user_ids:
        await message.answer("Вам не доступна данная команда.")
        return

    try:
        # Разделяем текст команды и никнейм
        command, nickname = message.text.split(' ', 1)

        # Получаем данные из Google таблицы
        records = sheet.get_all_records()

        user_info = None
        for row in records[1:]:  # Начинаем с третьей строки
            if str(row.get('NickName', '')) == nickname:
                user_info = row
                break

        if user_info:
            response_text = f"Информация о Агенте Поддержки с NickName {nickname}:\n"
            for key, value in user_info.items():
                response_text += f"{key}: {value}\n"
            await message.answer(response_text)
        else:
            await message.answer(f"Агент поддержки с NickName {nickname} не найден.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        await message.answer("Неправильный формат команды")


@dp.message_handler(Command("myadmins"))
async def cmd_gg(message: types.Message):
    gc = gspread.authorize(credentials)
    spreadsheet = gc.open_by_key(SPREADSHEET_ID)
    sheet = spreadsheet.get_worksheet(2)

    try:
        # Разделяем текст команды и никнейм
        command, nickname = message.text.split(' ', 1)

        # Получаем данные из Google таблицы
        records = sheet.get_all_records()

        user_info = None
        for row in records[2:]:  # Начинаем с третьей строки
            if str(row.get('NickName', '')) == nickname:
                user_info = row
                break

        user_id = message.from_user.id
        if await check_admin_id(user_id):
            if user_info:
                response_text = f"Информация о Администраторе с NickName {nickname}"
                for key, value in user_info.items():
                    if key != 'user_id':  # Исключаем вывод столбика с названием user_id
                        response_text += f"{key}: {value}\n"
                await message.answer(response_text)
            else:
                await message.answer(f"Администратор с NickName {nickname} не найден.")
        else:
            await message.answer("Вам недоступна данная команда.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        await message.answer("Неправильный формат команды")



@dp.message_handler(commands=['zovv'])
async def send_message_to_users(message: types.Message):
    if message.from_user.id in admin_id:
        # Отправляем сообщение каждому пользователю из списка
        for user_id in users_id:
            try:
                await bot.send_message(user_id, message.text[6:])  # Отправляем сообщение без "/rass "
            except Exception as e:
                logging.exception(e)
    else:
        await message.answer("Вы не являетесь членом руководства")


async def get_nlist(message: types.Message):
    sheet = client.open_by_key(SPREADSHEET_ID).get_worksheet(1)  # Используем метод get_worksheet() для обращения ко второму листу (индексация начинается с 0)
    values = sheet.get_all_values()
    nlist = '\n'.join([f"{row[0]} - {row[1]}" for row in values])
    await message.answer(nlist)

# Добавляем обработчик команды nlist
@dp.message_handler(commands=['nlist'])
async def process_nlist_command(message: types.Message):
    user_id = message.from_user.id
    if await check_user_id(user_id):
        await get_nlist(message)
    else:
        await message.answer("Вы не являетесь администратором")


# Определяем команду /ff
@dp.message_handler(commands=['sledak'])
async def handle_ff_command(message: types.Message):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
    gc = gspread.authorize(credentials)
    spreadsheet = gc.open_by_key(SPREADSHEET_ID)
    sheet = spreadsheet.worksheet(SHEET)
    try:
        # Получаем данные из Google Sheets
        sheet = client.open_by_key(SPREADSHEET_ID).get_worksheet(1)
        names = sheet.col_values(4)
        positions = sheet.col_values(5)
        vkontakte = sheet.col_values(6)

        # Формируем сообщение с данными
        result_message = "Контакты следящих:\n"
        for i in range(1, len(names)):
            result_message += f"{names[i]} - {positions[i]} - {vkontakte[i]}\n"

        # Отправляем сообщение пользователю
        user_id = message.from_user.id
        if await check_user_id(user_id):
         await message.answer(result_message)
        else:
            await message.answer("Вы не являетесь администратором")

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
