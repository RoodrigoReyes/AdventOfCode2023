def read_file_lines(file_path):
    with open(file_path) as file:
        return file.read().splitlines()


def main():
    # Main script
    input = read_file_lines("Input/day4.txt")
    list_points = []
    for card, line in enumerate(input):
        winning_numbers = line[9:39].split()
        my_numbers = line[41:].split()
        matches = set(winning_numbers).intersection(set(my_numbers))
        if matches:
            len_matches = len(matches)
            # print("Carta", card + 1, "Match:", len_matches)
            points = 2 ** (len_matches - 1)
            list_points.append(points)

    return sum(list_points)


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
