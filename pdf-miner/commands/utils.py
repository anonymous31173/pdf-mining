# utils.py
import glob
from os import path


def find_ext(dr, ext):
    """Returns all files in a directory 'dr' ending with extension
    'ext' """
    return glob(path.join(dr, "*.{}".format(ext)))
