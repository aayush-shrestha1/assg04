from q02 import load_word_set, compare_word_sets


def main():
    while True:
        left_filename = input("Enter file name to use for left set of words: ")

        try:
            left_set = load_word_set(left_filename)
            break
        except FileNotFoundError:
            print("Invalid file name given, try again")

    while True:
        right_filename = input("Enter file name to use for right set of words: ")

        try:
            right_set = load_word_set(right_filename)
            break
        except FileNotFoundError:
            print("Invalid file name given, try again")

    while True:
        comparison = input(
            "Enter comparison (BOTH, EITHER, LEFT, RIGHT) or QUIT: "
        )

        if comparison == "QUIT":
            break

        try:
            result = compare_word_sets(
                left_set,
                right_set,
                comparison
            )

            print(sorted(result))

        except Exception:
            print("Invalid comparison asked for, try again")


if __name__ == "__main__":
    main()
