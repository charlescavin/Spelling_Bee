import sys, os
from datetime import date
from utils import find_words
from get_sb_path import get_sb_path
from file_ops import read_sb_wordlist, write_found_wordlist


def main(argv):

    letters = argv
    sb_path = get_sb_path()
    today = date.today().isoformat()
    found_words_filename = sb_path + "words_found/wf-" + today + ".txt"

    try:
        sb_wordlist, len_sb_wordlist = read_sb_wordlist()
    except FileNotFoundError:
        return

    print("Number of words in dictionary:", len_sb_wordlist, "\n")

    found_words = find_words(letters, sb_wordlist)
    found_words_len = len(found_words)
    print("Found Words")
    print("===========")
    print(found_words)
    # for word in found_words:
    #    print(word)

    # Prevent overwriting the found words file
    if os.path.isfile(found_words_filename) is not True:
        write_found_wordlist(found_words_filename, found_words)
    else:
        print("\n", found_words_filename, "already exists.")


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        main("bhliyte")

    # print("argv:", sys.argv[1])
