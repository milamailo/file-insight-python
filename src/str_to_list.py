"""Convert"""
def convert_file_list(string):
    """Convert from txt file to list of integers"""
    numbers = string.split('-')
    lst =[]
    for n in numbers:
        lst.append(int(n))

    return  lst
