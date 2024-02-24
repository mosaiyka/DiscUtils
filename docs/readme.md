## Классы и их функции (не 👍 а class)

# class client

## Декораторы
- @bot.message
- - Принимает все входящие сообщения (если включен onlyone)
- - Параметры:
- - - message (```def message(message)```)
- @bot.on_dm_gateway
- - Принимает входящие сообщения из лс (если включен onlyone не работает)
- - Параметры:
- - - message (```def on_dm_gateway(message)```)
- @bot.on_message_gateway
- - Принимает входящие сообщения из гильдий (если включен onlyone не работает)
- - Параметры:
- - - message (```def on_message_gateway(message)```)
- @on_event_gateway
- - Принимает все входящие gateway events
- - Параметры:
- - - event (`def on_event_gateway(event)`)
- @on_event
- - Принимает все локальные входящие события самого бота (допустим когда были получены все пользователи из сервера, ответы от requests запросов и т.д.)
- - Параметры;
- - - event(`def on_event(event)`)

## ```bot = DiscUtils.client("TOKEN")```
- Параметры:
- - token - Ваш токен
- - onlyone - если значение True, то все сообщения Discord будут отправляться на метод `@bot.message`, иначе - на `@bot.on_dm_gateway` и `@bot.on_message_gateway`

## ```bot.change_hypesquad_status(1)```
- Меняет у бота хайп😎сквад
- Параметры:
- - hypesquad_house - число от 1 до 3

## `bot.change_name("123", "mosaiyka")`
- Меняет отображаемое имя у пользователя
- Параметры:
- - password - ваш пароль
- - new_display_name - новое отображаемое имя

## `bot.create_channel(46545, "Discutils")`
- Создает канал в гильдии
- Параметры:
- - guild_id - айдишник гильдии
- - name - имя канала
- - type - тип канала (по стандарту 0(текстовый канал))

## `bot.change_bio("new_bio")`
- Изменяет описание бота
- Параметры:
- - new_bio - новое описание

## `bot.get_friends()`
- Возращает список всех друзей пользователя

## `bot.get_profile("91191")`
- Возращает полный профиль пользователя
- Параметры:
- - user_id - айди юзера

## `bot.get_mutualguilds("46735")`
- Возращает общие сервера указанного пользователя и бота
- Параметры:
- - user_id - хз не придумал

## `bot.get_guilds()`
- Возращает список серверов на которых есть бот

## `bot.call(channel_id, guild_id=None, second=5, mute=False, deaf=False):`
- Начинает звонок по указанному адресу 
- Параметры:
- - channel_id - канал куда пойдет звонок
- - guild_id - айди гилдии (обязательно если звониье в гильдию, не пользователю)
- - second - продолжительность звонка
- - mute - бот будет в выключенным микрофоом или нет
- - deaf - у бота будут выключенны наушники или нет

## `bot.typing(322)`
- Отправляет запрос в канал, в течении 5-10 секунд будет отображатся статус тайпинга от вашего бота
- Параметры:
- - channel_id - айди канала

## `bot.add_reaction(channel_id=416, message_id=617, "🤫")`
- Добавляет реакцию на сообщение
- Параметры:
- - channel_id - айди канала
- - message_id - айди сообщения
- - emoji - эмодзи

## `bot.edit_message(14, 322, "это 322")`
- Изменяет уже существующие сообщение
- Параметры:
- - channel_id - айди канала
- - message_id - айди сообщения
- - new_content - новое сообщение

## `bot.delete_message("445", 57)`
- Удаляет сообщение
- Параметры:
- - channel_id - айди канала
- - message_id - айди сообщения

## `bot.send_file(34, "C:/Windows/System32/Okno.png/")`
- Отправляет файл
- Параметры:
- - channel_id - айди канала
- - message - сообщение (не обязательно)
- - path_to_file - путь к файлу

## `bot.send_message(144, "ࠂࠃࠅࠆࠇࠈࠉࠊࠋࠌࠍࠎࠏࠕ", embed)`
- Отправляет сообщение
- Параметры:
- - channel_id - айди канала
- - message - сообщение
- - embed - embed типо чоо (необязательно)

## `bot.get_guild_channels(14727)`
- Возвращает все каналы которые есть в гильдии
- Параметры:
- - guild_id - айди гильдии

## `bot.run()`
- Запускает бота, советую использовать точку входа (`if __name__ == "__main__"``)

# class embeds

## `embeds.get_embed()`
- Возвращает вам ссылку на embed
- Параметры:
- - provider_name - маленький заголовок сверху
- - provider_url - ссылочкк
- - author_name - заголовок побольше
- - author_url - сылочкк
- - title - заголовок
- - color - цвет embed в hex коде
- - media_type - размер медиа (large, mini)
- - media_url - сылочкк
- - description - описание
