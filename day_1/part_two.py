import re


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
            new_line = replace_numbers(line)
            num = extract_first_last_int_from_line(new_line)
            sum += num
    print(sum)       
    return sum


pattern = r'^\d+$'


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


def replace_numbers(line):
        """
        Replaces all instances of numbers in a line with the first letter of the number + the actual digit + the last letter of the number.

        Args:
            line (str): The line to replace numbers in.

        Returns:
            str: The line with numbers replaced.
        """
        word_to_number = {
            'one': 'o1e',
            'two': 't2o',
            'three': 't3e',
            'four': 'f4r',
            'five': 'f5e',
            'six': 's6x',
            'seven': 's7n',
            'eight': 'e8t',
            'nine': 'n9e'
        }

        for word, replacement in word_to_number.items():
            line = line.replace(word, replacement)
        return line

if __name__ == "__main__":
    # Add your code here
    read_file("test_data.txt")
    #replace_numbers("eightwothree")

