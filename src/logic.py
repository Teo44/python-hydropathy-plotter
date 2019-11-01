

def parse(seq, window_size):
    seq = list(seq)
    score = 0
    score_file = open("hydropathy_values.txt", "r")
    lines = score_file.readlines()
    values = dict()

    for i in range(len(lines)):
        line = lines[i].split()
        values[line[0]] = float(line[1])

    for i in range(window_size):
        score = score + values[seq[i]]

    scores = []
    scores.append(score)

    for i in range(0, len(seq) - window_size):
        score = score - values[seq[i]] + values[seq[i + window_size]]
        scores.append(score)

    return scores;
