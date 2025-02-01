"""
This program reads decimal numbers from a file, converts them to
binary and hexadecimal representations, displays the results in
the console, and saves them to a text file.
"""

import sys
import time


def decimal_to_binary(n):
    """Converts a decimal integer to its binary string representation."""
    if n == 0:
        return '0'
    binary = []
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary_str = ''.join(reversed(binary))
    return '-' + binary_str if is_negative else binary_str


def decimal_to_hex(n):
    """Converts a decimal integer to its hexadecimal string representation."""
    if n == 0:
        return '0'
    hex_chars = '0123456789ABCDEF'
    hex_digits = []
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        remainder = n % 16
        hex_digits.append(hex_chars[remainder])
        n //= 16
    hex_str = ''.join(reversed(hex_digits))
    return '-' + hex_str if is_negative else hex_str


def process_file(input_filename):
    """Processes the input file and generates conversion results."""
    start_time = time.time()
    results = []
    error_count = 0

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                raw_line = line.strip()
                if not raw_line:
                    continue

                try:
                    number = int(raw_line)
                except ValueError:
                    print(
                        f"Error in line {line_num}: Invalid data '{raw_line}', "
                        "skipping."
                    )
                    error_count += 1
                    continue

                binary = decimal_to_binary(number)
                hexa = decimal_to_hex(number)
                results.append((number, binary, hexa))
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        sys.exit(1)
    except IOError as e:
        print(f"File error: {e}")
        sys.exit(1)

    output_lines = ["Number\tBinary\tHexadecimal"]
    for number, bin_num, hex_num in results:
        output_lines.append(f"{number}\t{bin_num}\t{hex_num}")

    elapsed_time = time.time() - start_time
    time_str = f"\nExecution time: {elapsed_time:.6f} seconds"
    output_lines.append(time_str)

    print('\n'.join(output_lines))
    with open("ConversionResults.txt", 'w', encoding='utf-8') as out_file:
        out_file.write('\n'.join(output_lines))

    return elapsed_time, error_count


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Example of how to use: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)
