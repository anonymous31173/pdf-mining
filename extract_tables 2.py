import requests
from glob import glob
from os import system, path

def find_ext(dr, ext):
    """Returns all files in a directory 'dr' ending with extension
    'ext' """
    return glob(path.join(dr,"*.{}".format(ext)))

file_list = find_ext(".", "pdf")
file_list = [elem[2:] for elem in file_list]
for curr_file in file_list:
    print("Processing " + str(curr_file) + " ...")
    system("stapler sel " + str(curr_file) + " end processing.pdf")
    file_input = {'f': ('processing.pdf', open('processing.pdf', 'rb'))}
    response = requests.post("https://pdftables.com/api?key=9ag38xcu7qsd&format=csv", files=file_input)
    response.raise_for_status() # connection to pdftables API
    csv_name = curr_file[:len(curr_file)-4] + '.csv'
    with open(csv_name, "wb") as f:
        f.write(response.content)
    system("rm processing.pdf")
    system("mv " + str(curr_file) + " processed/" + str(curr_file))
