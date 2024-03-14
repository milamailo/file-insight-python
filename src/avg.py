"""Avg"""
def avg_file(lst):
    """Calculate the average of a list of numbers"""
    # Calculate the sum of the integers
    total_sum = sum(lst)

    # Calculate the average by dividing the sum by the length of the list
    average = total_sum / len(lst)

    return average
