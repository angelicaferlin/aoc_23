import re
import re

pattern = r'^\d+$'

def read_file(file_path):
    """
    Reads a file and calculates the sum of the first and last integers in each line.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        int: The sum of the first and last integers in each line.
    """
    sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            num = extract_first_last_int_from_line(line)
            sum += num        
    return sum

def extract_first_last_int_from_line(line: str):
    """
    Extracts the first and last integers from a line.

    Args:
        line (str): The line to extract the integers from.

    Returns:
        int: The sum of the first and last integers in the line.
    """
    list_of_ints = []
    for var in line:
       
        if re.match(pattern, var):
            list_of_ints.append(var)

    if len(list_of_ints) > 1:
        return int(list_of_ints[0] + list_of_ints[-1])
    if len(list_of_ints) == 1:
        return int(list_of_ints[0] + list_of_ints[0])
    else:
        return 0

if __name__ == '__main__':
    print(read_file('test_data.txt'))



