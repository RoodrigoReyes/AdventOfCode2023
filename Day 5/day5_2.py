def read_file_lines(file_path):
    with open(file_path) as file:
        return file.read().split("\n\n")


def main():
    # Main script
    inputs = read_file_lines("Input/day5.txt")
    seeds, *blocks = inputs

    seeds = list(map(int, seeds.split(": ")[1].split()))
    seeds = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            # a, b, c = list(map(int, line.split()))
            ranges.append(list(map(int, line.split())))

        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in ranges:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                new.append((s, e))

        seeds = new

    return seeds


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", min(result)[0])
