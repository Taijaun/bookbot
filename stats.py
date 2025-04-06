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

    return word_count

def times_char_occurs(text):
    occurence = {}

    for char in text:
        if char.lower() not in occurence:
            occurence[char.lower()] = 1
        else:
            occurence[char.lower()] += 1

    return occurence

def char_occurs():
    text = get_book_text("books/frankenstein.txt")
    return times_char_occurs(text)

# take in 1 dictionary
# return sorted list of dictionaries
# dictionary should be
# {character: "e",
#      count: 5}
# sort from largest to smallest count

def sort_on(dict):
    return dict["count"]

def sorted_dict():
    dicts_count = char_occurs()

    sorted_dicts = []

    for letter in dicts_count:
        sorted_dicts.append({"char": letter, "count": dicts_count[letter]})
    
    sorted_dicts.sort(reverse=True, key=sort_on)


    return sorted_dicts

def formatted_report():
    list = sorted_dict()

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {print_words_found()}")
    print("--------- Character Count -------")

    for i in list:
        print(f"{i["char"]}: {i["count"]}")
    
    print("============= END ===============")