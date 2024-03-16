""" Parse the employee data from the list of string and return a list of dictionaries. """
def parse_employee_data(lines):
    """Convert the string to Dict """
    # Extracting the headers from the second line of the input
    headers = lines[1].strip().split(',')
    # Initializing an empty list to store dictionaries for each employee
    employees = []
    # Iterating through the lines starting from the third line (index 2)
    for line in lines[2:]:
        # Splitting the line into individual pieces of employee information
        employee_info = line.strip().split(',')
        # Creating a dictionary mapping each header to its corresponding piece of information
        employee = dict(zip(headers, employee_info))
        # Adding the dictionary representing the current employee to the list
        employees.append(employee)
    return employees
