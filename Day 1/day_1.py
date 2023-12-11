import re


def get_input(file_path):
    with open(file_path) as file:
        return file.readlines()


def main():
    lines = get_input("Input\day1.txt")
    sum_ = 0

    for line in lines:
        numbers = re.findall(r"\d+", line)
        concat_numbers = "".join(numbers)

        if len(concat_numbers) > 1:
            number = concat_numbers[0] + concat_numbers[-1]
        else:
            number = concat_numbers + concat_numbers

        sum_ += int(number)

    return sum_


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
