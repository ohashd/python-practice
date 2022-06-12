import sys

def trim_whitespace(string):
    scan_index = 0
    trimmed_index = 0

    # Scan to first non blank character
    while scan_index < len(string) and string[scan_index] == ' ':
        scan_index += 1


    while scan_index < len(string):

        # Copy over all non whitespace characters
        while scan_index < len(string) and string[scan_index] != ' ':
            string[trimmed_index] = string[scan_index]
            scan_index += 1
            trimmed_index += 1

        # Scan to next first non blank character (or end of line)
        while scan_index < len(string) and string[scan_index] == ' ':
            scan_index += 1

        # If scan led to non blank character, add a space
        if scan_index < len(string):
            string[trimmed_index] = ' '
            trimmed_index += 1

    # Remove remaining space not used
    initial_length = len(string)
    for _ in range(trimmed_index, initial_length):
        string.pop()

def reverse(string, start_index, end_index):
    while (start_index < end_index):
        tmp = string[start_index]
        string[start_index] = string[end_index]
        string[end_index] = tmp
        start_index += 1
        end_index -= 1

def reverse_word_order(line):
    trim_whitespace(line)
    length = len(line)
    reverse(line, 0, length - 1)
    scan_index = start_index = 0

    while scan_index < length:
        scan_index += 1
        if scan_index >= length or line[scan_index] == " ":
            end_index = scan_index - 1
            reverse(line, start_index, end_index)
            scan_index = start_index = end_index + 2
    return line


if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    for input_line in input_lines:
        soln = reverse_word_order(list(input_line))
        print("".join(soln))
