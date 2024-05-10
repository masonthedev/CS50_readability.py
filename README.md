# CS50_readability.py

This is an updated implementation of a program I previously wrote that took a body of text from the user and used coleman-liau index to determine its associated reading level. This implementation uses Python.

# Text Analyzer

This Python program analyzes text input and calculates the approximate reading grade level based on the Coleman-Liau index.

## Description

This program takes user input and calculates the reading level required to understand the text. It counts the number of letters, words, and sentences in the input text, then uses the Coleman-Liau index formula to estimate the grade level required to understand the text.

## Getting Started

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run the program by executing `python text_analyzer.py`.

## Usage

1. Run the program.
2. Enter the text when prompted.
3. The program will output the estimated reading grade level required to understand the text.

## Example

python readability.py
Text: This is a sample text. It contains multiple sentences and some punctuation marks!

Grade 5


License
This project is licensed under the MIT License.
