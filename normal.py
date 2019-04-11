# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
import os, sys, lib_dir
print('sys.argv = ', sys.argv)
def print_help():
    print('godir - перейти в папку')
    print('dircur - просмотреть содержимое тек папки')
    print('deledir - удалить папку')
    print('mdir <dir_name> - создать папку')
print_help()

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
# если сделать список ключей, то выполняются все функции из модуля по порядку, я хочу чтобы только выбранная
# do = {
#     'godir': lib_dir.go_dir(dir_name),
#     'dircur': lib_dir.dirs(dir_name),
#     'deledir': lib_dir.deledir(dir_name),
#     'mdir': lib_dir.makedir(dir_name),
#     'help': print_help()
# }

# try:
#     key = sys.argv[1]
# except IndexError:
#     key = None
# if key in sys.argv:
    # if do.get(key):
    #     do [key]()
    # print('Задан неверный ключ')
    # print('Укажите ключ help для справки')
try:
    key = sys.argv[1]
except IndexError:
    print('Задан неверный ключ')
    print('Укажите ключ help для справки')

if 'godir' in sys.argv[1]:
    lib_dir.go_dir(dir_name)
if 'dircur' in sys.argv[1]:
    lib_dir.dirs(dir_name)
if 'deledir' in sys.argv[1]:
    lib_dir.deledir(dir_name)
if 'mdir' in sys.argv[1]:
    lib_dir.makedir(dir_name)
if 'help' in sys.argv[1]:
    print_help()

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
