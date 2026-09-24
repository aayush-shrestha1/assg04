def load_ranked_items(filename):
    items = []

    with open(filename, "r") as file:
        while True:
            rank = file.readline()

            if rank == "":
                break

            name = file.readline()

            rank = int(rank.strip())
            name = name.strip()

            items.append((rank, name))

    return items


def sort_ranked_items(items):
    return sorted(items)


def get_ranked_items(items, begin, end):
    if begin < 1 or begin > end or end > len(items):
        raise Exception("Invalid ranks")

    return items[begin - 1:end]
