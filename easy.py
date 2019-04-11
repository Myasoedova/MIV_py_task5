# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# import lib_dir
# k = 9 #количество директорий на создание и удаление
# for n in range(1, k+1):
#     lib_dir.makedir('dir_{}'.format(n))
# # print('*****')
# for n in range(1, k+1):
#     lib_dir.deledir('dir_{}'.format(n))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# import lib_dir
# print(lib_dir.currdirs())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# import sys, os, shutil
# f_path = sys.argv[0]
# dir_path = os.path.join(os.getcwd())
# f_new = 'backup_' + os.path.basename(__file__)
# dst = str(dir_path + '/' + f_new)
#
# print('f_path= ', f_path)
# print('dst = ', dst)
# with open(f_path, 'rb') as f:
#     src = f.read()
# with open(dst, 'wb') as f:
#     f.write(src)
