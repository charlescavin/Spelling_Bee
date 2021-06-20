# All file operations required for sb word list processing
import sys, os, csv
from datetime import date, timedelta
from get_sb_path import get_sb_path
from utils import get_solve_date


def get_sb_wordlist_filename():
    return get_sb_path() + "sb_wordlist.txt"


def read_sb_wordlist():

    filename = get_sb_wordlist_filename()
    if not os.path.isfile(filename):
        raise FileNotFoundError(
            "The Spelling Bee wordlist file", filename, "does not exist."
        )
        return

    sb_wordlist = []
    with open(get_sb_wordlist_filename(), "r") as file:
        for word in file:
            # Remove newline characters on each line and save the list
            word = word[:-1]
            sb_wordlist.append(word)
    return sb_wordlist, len(sb_wordlist)


def write_sb_wordlist(sb_wordlist):
    with open(get_sb_wordlist_filename(), "w") as file:
        # Add newline characters on each line of the list and save the file
        sb_wordlist_len = len(sb_wordlist)
        sb_wordlist = list(map(lambda x: x + "\n", sb_wordlist))
        file.writelines(sb_wordlist)

    return sb_wordlist_len


def read_sb_solution_wordlist(iso_date):
    filename = get_sb_path() + "solutions/solution-" + iso_date + ".csv"
    if not os.path.isfile(filename):
        raise FileNotFoundError(
            "The solution wordlist file", filename, "does not exist."
        )
        return

    solution_wordlist = []
    try:
        with open(filename, newline="", encoding="utf-8-sig") as csvfile:
            csv_reader = csv.reader(csvfile, dialect="excel")
            for word in csv_reader:
                print("word[0]:", word[0])
                solution_wordlist.append(word[0])
    except:
        print("Could not open solution wordlist:", filename)
    return solution_wordlist


def write_found_wordlist(found_words_filename, found_words):
    with open(found_words_filename, "w") as fw_file:
        found_words = list(map(lambda w: w + "\n", found_words))
        fw_file.writelines(found_words)


def read_found_wordlist(iso_date):
    filename = get_sb_path() + "words_found/wf-" + iso_date + ".txt"

    if not os.path.isfile(filename):
        raise FileNotFoundError("The found words file", filename, "does not exist.")
        return

    found_words = []
    with open(filename, "r") as fw_file:
        words = fw_file.readlines()
        words = words[1:]
        found_words = list(map(lambda w: w.rstrip(), words))
        print("found_words:", found_words)
    return found_words
