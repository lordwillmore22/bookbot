from stats import count_words,count_chars,sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("The correct way of executing the program is")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    data = get_book_text(path)
    words = count_words(data)
    chars = count_chars(data)
    sorted_chars = sort_dict(chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict['char'].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


main()