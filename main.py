def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    split_words = book.split()
    word_count = 0
    for words in split_words:
        word_count += 1
    print (f"{word_count} words found in the document")
    return word_count

def main():
    count_words(get_book_text("books/frankenstein.txt"))

main()