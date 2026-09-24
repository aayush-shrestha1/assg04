def load_word_set(filename):
    words = set()

    with open(filename, "r") as file:
        for line in file:
            word = line.strip()
            words.add(word)

    return words


def compare_word_sets(left_set, right_set, comparison):
    if comparison == "BOTH":
        return left_set & right_set

    elif comparison == "EITHER":
        return left_set | right_set

    elif comparison == "LEFT":
        return left_set - right_set

    elif comparison == "RIGHT":
        return right_set - left_set

    else:
        raise Exception(f"Invalid comparison requested: {comparison}")
