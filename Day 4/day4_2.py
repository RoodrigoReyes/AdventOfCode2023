def read_file_lines(file_path):
    with open(file_path) as file:
        return [line.strip("\n") for line in file.readlines()]


def main():
    # Main script
    pass


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
