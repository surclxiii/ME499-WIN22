import string
import sys


# https://docs.python.org/3/library/stdtypes.html#str.join
def load_score_dict(file="sentiment.txt"):
    # open file
    myfile = open(file, 'r')
    score_dict = dict()
    # Check for each line in file
    for line in myfile.readlines():
        # If line is not blank
        if len(line.strip()) != 0:
            # If line is not start with #
            if line.strip()[0] != "#":
                # Define word and score by strip and split
                word, score = line.strip().split()
                # Convert str to float
                score = float(score)
                # Save value to dict
                score_dict[word] = score
    return score_dict


# https://docs.python.org/3/library/string.html
def get_words(my_sentence):
    # Check each punctuation in my sentence
    for i in string.punctuation:
        # Replace with ""
        my_sentence = my_sentence.replace(i, "")
    # Convert to lower case then strip and split
    my_sentence = my_sentence.lower()
    my_sentence = my_sentence.strip().split()
    # Remove duplicate by set() then make it to list
    my_sentence = list(set(my_sentence))
    return my_sentence


# Work with Ittiwat
def score_sentence(my_sentence, scores):
    # Get unique word
    words = get_words(my_sentence)
    score = 0
    # Check if word is same in dict then add to the sum
    for key, value in scores.items():
        for word in words:
            if word == key:
                score += value
            else:
                score += 0
    return score


# Work with Ittiwat
if __name__ == '__main__':
    # To make CLI use sys
    try:
        with open(sys.argv[1], "r") as f:   # Open text file
            sentence = f.read()

    # Ask for filename input if not given
    except:
        with open(input("Input filename:"), "r") as f:
            sentence = f.read()
    score = score_sentence(sentence, load_score_dict())

    if score > 0:
        print("Positive")
    elif score < 0:
        print("Negative")
    else:
        print("Neutral")
