import os
import glob


def get_file_paths():
    files_path = os.getcwd() + "/sorted/"
    file_paths = glob.glob(files_path + "*.txt")
    return file_paths


def read_file_and_write_to_result():
    file_paths = get_file_paths()
    file_content_lst = []
    for file in file_paths:
        file_name = file.split("/")[-1]
        with open(file, encoding="utf-8") as f:
            data = f.readlines()
            file_content_lst.append([len(data), file_name, data])
    file_content_lst.sort()
    with open("result.txt", "w", encoding="utf-8") as res_f:
        for el in file_content_lst:
            res_f.write(f"{el[0]}\n{el[1]}\n{''.join(el[2])}\n")


read_file_and_write_to_result()