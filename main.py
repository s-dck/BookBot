import sys
from stats import get_num_characters, get_num_words, print_report


def get_book_text(path_to_file):
    with open(path_to_file, "r") as f:
        return f.read()

def __main__():
    if(len(sys.argv)!=2):
        print("Usage: python3 main.py <path_to_book")
        sys.exit(1)
    else: 
        path = sys.argv[1]

        

    file_content = get_book_text(path)
    print_report(file_content)
    

__main__()

