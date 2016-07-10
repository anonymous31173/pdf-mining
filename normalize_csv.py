import numpy as np
from glob import glob
import csv
from os import system, path

def find_ext(dr, ext):
    """Returns all files in a directory 'dr' ending with extension
    'ext' """
    return glob(path.join(dr,"*.{}".format(ext)))

file_list = find_ext(".", "csv")
file_list = [elem[2:] for elem in file_list]
for curr_file in file_list:
    print("Processing " + str(curr_file) + "...")
    index = -1
    with open(curr_file) as curr_csv:
        read_csv = csv.reader(curr_csv)
        csv_lines = list(read_csv)
        for i, row in enumerate(csv_lines):
            if 'ATTENDANCE' in row:
                index = i
                break
        print(curr_file, index)
        if index is not -1:
            with open('norm_' + curr_file, 'wb') as csv_file:
                to_write = csv.writer(csv_file, delimiter=',')
                for i in range(index, len(csv_lines)):
                    to_write.writerow(csv_lines[i])
            system("mv " + str(curr_file) + " processed/" + str(curr_file))
