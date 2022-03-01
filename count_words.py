"""Counting the words in a file. """


def counted_words(filename):
    """Count the approximate words of a file. """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist. ")
    else:
        # Count the words of a file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words. ")

filename = ['alice.txt', 'goosebumps.txt', 'scarlet.txt', 'frankenstein.txt']

for file in filename:
    counted_words(file)