def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def words_in_string(text):
    count = 0
    words = text.split()

    for word in words:
        count += 1

    return count

def print_words_found():
    book_string = get_book_text("books/frankenstein.txt")
    word_count = words_in_string(book_string)

    print(f"{word_count} words found in the document")


def main():
    print_words_found()


main()