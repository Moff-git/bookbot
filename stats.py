def count_words(book):
    split_words = book.split()
    word_count = 0
    for words in split_words:
        word_count += 1
    return word_count

def count_letters(book):
    letters_counted = {}
    book = book.lower()
    for letter in book:
        if letter not in letters_counted:
            letters_counted[letter] = 1
        else:
            letters_counted[letter] += 1
    return letters_counted

def sort_letters(letter_count):
    list_of_letters =[]
    for letter, value in letter_count.items():
        list_of_letters.append({"char": letter, "num": value})
    def get_letters_counted_value(dict_item):
        return dict_item["num"]
    list_of_letters.sort(key = get_letters_counted_value, reverse = True)
    return list_of_letters