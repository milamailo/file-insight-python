def read_write_file(filename, option, content=None):
    if option == 'read':
        with open(filename, 'r') as file:
            content = file.readline()
            file.close()
        return content
    elif option == 'write':
        with open(filename, 'a') as file:
            file.write('\n' + str(content))
            file.close()
    else:
        print("Invalid option")