"""
FileInsight:
It is a versatile file analysis tool that enables users to effortlessly 
calculate the sum and average of numerical data within text files, 
facilitating deeper insights into the underlying data trends.
Main
"""

# Importing necessary functions from custom modules
import src.sum as sum_file
import src.avg as avg_file
import src.str_to_list as cfl
import src.read_write_to_file as rwtf


def main():
    """File analysis and statistics"""

    # File path
    filename = './data/int_num.txt'

    # Reading content from the file
    option = 'read'
    content = rwtf.read_write_file(filename, option)

    # Converting string to list of numbers
    numbers = cfl.convert_file_list(content)

    # Calculating sum and average of the numbers
    file_total_sum = sum_file.sum_file(numbers)
    file_avg = avg_file.avg_file(numbers)

    # Printing numbers, sum, and average
    print("numbers: ", numbers)
    print("Sum of numbers: ", file_total_sum)
    print("Average of numbers: ", file_avg)

    # Writing sum and average back to the file
    option = 'write'
    rwtf.read_write_file(filename, option, f"Sum of numbers: {file_total_sum}" +
                         f" and Avg: {file_avg}  \nList of numbers: {numbers}")

if __name__ == "__main__":
    main()
