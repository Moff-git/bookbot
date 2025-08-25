from stats import count_words, count_letters, sort_letters
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    sorted_list = sort_letters(count_letters(get_book_text(sys.argv[1])))
    for char_and_count in sorted_list:
        if char_and_count["char"].isalpha():
            print (f"{char_and_count['char']}: {char_and_count['num']}")
    print("============= END ===============")

main()