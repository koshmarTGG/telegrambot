import logging
import config
from aiogram import Bot, Dispatcher, executor, types
ribogod_list=[0,1,2,3,4,5,6,7,8,9]
ribogod_dict ={'асось':4, 'семка':1,'азязь':10}
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
<b>/buy</b> - <em>посмотреть колличество товара</em>
<b>/buy (количество)</b>-<em>покупка</em>
'''
def print_dict (ribof):
    tmp=''
    for i in ribof:
        tmn +=f'{i} : {ribof[i]} \n'
    return tmp
@dp.message_handler(commands=['help'])
async def send_help_command(message: types.Message):
    await bot.send_message(message.chat.id, HELP_MESSAGE,"HTML")

@dp.message_handler(commands=['buy'])
async def send_bay_command(message: types.Message):
    args = message.get_args()
    # /buy Язь 3
    args = args.split()

    if not args:
        return await bot.send_message(message.chat.id, f'Вот наш асортимент рыбов\n{print_dict(ribogod_dict)}'
                                                       f'Сколько рыбов вы хотите купить?')
    else:
        if args[0] in ribogod_dict:
            if ribogod_dict[args[0]] == 0:
                return await bot.send_message(message.chat.id,
                                              "Мы сожалеем, но рыбов "
                                              "не осталось, "
                                              "приходите по позже")
            if args[1].isdigit():
                args[1] = int(args[1])
                if args[1] > ribogod_dict[args[0]]:
                    return await bot.send_message(message.chat.id,
                                                  "Мы сожалеем, но "
                                                  "рыбов "
                                                  "не хватит поробуйте "
                                                  "ввести "
                                                  "число поменьше")
                else:
                    ribogod_dict[args[0]] = ribogod_dict[args[0]] - args[1]

                    return await bot.send_message(message.chat.id,
                                                  f"Осталось \n{print_dict(ribogod_dict)} рыбов в наличии.")
            else:
                return await bot.send_message(message.chat.id, "Ой кажется вы ввели "
                                                               "не верное значение, "
                                                               "введите пожалуйста цифру")
        else:
            return await bot.send_message(message.chat.id, "Мы сожалем но такой рыбы нет!")


@dp.message_handler(commands=['adds'])
async def send_help_command(message: types.Message):
    print(message.chat.id)
    if 
        return await bot.send_message(message.chat.id, f" {len(ricrol_list)}")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
