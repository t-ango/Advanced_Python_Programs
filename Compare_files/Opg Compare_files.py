"""
Word Comparison Between Two Files

This program reads two text files, extracts their unique words, and performs set operations to analyze word differences and similarities.

Functions:
    - readfile(filename): Reads words from a file and returns them as a list.
    - main(): Compares the unique words in two files and displays results for:
        - Union of words (unique words in both files).
        - Intersection of words (words common to both files).
        - Difference (words in one file but not the other).
        - Symmetric difference (words unique to each file).

Usage:
    - Place two text files in the same directory as the script, named "Test.txt" and "Test_2.txt".
    - Run the program to see the analysis results.

Example Output:
    Total unique words in both files: 15
    Words in both files: {'word1', 'word2'}
    Words only in the first file: {'unique1'}
    Words only in the second file: {'unique2'}
    Words in either file but not both: {'unique1', 'unique2'}
"""

import os.path

def readfile (filename):
    filelist = []
    if os.path.isfile(filename):
        with open (filename, "r") as inputfile:
            try: 
                filelist = inputfile.read().split()
            except Exception as e:
                print ("Error loading file: {e}") 
    else: 
        print("File not found")
    return filelist  

def main():

    #file_1 = input("Enter file one: ")
    #file_2 = input("Enter file two: ")

    set_1 = set(readfile("Test.txt"))
    set_2 = set(readfile("Test_2.txt"))

    print ("Antall olike ord i begge filer: ", len(set_1.union(set_2)))
    print ("Alle unike ord i begge filer: ", set_1|set_2 )
    print ("Alle unike ord som forekommer både i første og andre fil: ", set_1&set_2)
    print ("Alle unike ord som forekommer i første fil, men ikke i andre: ", set_1.difference(set_2))
    print ("Alle unike ord som forekommer i andre fil, men ikke i første: ", set_2 - set_1)
    print ("Alle ord som forekommer enten i første eller andre, men ikke i begge: ", set_1^set_2)

main()






