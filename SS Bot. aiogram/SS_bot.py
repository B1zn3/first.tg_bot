from aiogram import Dispatcher, types, Bot, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


API_TOKEN = '6978869260:AAHXcvyveNS0T9hcEXWRhe12kgrS5zz4S_A'
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)




async def on_startup(_):
    print('BOT START')

# Keyboard
kb = ReplyKeyboardMarkup(resize_keyboard=True)

ib1= KeyboardButton(text='/help')
ib2= KeyboardButton(text='/gear')
ib3= KeyboardButton(text='/delivery')
ib4= KeyboardButton(text='/payment')
ib5= KeyboardButton(text='/inst')
ib6= KeyboardButton(text='/chat')

kb.add(ib1).add(ib2)
kb.add(ib3).add(ib4)  
kb.add(ib5).add(ib6)


# Shmot
Shmotki = {'Hoodie POLAR (BLACK)': '180  /EnterItem1',
           'Empyre (GREY)': '180  /EnterItem2',
           'Thrasher (GREY)': '120  /EnterItem3',
           'Hoodie ASSC (BLACK)': '130  /EnterItem4',
           'Hoodie ASSC (BLACK+GREEN)': '150  /EnterItem5',
           'Empyre (BLACK)': '180  /EnterItem6',
           'empyre (GREY)': '180  /EnterItem7',
           'Thrasher (SKYBLUE)': '120  /EnterItem8',
           'Thrasher (BLACK)': '120  /EnterItem9'}


# HELP_box
HELP_box = '''<b>/help</b> - вызов списка комманд 
<b>/gear</b> - наши шмотки 
<b>/delivery</b> - информация про доставку 
<b>/payment</b> - информация об оплате
<b>/inst</b> - мы в instagram 
<b>/chat</b> - дополнительная информация'''

# function /start
@dp.message_handler(commands=['start'])
async def start_massege(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, 
                           text=f'''Здравствуй, {message.from_user.first_name}
Вас приветствует наш shop''')
    await bot.send_message(message.from_user.id, f'''Список команд:
{HELP_box.strip()}''', reply_markup=kb, parse_mode='HTML')
    user_list_proverka = open('database.txt', 'r')
    if str(message.from_user.id)+'\n' not in user_list_proverka:
        user_list_proverka.close()
        user_list_redact = open('database.txt', 'a')    
        user_list_redact.write(str(message.from_user.id)+'\n')
        user_list_redact.close()
    else:    
        user_list_proverka.close()    
    await message.delete()

# function /help
@dp.message_handler(commands=['help'])
async def help_massege(message: types.Message):
    await bot.send_message(message.from_user.id, f'''Список команд:
{HELP_box.strip()}''', parse_mode='HTML')
    await message.delete()


# function /gear
@dp.message_handler(commands=['gear'])
async def start_massege(message: types.Message):
    await bot.send_message(message.from_user.id, f'''<b>Наш shmot:</b>''', parse_mode='HTML')
    for key in Shmotki:
        await bot.send_message(message.from_user.id, f'{key} - <b>Price {Shmotki[key]}</b>', parse_mode='HTML')
    await message.delete()

                               
# function /EnterItem
@dp.message_handler(commands=['EnterItem1', 'EnterItem2', 'EnterItem3', 'EnterItem4', 'EnterItem5', 'EnterItem6', 'EnterItem7', 'EnterItem8', 'EnterItem9'])
async def send_photo(message: types.Message):
    if message.text == '/EnterItem1':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo)
    if message.text == '/EnterItem2':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo) 
    if message.text == '/EnterItem3':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo)
    if message.text == '/EnterItem4':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo)
    if message.text == '/EnterItem5':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo)
    if message.text == '/EnterItem6':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo)
    if message.text == '/EnterItem7':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo)
    if message.text == '/EnterItem8':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo)
    if message.text == '/EnterItem9':
        photo_path = 'PHOTOS\logo.jpg'
        with open(photo_path, 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo)                                                  
    await message.delete()


# function /delivery
@dp.message_handler(commands=['delivery'])
async def delivery_massege(message: types.Message):
    await bot.send_message(message.from_user.id, '''<b>Доставка:</b>
Мы осуществляем доставку Европочтой по всей Беларуси
                         
Возможна личная встреча по Моло
                          
Отправка товара просходит в следующие три дня после заказа(❗бывают исключения)
                                                                              
❗Полная предоплата на карту или наложенным платежом''', parse_mode="HTML")
    await message.delete()


# function /payment
@dp.message_handler(commands=['payment'])
async def payment_massege(message: types.Message):
    await bot.send_message(message.from_user.id, '''<b>Оплата:</b>
❗Полная предоплата на карту или наложенным платежом
                         
Торг по товарам уместен. <b>Возврата нет!</b>
                         
❗Писать насчет покупки: <b>@Pashabolda or @B1zn33</b>''', parse_mode="HTML")
    await message.delete()


# function /chat
@dp.message_handler(commands=['chat'])
async def chat_massege(message: types.Message):
    await bot.send_message(message.from_user.id, '''<b>Дополнительная информация:</b>
По дополнительным вопросам и предложениям писать 
        👇              или           👇
<b>@Pashabolda               @B1zn33</b>''', parse_mode="HTML")
    await message.delete()
    

# function /inst
@dp.message_handler(commands=['inst'])
async def inst_massege(message: types.Message):
    await bot.send_message(message.from_user.id, '''<b>Наш inst:</b> 
https://www.instagram.com/sippy.sh0p/''', parse_mode='HTML')
    await message.delete()


# function for mailing
@dp.message_handler(commands=['send_all'])
async def start_massege(message: types.Message):
    if message.from_user.id == 2095893055:
        user_list_read = open('database.txt', 'r')
        for i in user_list_read:
            await bot.send_message(chat_id=i, text='TEST рассылки')
        user_list_read.close()


# if user no enter function 
@dp.message_handler()
async def all_massege(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'''<b>Ошибка ввода! Введите команду из списка!</b>

Список команд:
{HELP_box.strip()}''', parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)







