# Spelling Bee
A small project to make life more interesting.

The modules here are to establish and manage a word list that conforms to the solutions given in the New York Times Spelling Bee games. The starting point was a large word list from http://www-personal.umich.edu/~jlawler/wordlist.html. Given the letters provided for each game, find_words.py will find every word in the sb_wordlist.txt file that uses those letters, including the required letter. To keep the word list current, refine_word_list compares the solutions (given the next day) with what is in sb_wordlist.txt and adds or removes words as necessary.
