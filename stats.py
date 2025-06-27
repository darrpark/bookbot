def word_count(text):
    num_words = 0
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def char_count(text):
    letter_count = dict()
 #   lower_text = text.lower()
 #   words = lower_text.split()
 #   for word in words:
    for letter in text.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on(item):
    return item["num"]

def sort_list(text_count):
    sortable_dict = []
    for letter, count in text_count.items():
        item = {"char": letter, "num": count}
        sortable_dict.append(item)

    sortable_dict.sort(reverse=True, key=sort_on)
    
    return sortable_dict