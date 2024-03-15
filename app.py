"""
FileInsight:
It is a versatile file analysis tool that enables users to effortlessly 
calculate the sum and average of numerical data within text files, 
facilitating deeper insights into the underlying data trends.
Main
"""

# Importing necessary functions from custom modules
import os
import src.sum as sum_file
import src.avg as avg_file
import src.str_to_list as cfl
import src.read_write_to_file as rwtf

def main_menu():
    """Printing the choice to select"""
    print("Main Menu:")
    print("1. SUM & AVG")
    print("0. Exit")

def clear_screen():
    """Function to clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """File analysis and statistics"""
    read = "read"
    write = "write"
    filename = './data/int_num.txt'

    # Reading content from the file
    content = rwtf.read_write_file(filename, read)

    # Converting string to list of numbers
    numbers = cfl.convert_file_list(content)


    while True:
        # Clear screen and call main_menu to print the option
        clear_screen()
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            # Calculating sum and average of the numbers
            file_total_sum = sum_file.sum_file(numbers)
            file_avg = avg_file.avg_file(numbers)

            # Printing numbers, sum, and average
            print("numbers: ", numbers)
            print("Sum of numbers: ", file_total_sum)
            print("Average of numbers: ", file_avg)

            # Writing sum and average back to the file
            rwtf.read_write_file(filename, write, f"Sum of numbers: {file_total_sum}" +
                                 f" and Avg: {file_avg}  \nList of numbers: {numbers}")
            print()
            input("Please hit any key to back to menu.")

        elif choice == '0':
            clear_screen()
            print("Exiting program...")
             # Exit the loop and end the program
            break
        else:
            clear_screen()
            print("Invalid choice. Please try again.")
            print()
            input("Please hit any key to back to menu.")


if __name__ == "__main__":
    main()
