import string


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


if __name__ == '__main__':
    print(load_score_dict())
    print(get_words("zoftig zoftig"))
    word1 = "zygnema, zygophyllum, zyloprim"
    dict1 = {"zygnema": 1, "zygophyllum": 2, "zyloprim": -1}
    print(score_sentence(word1, dict1))
