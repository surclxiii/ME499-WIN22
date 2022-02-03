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


if __name__ == '__main__':
    print(load_score_dict())