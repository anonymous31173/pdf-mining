import requests
from os import system
import csv
from utils import find_ext

# get pdf list.
file_list = find_ext(".", "pdf")
file_list = [elem[2:] for elem in file_list]


for curr_file in file_list:
    # print status message to stdout
    print("Processing " + str(curr_file) + " ...")
    # select last page of a pdf, push to temp file processing.pdf
    system("stapler sel " + str(curr_file) + " end processing.pdf")
    # create dict for raise request to API
    file_input = {'f': ('processing.pdf', open('processing.pdf', 'rb'))}
    response = requests.post("https://pdftables.com/api?key=9ag38xcu7qsd&format=csv", files=file_input)
    response.raise_for_status()  # connection to pdftables API
    # removes ext, appends csv
    csv_name = curr_file[:len(curr_file)-4] + '.csv'

    # push parsed output to CSV.
    with open(csv_name, "wb") as f:
        f.write(response.content)
        read_csv = csv.reader(f)
        csv_lines = list(read_csv)
        index = None
        for i, row in enumerate(csv_lines):
            # use structure of data, looking for line w/ 'Attendance' key
            if 'ATTENDANCE' in row:
                index = i
                break
        # if index is not None, we know that the data is correctly structured.
        if index:
            with open('norm_' + csv_name, 'wb') as csv_file:
                to_write = csv.writer(csv_file, delimiter=',')
                for i in range(index, len(csv_lines)):
                    to_write.writerow(csv_lines[i])
            # mark pdf as processed
            system("mv " + str(curr_file) + " processed/" + str(curr_file))
            # mark csv as processed
            system("mv " + str(csv_name) + " processed/" + str(curr_file))
        # in this case, the file is not correctly structured for parser.
        else:
            print("File with name" + str(curr_file) + "does not contain key.")
            # mark pdf and csv as error in processing.
            system("mv " + str(curr_file) + " errdir/" + str(curr_file))
            system("mv " + str(csv_name) + " errdir/" + str(curr_file))

    # delete temporary file, 'processing.pdf'
    system("rm processing.pdf")
