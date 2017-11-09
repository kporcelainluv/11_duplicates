import os
from collections import Counter
import sys


def directory_name():
    file_path = filepath
    return file_path


def collecting_filenames_from_dir(directory_path):
    list_of_filenames_in_dir = list()
    for path, dirs, files_list in os.walk(directory_path):
        for file in files_list:
            size_of_file = str(os.stat(path + "/" + file).st_size)
            name_and_size_of_file = file + "-" + size_of_file
            list_of_filenames_in_dir.append(name_and_size_of_file)
    return list_of_filenames_in_dir


def printing_duplicates(list_of_filenames):
    counter_of_file_names = Counter(list_of_filenames)
    print("The duplicates are: ")
    for name in counter_of_file_names:
        number_of_duplicates = counter_of_file_names[name]
        if number_of_duplicates >= 2:
            filesize_in_filename = name.index("-")
            print(name[:filesize_in_filename])
    return "Thank you for using the program!"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print(printing_duplicates(collecting_filenames_from_dir(directory_name())))
