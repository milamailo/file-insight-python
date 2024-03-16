""" Parse the employee data from the list of string and return a list of dictionaries. """
def parse_employee_data(lines):
    """Convert the string to Dict """
    headers = lines[1].strip().split(',')
    employees = []
    for line in lines[2:]:
        employee_info = line.strip().split(',')
        employee = dict(zip(headers, employee_info))
        employees.append(employee)
    return employees
