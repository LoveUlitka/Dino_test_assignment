import os
import os.path

ENTER_POINT = 'C:\\Windows\\System32\\'
FILE_EXT = '.dll'
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
        items_enumeration(sub_path, path_to_name, dirs)
    return path_to_name


def print_answer(path_to_name):
    count_files = 0
    files = []
    for key, value in path_to_name.items():
        count_files += 1
        files.append(value)
    print('Number of files: ' + str(count_files) + '\n')
    print('Files:')
    for i in range(count_files):
        print(files[i])

path_to_name = dirs_enumeration(ENTER_POINT)
print_answer(path_to_name)