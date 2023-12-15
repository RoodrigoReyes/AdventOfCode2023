def read_file_lines(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    time = [int("".join(lines[0].split()[1:]))]
    distance = [int("".join(lines[1].split()[1:]))]

    return time, distance


def main():
    times, distances = read_file_lines("Input/day6.txt")

    n = 1
    for time, distance in zip(times, distances):
        margin = 0
        for bp in range(1, time + 1):
            dr = bp * (time - bp)
            if dr > distance:
                margin += 1

        n *= margin

    return n


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
