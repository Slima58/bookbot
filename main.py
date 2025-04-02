
from stats import get_book_text, get_character_dict
import sys


def report(file_path):
    """Getting characters and  """
    nw = get_book_text(file_path)
    ld = get_character_dict(file_path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {nw} total words ")
    print("--------- Character Count -------")
    for k, v in ld.items():
        print(f"{k}: {v}")
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        report(sys.argv[1])
