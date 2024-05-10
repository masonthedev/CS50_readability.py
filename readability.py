from cs50 import get_string

# Prompt the user for a text.
text = get_string("Text: ")

# Initialize counters for letters, words, and sentences to 0.
letters = 0
words = 0
sentences = 0

# For each character in the text:
for i in range(len(text)):
    # If char is alphabetical, increment letters
    if text[i].isalpha():
        letters += 1
    # If char is a space, increment words
    if i > 0 and text[i] == ' ' and text[i - 1] != ' ':
        words += 1
    # If char is punctuation increment sentences.
    if text[i] in ".!?":
        sentences += 1
    # Handle the last word
if text[-1].isalpha() or " ":
    words += 1

# Calculate the average number of letters per 100 words.
l = letters / words * 100

# Calculate the average number of sentences per 100 words.
s = sentences / words * 100

# Use the Coleman-Liau index to calculate the grade level.
index = round(0.0588 * l - 0.296 * s - 15.8)

# Print the grade level.
if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(index)}")

print(letters)
print(words)
print(sentences)
