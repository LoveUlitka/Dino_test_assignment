import os

ENTER_POINT = 'C:\\Windows\\System32'
# Warning! when run 32-bit python on 64-bit Windows
# \System32 path will be swapped to \SysWOW64 internally

FILE_EXT = '.dll'
DIR_PREFIX = 'a'


# for given directory (start_path):
#   append all subdirs into dirs
#   insert all files into path_to_name dict
def visit_dir(start_path, path_to_name, dirs):
    items = os.listdir(start_path)
    for item in items:
        cur_path = os.path.join(start_path, item)
        if os.path.isfile(cur_path) and item.lower().endswith(FILE_EXT):
            path_to_name[cur_path] = item
        elif os.path.isdir(cur_path) and item[0] == DIR_PREFIX:
            dirs.append(cur_path)


# recursive dir traverse
# return dict {full path : filename}
def dir_iter(start_path):
    path_to_name = {}
    dirs = []  # dirs to proceed
    visit_dir(start_path, path_to_name, dirs)

    while dirs:
        sub_path = dirs.pop()
        visit_dir(sub_path, path_to_name, dirs)
    return path_to_name


def print_answer(path_to_name):
    print('Number of files: ' + str(len(path_to_name)) + '\n')

    print('Files:')
    for key, value in path_to_name.items():
        print(key + " -> " + value)

path_to_name = dir_iter(ENTER_POINT)
print_answer(path_to_name)