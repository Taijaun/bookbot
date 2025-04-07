import sys

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

def print_words_found(filepath):
    book_string = get_book_text(filepath)
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

def char_occurs(filepath):
    text = get_book_text(filepath)
    return times_char_occurs(text)

# take in 1 dictionary
# return sorted list of dictionaries
# dictionary should be
# {character: "e",
#      count: 5}
# sort from largest to smallest count

def sort_on(dict):
    return dict["count"]

def sorted_dict(filepath):
    dicts_count = char_occurs(filepath)

    sorted_dicts = []

    for letter in dicts_count:
        sorted_dicts.append({"char": letter, "count": dicts_count[letter]})
    
    sorted_dicts.sort(reverse=True, key=sort_on)


    return sorted_dicts

def formatted_report(filepath):
    list = sorted_dict(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {print_words_found(filepath)} total words")
    print("--------- Character Count -------")

    for i in list:
        print(f"{i["char"]}: {i["count"]}")
    
    print("============= END ===============")