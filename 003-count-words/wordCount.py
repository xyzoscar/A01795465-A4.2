"""
This program reads a text file, counts the occurrences of each word,
reports errors, displays the results in the console, and saves them
to a text file
"""

import sys
import time


def count_words(filename):
    """Count occurrences of each word in a given text file and report errors"""
    word_counts = {}
    error_count = 0
    total_lines = 0
    start_time = time.time()

    try:
        with open(filename, 'rb') as file:
            for line_num, line in enumerate(file, 1):
                total_lines += 1
                try:
                    line_str = line.decode('utf-8').strip()
                except UnicodeDecodeError as e:
                    print(f"Error in line {line_num}: "
                          f"Unable to decode - {str(e)}")
                    error_count += 1
                    continue

                words = line_str.split()
                for word in words:
                    if word:
                        word_counts[word] = word_counts.get(word, 0) + 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist")
        sys.exit(1)
    except IOError as e:
        print(f"Error opening file: {str(e)}")
        sys.exit(1)

    elapsed_time = time.time() - start_time
    sorted_words = sorted(
        word_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )
    results = [f"{word}: {count}" for word, count in sorted_words]
    summary = (
        f"\nTotal lines analyzed: {total_lines}\n"
        f"Total errors encountered: {error_count}\n"
        f"Time elapsed: {elapsed_time:.4f} seconds"
    )

    with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write('\n'.join(results) + summary)

    print('\n'.join(results))
    print(summary)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Example of how to use: python wordcount.py fileWithData.txt")
        sys.exit(1)

    count_words(sys.argv[1])
