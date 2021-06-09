import bisect
from datetime import date, timedelta


def find_words(letters, sb_wordlist):
    found_words = []
    found_words.append(letters)
    req_letter = letters[0]

    for word in sb_wordlist:

        # This test was dropped because words less than 4 characters
        # were removed from the wordlist.
        """
        # Is the word length 4 or greater?
        if len(word) < 4:
            continue
        """

        # Is the required letter in the word? If not, go to the next word.
        if req_letter not in word:
            continue

        # Every letter in the word must be in the list of supplied letters.
        for letter in word:
            if letter not in letters:
                found_word = False
                break
            else:
                found_word = True

        if found_word is True:
            found_words.append(word)

    return found_words


def deduce_letters_from_panagram(panagram):
    letters = []
    for letter in panagram:
        if letter not in letters:
            letters.append(letter)
    return letters


def unique_letters_in_word(word):

    letters = []
    for letter in word:
        if letter not in letters:
            letters.append(letter)
    return letters


def find_shortest_word_in_wordlist(wordlist):
    # Find the first word that is 4 characters long, or at
    # worst, the first 5 character word.
    for i in range(4, 6):
        for word in wordlist:
            if len(word) == i:
                return word


# From a list of words, determine what the unique letters
# are and what the required letter is.
def deduce_letters_from_wordlist(wordlist):

    letters = []
    for word in wordlist:
        for letter in word:
            if letter not in letters:
                letters.append(letter)
    return letters


def deduce_required_letter(wordlist):

    shortest_word = find_shortest_word_in_wordlist(wordlist)
    req_letters = unique_letters_in_word(shortest_word)
    wordlist.remove(shortest_word)

    first_word = True
    for word in wordlist:
        if first_word is True:
            req_letters = unique_letters_in_word(word)
            first_word = False
            continue
        else:
            unique_letters = unique_letters_in_word(word)
            for req_letter in req_letters:
                if req_letter not in unique_letters:
                    req_letters.remove(req_letter)
                if len(req_letters) == 1:
                    print("The required letter is:", req_letters[0])
                    return req_letters[0]

    if len(req_letters) > 1:
        return "Required letter not found."


# Add words from the word_list to the sb_wordlist if
# they aren't already there.
def add_words(sb_wordlist, word_list):

    added_words = []
    num_of_added_words = 0
    # Insert the new words if they aren't in the word list
    for word in word_list:
        if word not in sb_wordlist:
            bisect.insort(sb_wordlist, word)
            added_words.append(word)
            num_of_added_words += 1

    return sb_wordlist, added_words, num_of_added_words


# Remove words in the word_list from the sb_wordlist
def remove_words(sb_wordlist, words_to_remove):
    removed_words = []
    num_of_removed_words = 0
    for word in words_to_remove:
        if word in sb_wordlist:
            sb_wordlist.remove(word)
            removed_words.append(word)
            num_of_removed_words += 1
    return sb_wordlist, removed_words, num_of_removed_words


def get_solve_date(days_ago=1):
    td = timedelta(days_ago)
    solve_date = date.today() - td
    return solve_date.isoformat()

