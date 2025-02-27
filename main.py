import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
print(f"Processing book at: {book_path}")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text(book_path)
    word_count= count_words(text)
    letter_count = num_character(text)
    list_dict = sorted_list_dicts(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    alpha_sorted_list(list_dict)
    print("============= END ===============")
      #print(text)
main()