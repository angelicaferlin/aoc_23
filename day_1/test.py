def parse_line(input_string):
    # Define a mapping of letters to digits
    letter_to_digit = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    result = []
    current_number = ''

    for char in input_string:
        if char in letter_to_digit:
            current_number += letter_to_digit[char]
        else:
            # Check for cases where a letter is both the end and the start of a number
            if current_number:
                result.append(int(current_number))
                current_number = ''

    # Add the last number if any
    if current_number:
        result.append(int(current_number))

    return result

# Example usage
input_line = "eightwothree"
result = parse_line(input_line)
print(result)


