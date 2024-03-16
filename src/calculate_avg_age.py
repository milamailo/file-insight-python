"""Calculate the average age of the employees based on the current day"""
from datetime import datetime

def calculate_avg_age(employees):
    """ Calculate the average age. """
    # Get today's date
    today = datetime.today()
    # Initialize total_age to calculate the sum of ages
    total_age = 0
    # Get the number of employees
    num_employees = len(employees)
    # Loop through each employee to calculate their age and add it to the total_age
    for employee in employees:
        # Convert the employee's date of birth from string to datetime object
        birth_date = datetime.strptime(employee['date_of_birth'], '%Y-%m-%d')
        # Calculate the age of the employee
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day))
        # Add the age to the total_age
        total_age += age
    # Calculate the average age
    avg_age = total_age / num_employees
    return avg_age
