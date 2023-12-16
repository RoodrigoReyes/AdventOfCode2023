from collections import Counter, defaultdict


def read_file_lines(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()

    return [line.split() for line in lines]


def check_hand(values):
    len_values = len(values)

    if len_values == 5:
        return "HighCard"

    elif len_values == 4:
        return "OnePair"

    elif len_values == 3:
        if 3 in values:
            return "ThreeOfAKind"
        else:
            return "TwoPair"

    elif len_values == 2:
        if 4 in values:
            return "FourOfAKind"
        else:
            return "FullHouse"

    else:
        return "FiveOfAKind"


def main():
    data = read_file_lines("Input/day7.txt")

    win_hands = defaultdict(list)
    groups = [
        "HighCard",
        "OnePair",
        "TwoPair",
        "ThreeOfAKind",
        "FullHouse",
        "FourOfAKind",
        "FiveOfAKind",
    ]

    for hand, bid in data:
        counter = Counter(hand)
        values = list(counter.values())
        result_hand = check_hand(values)

        # print("Mano:", hand, "Resultado:", result_hand)

    return data


if __name__ == "__main__":
    result = main()

    # print(result)
