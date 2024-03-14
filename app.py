import src.sum as sum_file
import src.avg as avg_file
import src.strToList as cfl
import src.readWriteToFile as rwtf

def main():
    filename = './data/int_num.txt'
    option = 'read'
    content = rwtf.read_write_file(filename, option)
    numbers = cfl.convert_file_list(content)
    print(numbers)
    total_sum = sum_file.sum_file(numbers)
    print("Sum of numbers:", total_sum)

    option = 'write'
    # sum_file.read_write_file(filename, option, f"Sum of numbers: {total_sum}")

    rwtf.read_write_file(filename, option, total_sum)

if __name__ == "__main__":
    main()
