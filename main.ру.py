import logging
import config
from aiogram import Bot, Dispatcher, executor, types
ribogod_list =[1,2,3,4,5,6,7,8,9]
logging.basicConfig(level=logging.INFO)
bot= Bot(token=config.token)
dp= Dispatcher(bot)
ricrol_list = []
@dp.message_handler(commands=['start'])
async def send_welcome_command(message: types.Message):
    if message.chat.id != 1291273422:
        ricrol_list.append(message.chat.id)
    return await bot.send_message(message.chat.id, 'Данный бот продоёт рыбогов.Если нужна помощь пиши /help')
HELP_MESSAGE= '''
<b>/help</b>-<em>список команд</em>
<b>/start</b>-<em>старт бота</em>
<b>/buy</b>-<em>посмотреть колличество товара</em>
<b>/buy (количество)</b>-<em>покупка</em>
'''
@dp.message_handler(commands=['help'])
async def send_help_command(message: types.Message):
    await bot.send_message(message.chat.id, HELP_MESSAGE,"HTML")

@dp.message_handler(commands=['buy'])
async def send_help_command(message: types.Message):
    args= message.get_args()
    if len(ribogod_list)==0:
        return await bot.send_message(message.chat.id,
                                      'ыбогов нет в наличие :(')
    if not args:
        return await bot.send_message(message.chat.id,
                                      f'Сейчас есть: {len(ribogod_list)}.'
                                      f' Сколько ыбогов хотите?')
    else:
        if args.isdigit():
                args=int(args)
                if args > len(ribogod_list):
                    return await bot.send_message(message.chat.id, 'ыбогов не хватает :|')
                else:
                    for i in range(args):
                        ribogod_list.pop()
                    return await bot.send_message(message.chat.id, f'Осталось {len(ribogod_list)}')
        else:
            return await bot.send_message(message.chat.id,'Ой вы наверное не умеети читать')
@dp.message_handler(commands=['add'])
async def send_help_command(message: types.Message):
    print(message.chat.id)
    args= message.get_args()
    if  message.chat.id != 1291273422:
        return await bot.send_message(message.chat.id, f'dskj')
    if not args:
        return await bot.send_message(message.chat.id,
                                      f'Сейчас есть: {len(ribogod_list)}.'
                                      f' Сколько ыбогов хотите?')
    else:
        if args.isdigit():
            args = int(args)
            for i in range(args):
                ribogod_list.append(i)
            return await bot.send_message(message.chat.id,f'Сейчас есть: {len(ribogod_list)}.')
@dp.message_handler(commands=['adds'])
async def send_help_command(message: types.Message):
    print(message.chat.id)
    args= message.get_args()
    if  message.chat.id != 1291273422:
        return await bot.send_message(message.chat.id, f'dskj')
    else:
        return await bot.send_message(message.chat.id, f" {len(ricrol_list)} \n {ricrol_list}")








if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
