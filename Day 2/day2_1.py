import re


def get_input(file_path):
    with open(file_path) as file:
        return file.readlines()


def process_row(row):
    cleaned_values = row.strip().split(": ")[1].split("; ")
    color_count_dict = {}
    for value_group in cleaned_values:
        color_values = value_group.split(", ")
        for color_value in color_values:
            color = re.findall(r"[a-zA-Z]+", color_value)[0]
            count = int(re.findall(r"\d+", color_value)[0])
            if color in color_count_dict:
                color_count_dict[color] = max(color_count_dict[color], count)
            else:
                color_count_dict[color] = count

    return color_count_dict


def main():
    input = get_input("Input\day2.txt")
    sum_ = 0
    for index, row in enumerate(input, start=1):
        values = process_row(row)
        if values["red"] <= 12 and values["green"] <= 13 and values["blue"] <= 14:
            sum_ += index

    return sum_


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
