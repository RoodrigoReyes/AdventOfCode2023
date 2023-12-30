def read_file_lines(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()

    return [list(map(int, line.split())) for line in lines]


def get_diferences(numbers):
    if all(x == 0 for x in numbers):
        return 0

    differences = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]

    return numbers[-1] + get_diferences(differences)


def main():
    list_numbers = read_file_lines("Input/day9.txt")
    return sum([get_diferences(numbers) for numbers in list_numbers])


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
