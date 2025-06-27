import sys
from stats import word_count
from stats import char_count
from stats import sort_list

def get_book_text(filepath):
    book_contents = ""
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = f"{sys.argv[1]}"
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ------------")
    print(word_count(book_text))
    print("--------- Character Count ---------")
    for each_letter in sort_list(char_count(book_text)):
        if each_letter["char"].isalpha():
            print(f'{each_letter["char"]}: {each_letter["num"]}')
    print("============= END ===============")
main()