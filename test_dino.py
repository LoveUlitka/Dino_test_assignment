import os
import os.path

ENTER_POINT = 'C:\\Users\\Ulitka\\Desktop\\n\\'
FILE_EXT = '.jpg'
DIR_PREFIX = 'a'
DELIM = '\\'


def items_enumeration(start_path, path_to_name, dirs):
    items = os.listdir(start_path)

    for item in items:
        cur_path = start_path + DELIM + item
        if os.path.isfile(cur_path) and item.lower().endswith(FILE_EXT):
            path_to_name[cur_path] = item
        elif os.path.isdir(cur_path) and item.lower()[0] == DIR_PREFIX:
            dirs.append(cur_path)


def dirs_enumeration(start_path):
    path_to_name = {}
    dirs = []
    items_enumeration(start_path, path_to_name, dirs)

    while dirs:
        sub_path = dirs.pop()
        items_enumeration(start_path, path_to_name, dirs)
    return path_to_name


def print_answer(path_to_name):
    for key, value in d.items():