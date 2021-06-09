import sys, bisect
from file_ops import read_sb_wordlist, write_sb_wordlist


def add_words(words_to_add):

    sb_wordlist = read_sb_wordlist()

    # Add words if they aren't in the sb word list
    ctr = 0
    for word in words_to_add:
        if word in sb_wordlist:
            continue
        else:
            bisect.insort(sb_wordlist, word)
            print("Word added:", word)
            ctr += 1

    print("\n", ctr, "words added.")
    write_sb_wordlist(sb_wordlist)


def main(argv):

    sb_wordlist = read_sb_wordlist()
    words_to_add = argv

    add_words(words_to_add)


if __name__ == "__main__":
    main(sys.argv[1:])
    print("argv:", sys.argv[1:])
