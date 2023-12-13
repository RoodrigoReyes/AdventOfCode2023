def read_file_lines(file_path):
    with open(file_path) as file:
        return file.read().split("\n\n")


def main():
    # Main script
    input = read_file_lines("Input/day5.txt")
    seeds, *blocks = input

    seeds = list(map(int, seeds.split(": ")[1].split()))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            # a, b, c = list(map(int, line.split()))
            ranges.append(list(map(int, line.split())))
        new = []
        # print(seeds)
        for x in seeds:
            for a, b, c in ranges:
                if x in range(b, b + c):
                    value = x + a - b
                    new.append(value)
                    break
            else:
                new.append(x)
        seeds = new

    return seeds


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", min(result))
