import math
import re


def read_file_lines(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()

    lines = [line for line in lines if line != ""]

    directions = lines[0]

    dict_nodes = {line.split()[0]: re.findall("[a-zA-Z]+", line)[1:] for line in lines[1:]}  # fmt: skip

    return directions, dict_nodes


def main():
    directions, dict_nodes = read_file_lines("Input/day8.txt")

    inits_nodes = [node for node in dict_nodes.keys() if node.endswith("A")]

    all_steps = []
    for node in inits_nodes:
        count = 0
        while not node.endswith("Z"):
            for direction in directions:
                if direction == "L":
                    node = dict_nodes[node][0]
                elif direction == "R":
                    node = dict_nodes[node][1]
                count += 1

        all_steps.append(count)

    return math.lcm(*all_steps)


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
