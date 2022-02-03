# https://www.chegg.com/homework-help/questions-and-answers/problem-1-score-dictionary-assignment-create-new-file-called-sentimentpy-code-defined-file-q67019619
import string


def load_score_dict(file="sentiment.txt"):
    myfile = open(file, 'r')
    score_dict = dict()
    for line in myfile.readlines():
        if len(line.strip()) != 0:
            if line.strip()[0] != "#":
                word, score = line.strip().split()
                score = float(score)
                score_dict[word] = score
    return score_dict


# https://www.chegg.com/homework-help/questions-and-answers/problem-2-word-retrieval-write-function-called-getwords-takes-single-argument-string-repre-q67019720
def get_words(my_sentence):
    for i in string.punctuation:
        my_sentence = my_sentence.replace(i, "")
    my_sentence = my_sentence.lower()
    my_sentence = my_sentence.strip().split()
    my_sentence = list(set(my_sentence))
    return my_sentence


def score_sentence(my_sentence, file="sentiment.txt"):
    words = get_words(my_sentence)
    scores = load_score_dict(file)
    score = 0
    for i in words:
        if i in scores:
            if i.isalpha():
                score += scores[i]
    return score


if __name__ == '__main__':
    print(load_score_dict())
    print(get_words("zoftig zoftig"))
    print(score_sentence("zymotic zymosis zoster", "sentiment.txt"))
