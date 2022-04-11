import os

FIND_DIR = input('Where to look(Enter FULL PATH) \n : ')
FIND_STR = input('What words we are looking for \n : ')
ADD_SYMBOLS = 10


def find(dir, string):
    for root, dir_names, file_names in os.walk(dir):
        for name in file_names:
            find_str_in_file(os.path.join(root, name), string)


def find_str_in_file(file, string):
    f = open(file, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    index = content.find(string)
    if index != -1:
        print_find_info (file, content, string)


def print_find_info (file, content, string):
    index =content.find(string)
    start_index = index - ADD_SYMBOLS if index >= ADD_SYMBOLS else 0
    end_index = index + ADD_SYMBOLS + len(string)
    content = content[start_index : end_index]
    content = content.replace(string, "\x1b[32;1m" + string + "\x1b[0m")
    print(f'{file}:\n{content}')


if __name__ == '__main__':
    find(FIND_DIR, FIND_STR)

