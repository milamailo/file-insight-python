"""read and write"""
def read_write_file(filename, option, content=None):
    """Read from or write to a file."""
    #don't need to explicitly close the file when using the with statement
    #because Python takes care of closing the file automatically.
    if option == 'read':
        with open(filename, 'r', encoding='utf-8') as file:
            # Reading from the file
            content = file.readline()
        return content
    elif option == 'write':
        with open(filename, 'a', encoding='utf-8') as file:
            # Writing to the file
            file.write('\n' + str(content))
    else:
        print("Invalid option")
    return None
