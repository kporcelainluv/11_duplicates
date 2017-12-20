from collections import defaultdict
import os
import sys


def collecting_filenames_from_dir(directory_path):
    dict_of_filenames_in_dir = defaultdict(list)
    for path, dirs, files_names in os.walk(directory_path):
        for filename in files_names:
            size_of_file = str(os.stat(os.path.join(path, filename)).st_size)
            name_and_size_of_file = (filename, size_of_file)
            dict_of_filenames_in_dir[name_and_size_of_file].append(path)
    return dict_of_filenames_in_dir.items()


def finding_duplicates(dict_of_filenames_in_dir):
    dictionary_of_duplicates = {}
    for (name, size), paths in dict_of_filenames_in_dir:
        if len(paths) > 1:
            dictionary_of_duplicates[(name, size)] = paths
    return dictionary_of_duplicates


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("The duplicates are: ")
        duplicates = finding_duplicates(collecting_filenames_from_dir(sys.argv[1]))
        for name_and_size in duplicates:
            print("filename:", name_and_size[0], end="\n")
            for path_to_file in duplicates[name_and_size]:
                print("path to file:", os.path.join(os.getcwd() + path_to_file))
