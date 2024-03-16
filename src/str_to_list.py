"""Convert from txt file to list of integers"""
import re

def convert_file_list(string):
    """Split the string and convert non-empty parts to integers"""
    numbers = re.split(r'[,|\-\s]', string)
    lst = []
    for n in numbers:
        if n:
            lst.append(int(n))
    return lst
