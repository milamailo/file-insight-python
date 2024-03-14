import src.sum as sum_file

def main():
    filename = './data/int_num.txt'
    option = 'read'
    content = sum_file.read_write_file(filename, option)
    numbers = sum_file.convert_file_list(content)
    total_sum = sum_file.sum_file(numbers)
    print("Sum of numbers:", total_sum)

    option = 'write'
    sum_file.read_write_file(filename, option, total_sum)

if __name__ == "__main__":
    main()
