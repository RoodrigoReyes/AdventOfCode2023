import re


def read_file_lines(file_path):
    with open(file_path) as file:
        return [line.strip("\n") for line in file.readlines()]


def nest_input_lines(lines):
    return [list(line) for line in lines]


def get_positions(data):
    number_positions = {}
    syms_positions = {}
    for r, line in enumerate(data):
        # Obtener la posicion en rangos de los valores numericos que estan en la data
        # Encontrar todas las coincidencias
        matches = re.finditer(r"\d+", line)
        # Crear una lista de números y sus rangos de índices
        for _match in matches:
            start = _match.start()
            end = _match.end() - 1
            for i in range(start, end + 1):
                number_positions[(r, i)] = int(_match.group())

        # Obtener la posición en rangos de los signos de puntuación que no sean puntos
        line_syms = re.sub(r"[\d\.]", " ", line).split()
        offset = 0

        if line_syms:
            for symbol in line_syms:
                symbol_pos = line.index(symbol, offset)

                syms_positions[(r, symbol_pos)] = symbol
                offset = symbol_pos + 1

    return number_positions, syms_positions


def obtener_elementos_adyacentes(matriz, nums, x, y):
    # Direcciones relativas para buscar alrededor del punto dado
    direcciones = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, 1], [1, 1], [-1, -1], [1, -1]]

    # Iterar sobre cada dirección
    resultados = []
    for i, (dx, dy) in enumerate(direcciones):
        nx, ny = x + dx, y + dy
        # Verificar si las nuevas coordenadas están dentro de los límites de la matriz
        if (
            0 <= nx < len(matriz)
            and 0 <= ny < len(matriz[0])
            and matriz[nx][ny].isdigit()
        ):
            resultados.append(nums[(nx, ny)])

    return list(set(resultados))


def main():
    # Main script
    file_lines = read_file_lines("Input/day3.txt")
    nested_lines = nest_input_lines(file_lines)
    nums, syms = get_positions(file_lines)

    total_answer = []
    for x, y in syms.keys():
        list_numbers_adj = obtener_elementos_adyacentes(nested_lines, nums, x, y)
        total_answer.extend(list_numbers_adj)

    return sum(total_answer)


if __name__ == "__main__":
    result = main()

    print("La respuesta es:", result)
