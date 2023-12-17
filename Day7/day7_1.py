from collections import Counter, defaultdict


def read_file_lines(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()
    return [[line.split()[0], int(line.split()[1])] for line in lines]


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


def calculate_hand_sum(hand, card_values):
    return [card_values[card] for card in hand]


def main():
    data = read_file_lines("Input/day7.txt")
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 11,
                   "T": 10, "9": 9,  "8": 8,  "7": 7,
                   "6": 6,  "5": 5,  "4": 4,  "3": 3,
                   "2": 2
                    }  # fmt: skip

    list_result_hands = ["HighCard", "OnePair", "TwoPair", "ThreeOfAKind",
                         "FullHouse", "FourOfAKind", "FiveOfAKind"
                         ]  # fmt: skip

    dict_hands = defaultdict(list)

    for hand, bid in data:
        values = list(Counter(hand).values())
        result_hand = check_hand(values)
        list_numbers_card = calculate_hand_sum(hand, card_values)
        dict_hands[result_hand].append((hand, list_numbers_card, bid))

    n = 0
    count = 1
    for hand_type in list_result_hands:
        dict_hands[hand_type].sort(key=lambda x: x[1])
        for hand, list_numbers_card, bid in dict_hands[hand_type]:
            n += bid * count
            count += 1

    return n


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
