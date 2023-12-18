import re


def read_file_lines(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()

    lines = [line for line in lines if line != ""]

    directions = lines[0]

    dict_nodes = {
        line.split()[0]: re.findall("[a-zA-Z]+", line)[1:] for line in lines[1:]
    }

    return directions, dict_nodes


def main():
    node = "AAA"
    end_node = "ZZZ"

    directions, dict_nodes = read_file_lines("Input/day8.txt")

    count = 0
    while node != end_node:
        cur = node
        for direction in directions:
            if direction == "R":
                node = dict_nodes[cur][1]
            elif direction == "L":
                node = dict_nodes[cur][0]
            count += 1

    return count


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
