from collections import defaultdict, Counter


def read_file_lines(file_path):
    with open(file_path) as file:
        return [line.strip("\n") for line in file.readlines()]


def main():
    # Main script
    input = read_file_lines("Input/day4.txt")

    scratchcards = defaultdict(int)
    temp = Counter()

    for card, line in enumerate(input, start=1):
        winning_numbers = set(line[9:39].split())
        my_numbers = set(line[41:].split())
        matches = winning_numbers.intersection(my_numbers)

        new_cards = list(range(card + 1, len(matches) + card + 1))
        occurrences = temp[card] + 1

        scratchcards[card] += occurrences
        for item in new_cards:
            temp[item] += occurrences

    return sum(scratchcards.values())


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
