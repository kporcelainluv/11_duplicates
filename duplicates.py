import os
from collections import Counter
import sys


def collecting_filenames_from_dir(directory_path):
    list_of_filenames_in_dir = list()
    for path, dirs, files_names in os.walk(directory_path):
        for filename in files_names:
            size_of_file = str(os.stat(os.path.join(path, filename)).st_size)
            name_and_size_of_file = (filename, size_of_file)
            list_of_filenames_in_dir.append(name_and_size_of_file)
    return list_of_filenames_in_dir


def finding_duplicates(list_of_filenames):
    counter_of_file_names = Counter(list_of_filenames)
    print("The duplicates are: ")
    for name_and_size in counter_of_file_names:
        if counter_of_file_names[name_and_size] >= 2:
            print(name_and_size[0], " path to file:", os.path.abspath(name_and_size[0]))
    return "Thank you for using the program!"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(finding_duplicates(collecting_filenames_from_dir(sys.argv[1])))

