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
import src.parse_employee_data as emp_list
import src.calculate_avg_age as emp_avg_age

def main_menu():
    """Printing the choice to select"""
    print("Main Menu:")
    print("1. SUM & AVG")
    print("2. Employees avg age")
    print("0. Exit")

def clear_screen():
    """Function to clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """File analysis and statistics"""
    read = "read"
    write = "write"
    all_lines = "all_lines"
    filename_num = './data/int_num.txt'
    filename_emp = './data/employees_list.txt'


    while True:
        # Clear screen and call main_menu to print the option
        clear_screen()
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            # Reading content from the file
            content = rwtf.read_write_file(filename_num, read)
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
            rwtf.read_write_file(filename_num, write, f"Sum of numbers: {file_total_sum}" +
                                 f" and Avg: {file_avg}  \nList of numbers: {numbers}")
            print()
            input("Please hit any key to back to menu.")

        elif choice == '2':
            clear_screen()
            # Read data from file
            lines = content = rwtf.read_write_file(filename_emp, all_lines)
            # Parse employee data
            employees = emp_list.parse_employee_data(lines)
            # Calculate average age
            avg_age = emp_avg_age.calculate_avg_age(employees)
            print("Average age of employees:", avg_age)
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
