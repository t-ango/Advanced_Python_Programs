"""
Word Sorting and Organization from File (14.3)

This program reads a text file, processes its contents by removing punctuation, and organizes the unique words into a dictionary sorted alphabetically by their first letter.

Functions:
    - readfile(filename): Reads words from a file into a list.
    - replace_punctuation(some_list): Removes punctuation from words in a list.
    - sort_list_into_dict(mylist): Sorts unique words into a dictionary based on their first letter.
    - print_sorted_dict(word_dict): Displays the dictionary in an organized format.

Usage:
    - Enter the filename of a text file when prompted.
    - The program will display the sorted dictionary of unique words.
"""

import os
import pickle

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

def sort_list_into_dict(mylist):
    word_dictionary = {}
    unique_words = set(word.lower() for word in mylist)
    for item in unique_words:
        if isinstance(item,str):
            initial = item[0].lower()
            if item not in word_dictionary:
                word_dictionary[item] = initial
    return word_dictionary


def print_sorted_dict(word_dict):
    prev_initial = None
    for word, initial in sorted(word_dict.items()):
        if initial != prev_initial:
            if prev_initial is not None:
                print()
            print (f"\t{initial}:", end='')
            prev_initial = initial
        print (f"\n\t   {word}", end="\t")
    print()

def replace_punctuation(some_list):
    modified_list = []
    for word in some_list:
        modified_word = ''.join(ch for ch in word if ch not in "!\"#€%&/()=?`*^¨'_:;,.->>°§")
        modified_list.append(modified_word)
    return modified_list

def main ():

    new_file = input("Enter file name (e.g: 'filename.txt'): ")
    new_list = readfile(new_file)
    new_list = replace_punctuation(new_list)
    new_dict = sort_list_into_dict(new_list)
    print_sorted_dict(new_dict)

main()








