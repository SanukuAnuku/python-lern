"""Скрипт показывает информацию об ос
    Основная инфа которая показывает этот скрипт:
    -Информация об имени
    -Инфо об версии ос
    -Инфа об времени (год, месяц, день, часы)
    -Инфо об int
    -Копирайт
    -Инфа про расположения
    -Инфа по api версии"""

import os
import sys
import platform
import datetime

os_name = platform.system() #берёт имя пользователя
os_version = platform.version() #берёт версию ос
os_arch = platform.architecture()[0]

now = datetime.datetime.now() #берёт время (сейчас)
sys_in = sys.path

info = sys.int_info #Информация
copy = sys.copyright #Копирайт
dir = sys.argv #Расположение данного файла
ver = sys.api_version #Версия

print(f"{os_name} \n"
      f"{os_version} \n"
      f"{os_arch} \n"
      f"{now.year} \n"
      f"{now.month} \n"
      f"{now.day} \n"
      f"{now.hour} \n"
      f"{info} \n"
      f"{copy} \n"
      f"{dir} \n"
      f"{ver} \n"
      "end")