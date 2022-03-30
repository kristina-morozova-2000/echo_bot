# Echo_bot
Echo_bot - эхо-бот дя Telegram, который умеет повторять: текстовые сообщения, изображения, стикеры, документы, аудиозаписи, голосовые сообщения и геолокацию.

## Список файлов
main.py - содержит код бота;
.env - содержит токен бота;
requirements.txt - содержит список зависимостей: библиотек, которые необходимо установить.

## Настройка и запуск
Должен быть устaновлен python версии не ниже 3.8 (инструкция по [ссылке](https://python-scripts.com/install-python-windows) )
____
Перейдите в корневую папку проекта. Создайте виртуальное окружение и активируйте его (инструкция по [ссылке](https://python-scripts.com/virtualenv) ). 
Выполните команду, устанавливающую зависимости:
pip install -r requirements.txt
____
Необходимо создать telegram-бота и получить его токен (инструкция по [ссылке](https://tlgrm.ru/docs/bots) ).
Полученный токен скопируйте в файл .env. Запись в данном файле должна выглядеть следующим образом:
TOKEN_BOT='your_telegram_bot_token'
____
Для запуска бота выполните команду:
python3 main.py
