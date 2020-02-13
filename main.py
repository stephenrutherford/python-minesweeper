
def main(bombs, rows, cols):
    field = [[0 for i in range(cols)] for j in range(rows)]

    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_col + 2)
        col_range = range(bomb_row - 1, bomb_col + 2)

        for i in row_range:
            for j in col_range:
                if (0 <= i < rows and 0 <= j < cols and field[i][j] != -1):
                    field[i][j] += 1

    return "\n".join([str(row) for row in field])
    # return field

print(main([[0,0], [1,2]], 3, 4))