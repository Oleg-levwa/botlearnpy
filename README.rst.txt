CatBot
======

CatBot - это бот для Telegram, созданный с целью учёбы.

Установка
---------

Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:
.. code-block:: text
    pip install -r requirements.txt

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:
.. code-block:: python
PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
    'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password':'ПАРОЛЬ'}}

API_KEY = 'API ключ, который вы получили у BotFather'

USER_EMOJI = [':smley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

Запуск
------

В активированном вирт окружении выполните:
.. code-block:: text
    python bot.py
