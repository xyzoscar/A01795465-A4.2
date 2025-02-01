"""
This program reads numerical data from a file, computes statistical measures
(count, mean, median, mode, standard deviation, variance), displays results
in the console, and saves them to a text file.
"""

import sys
import time


def compute_statistics(filename):
    """
    Computes statistical measures from numerical data in a file

    Args:
        filename (str): Path to the file containing numerical data

    Returns:
        None: Results are printed and saved to a file
    """
    start_time = time.time()
    numbers = []
    error_count = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                try:
                    num = float(stripped_line)
                    numbers.append(num)
                except ValueError:
                    error_msg = (
                        f"Error in line {line_num}: "
                        f"Invalid data '{stripped_line}'"
                    )
                    print(error_msg)
                    error_count += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except (IOError, OSError) as error:
        print(f"Error reading file: {error}")
        sys.exit(1)

    if not numbers:
        print("No valid data found in the file")
        sys.exit(1)

    count = len(numbers)
    mean = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    mid_index = count // 2
    if count % 2 == 1:
        median = sorted_numbers[mid_index]
    else:
        median = (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2

    frequency = {}
    for num in sorted_numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_freq]

    if max_freq == 1:
        mode_str = "No mode"
    else:
        mode = min(modes) if len(modes) > 1 else modes[0]
        mode_str = f"{mode:.6f}"

    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = variance ** 0.5
    elapsed_time = time.time() - start_time

    results = (
        "Descriptive Statistics Results:\n"
        f"Valid data: {count}\n"
        f"Invalid data: {error_count}\n"
        f"Count: {count}\n"
        f"Mean: {mean:.6f}\n"
        f"Median: {median:.6f}\n"
        f"Mode: {mode_str}\n"
        f"Standard Deviation: {std_dev:.6f}\n"
        f"Variance: {variance:.6f}\n"
        f"Time elapsed: {elapsed_time:.6f} seconds\n"
    )

    print(results)
    with open("StatisticsResults.txt", "w", encoding='utf-8') as file:
        file.write(results)


def main():
    """Main function handling command line arguments."""
    if len(sys.argv) != 2:
        print("Example of how to use: python computeStatistics.py fileWithData.txt")
        sys.exit(1)
    compute_statistics(sys.argv[1])


if __name__ == "__main__":
    main()
