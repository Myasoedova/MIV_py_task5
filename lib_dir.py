def makedir(dir_name):
    import os
    if not dir_name:
        print('Необходимо указать имя директории 2-м параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('успешно создана папка {} '.format(dir_path))
    except FileExistsError:
        print('Ошибка! Такая директория {} уже есть!'.format(dir_path))

def deledir(dir_name):
    import os
    if not dir_name:
        print('Необходимо указать имя директории 2-м параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.removedirs(dir_path)
    except FileNotFoundError:
        print('Ошибка, не удалось найти такую папку и удалить! {}'.format(dir_path))
    else:
        print('папка {} - успешно удалена! '.format(dir_path))


def dirs(dir_name):
    import os
    dir_path = os.path.join(os.getcwd(), dir_name)
    for i, d, f in os.walk(dir_path):
        print('По этому пути : {} располгаются такие папки'.format(i))
        # если надо вложенность показать
        for _d in d:
            print(_d)
def currdirs():
    import os
    dir_path = os.path.join(os.getcwd())
    for i, d, f in os.walk(dir_path):
        print('По этому пути : {} располгаются такие папки'.format(i))
        # если надо вложенность показать
        for _d in d:
            print(_d)


def go_dir(dir_name):
    import os
    if not dir_name:
        print('Необходимо указать путь директории, куда перейти')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    print(dir_path)
    os.chdir(dir_path)