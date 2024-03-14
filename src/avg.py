
def read_write_file(filename, option, content=None):
    if option == 'read':
        with open(filename, 'r') as file:
            content = file.readline()
        return content
    elif option == 'write':
        with open(filename, 'a') as file:
            file.write('\n' + str(content))
    else:
        print("Invalid option")



def avg_file(lst):
    return sum(map(int, lst)) / len(lst)