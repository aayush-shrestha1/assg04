from q01 import load_ranked_items, sort_ranked_items, get_ranked_items


def main():
    while True:
        filename = input("Enter file name of ranked items to query: ")

        try:
            items = load_ranked_items(filename)
            break
        except FileNotFoundError:
            print("Invalid rank item file name, try again")

    items = sort_ranked_items(items)

    print(f"Loaded {len(items)} items from {filename}")

    while True:
        begin = int(input(f"Enter begin index (1 to {len(items)}, 0 to exit): "))

        if begin == 0:
            break

        end = int(input(f"Enter end index (1 to {len(items)}, begin <= end): "))

        try:
            result = get_ranked_items(items, begin, end)
            print(result)
        except Exception:
            print("Invalid index(s) entered, try again")


if __name__ == "__main__":
    main()
