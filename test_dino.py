import os
import os.path

ENTER_POINT = 'C:\\Users\\Ulitka\\Desktop\\n\\'
FILE_EXT = '.jpg'
DIR_PREFIX = 'a'
DELIM = '\\'


def example(start_path):
    path_to_name = {}
    dirs = []

    items = os.listdir(start_path)
    for item in items:
        cur_path = start_path + item
        if os.path.isfile(cur_path) and item.lower().endswith(FILE_EXT):
            path_to_name[cur_path] = item
        elif os.path.isdir(cur_path) and item.lower()[0] == DIR_PREFIX:
            dirs.append(cur_path)

    while dirs:
        sub_path = dirs.pop()
        items = os.listdir(sub_path)
        for item in items:
            cur_path = sub_path + DELIM + item
            if os.path.isfile(cur_path) and item.lower().endswith(FILE_EXT):
                path_to_name[cur_path] = item
            elif os.path.isdir(cur_path) and item.lower()[0] == DIR_PREFIX:
                dirs.append(cur_path)

    for key, value in path_to_name.items():
        print(key + ' -> ' + value)

example(ENTER_POINT)

# def count_files(path_to_dir):
#     file_counter = 0
#     files = os.listdir(path_to_dir)
#     for f in files:
#         if os.path.isfile(path_to_dir + f) and f.lower().endswith(FILE_EXT):
#             file_counter += 1
#             print(f)
#     print(file_counter)
#     return file_counter
#
# count_files(ENTER_POINT)
#
#
# def check_dir(path_to_dir, CountGlob):
#     files = os.listdir(path_to_dir)
#     CountGlob += count_files(path_to_dir)
#
#     for i in files:
#         if os.path.isdir(PathToDir + i + '\\'):
#             PathToDir = PathToDir + i + '\\'
#             CountGlob += CheckFiles(PathToDir)
#             CheckDir(PathToDir, CountGlob)
#     return CountGlob
# #
# #
# # print(CheckDir(path, CountDll))

