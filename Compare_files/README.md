# Word Comparison Between Two Files

This program compares the unique words in two text files using Python's set operations. It provides insights into shared and unique words across the files.

## Features

- Reads and processes two text files.
- Computes:
  - Total unique words in both files.
  - Words common to both files.
  - Words unique to each file.
  - Words in either file but not both.

## Usage

1. Place two text files named `Test.txt` and `Test_2.txt` in the same directory as the script.
2. Run the program:
   ```bash
   python word_comparison.py
The program will output:
Total unique words.
Common words.
Words unique to each file.
Words in either file but not both.
Example Output

For two files containing the following words:

Test.txt: apple banana cherry
Test_2.txt: banana cherry date
The program will output:

Total unique words in both files: 4
Words in both files: {'banana', 'cherry'}
Words only in the first file: {'apple'}
Words only in the second file: {'date'}
Words in either file but not both: {'apple', 'date'}

Twi files with example text are provided in the folder 

Requirements

Python 3.x
