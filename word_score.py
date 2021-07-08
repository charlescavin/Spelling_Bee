# Calculate the score for each word
# 4 letter word = 1 pt
# For a word longer than 4 letters:
#    1 pt for each letter
#    A 5 letter word receives 5 pts.
# Panagrams receive 7 extra pts.


def get_word_points(word, letters):
    word_len = len(word)
    if word_len == 4:
        points = 1
    else:
        points = word_len
    if is_panagram(word, letters):
        points += 7
    return points


def is_panagram(word, letters):
    for letter in letters:
        if letter not in word:
            return False
    return True


def get_total_points(word_list, letters):
    total_points = 0
    for word in word_list:
        word_points = get_word_points(word, letters)
        total_points += word_points
        print("points for:", word, "=", word_points)
    print("Total points =", total_points)


word_list = [
    "accord",
    "acid",
    "acidic",
    "acrid",
    "arcadia",
    "ardor",
    "card",
    "cardiac",
    "cardio",
    "cardioid",
    "carload",
    "cicada",
    "clad",
    "clod",
    "coda",
    "codicil",
    "cold",
    "collard",
    "colloid",
    "cord",
    "cordial",
    "corridor",
    "dial",
    "dildo",
    "dill",
    "dodo",
    "doll",
    "dollar",
    "dolor",
    "doodad",
    "door",
    "drill",
    "droid",
    "droll",
    "drool",
    "idol",
    "laid",
    "lard",
    "load",
    "lord",
    "odor",
    "radar",
    "radial",
    "radical",
    "radio",
    "railroad",
    "road",
    "rood",
]

letters = "draiocl"
# test_words = ["clod", "collard", "cordial"]

get_total_points(word_list, letters)
