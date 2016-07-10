import csv
import re
from os import system
from utils import find_ext


def contains_date(curr_list):
    rege = re.compile("(.+)([a-zA-Z]+) (\d+), (\d+)(.+)")
    for elem in curr_list:
        if rege.match(elem) != None:
            return [True, elem]
    return [False, None]

file_list = find_ext(".", "csv")
file_list = [elem[2:] for elem in file_list]
with open('joined3.csv', 'wb') as output:
    to_write = csv.writer(output, delimiter=',')
    num_cols = 8
    for myfile in file_list:
        with open(myfile) as curr_file:
            jurisdiction = -1
            date_index = -1
            date = None
            csv_lines = list(csv.reader(curr_file))
            for i, line in enumerate(csv_lines[0:10]):
                if 'JURISDICTION/' in line or 'JURISDICTION' in line or 'JURISDICTION/ ORGANIZATION' in line:
                    jurisdiction = i
                if contains_date(line)[0]:
                    date_index = i
                    date = contains_date(line)[1]
            # at this point, have line for jurisdiction, date, and date itself.
            if jurisdiction != -1 and date_index != -1: # check if these exist
                csv_lines = [[[date] + [myfile[5:]] + line + ['']*(num_cols - len(line) - 2)] for line in csv_lines]
                for line in csv_lines:
                    to_write.writerow(line)
                print(myfile)
                system("mv " + str(myfile) + " processed/" + str(myfile))
