from aiogram import Dispatcher, types


async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [types.BotCommand(command='/start', description='Запуск бота'),
                          types.BotCommand(command='/help', description='Как пользоваться ботом'),
                          ]
    await dp.bot.set_my_commands(main_menu_commands)
