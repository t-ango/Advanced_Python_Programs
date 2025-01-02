# Huffman Coding: Encoding and Decoding

This program implements Huffman coding to compress text by encoding characters into variable-length binary codes based on their frequencies. It also includes functionality to decode the binary string back into the original text.

## Features
- Builds a Huffman tree from character frequencies.
- Encodes input text into a binary string.
- Decodes the binary string back into the original text.

## Usage
1. Run the program:
   ```bash
   python Huffman decode.py
Enter a text string when prompted.
The program will display:
Character frequencies.
Huffman codes for each character.
Encoded binary string.
Decoded original text.
Example:

Enter a text: hello
ASCII Code    Character      Frequency      Code       
104           h              1              00         
101           e              1              01         
108           l              2              1          
111           o              1              10         
Encoded Text: 00011011010
Decoded Text: hello
Requirements

Python 3.x
