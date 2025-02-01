# Python Data Processing Utilities

This repository contains three Python programs designed to process numerical and textual data, perform computations, and save results to files.

## Features

Each program reads data from a file, processes it accordingly, displays the output in the console, and saves the results to a text file.

### 1. Statistical Analysis
**Reads numerical data from a file.**  
Computes and displays statistical measures:
- Count
- Mean
- Median
- Mode
- Standard Deviation
- Variance  
- Saves results to an output file.

### 2. Number Conversion
**Reads decimal numbers from a file.**  
Converts them to:
- Binary
- Hexadecimal  
- Saves results to an output file.

### 3. Word Frequency Analysis
**Reads a text file.**  
- Counts occurrences of each word.  
- Reports errors if necessary.  
- Displays the word count results.  
- Saves results to an output file.

## Usage

Ensure you have Python installed before running any of the scripts. Each script reads input data from a predefined file and generates an output file.

```bash
python computeStatistics.py fileWithData.txt
python convertNumbers.py fileWithData.txt
python wordCount.py fileWithData.txt
```

## Requirements

Python 3.x

