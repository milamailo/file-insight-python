"""Calculate the average age of the employees based on the current day"""
from datetime import datetime

def calculate_avg_age(employees):
    """ Calculate the average age. """
    today = datetime.today()
    total_age = 0
    num_employees = len(employees)
    for employee in employees:
        birth_date = datetime.strptime(employee['date_of_birth'], '%Y-%m-%d')
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day))
        total_age += age
    avg_age = total_age / num_employees
    return avg_age
