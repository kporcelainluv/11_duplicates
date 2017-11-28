import os
import sys


def collecting_filenames_from_dir(directory_path):
    list_of_filenames_in_dir = dict()
    dictionary_of_duplicates = dict()
    for path, dirs, files_names in os.walk(directory_path):
        for filename in files_names:
            size_of_file = str(os.stat(os.path.join(path, filename)).st_size)
            name_and_size_of_file = (filename, size_of_file)
            if name_and_size_of_file in list_of_filenames_in_dir:
                dictionary_of_duplicates[name_and_size_of_file] = path
            else:
                list_of_filenames_in_dir[name_and_size_of_file] = path
    print(dictionary_of_duplicates)
    return list_of_filenames_in_dir


def finding_duplicates(dictionary_of_duplicates):
    print("The duplicates are: ")
    for name_and_size in dictionary_of_duplicates:
        print("filename:", name_and_size[0], end="\n")
        print("path to file:", (os.getcwd() + "/" + dictionary_of_duplicates[name_and_size]))
    return "Thank you for using the program!"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(finding_duplicates(collecting_filenames_from_dir(sys.argv[1])))
