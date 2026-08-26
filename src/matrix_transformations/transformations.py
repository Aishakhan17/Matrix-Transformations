from copy import deepcopy


def horizontal_reflection(grid):
    reflected_grid = []
    for row in grid[::-1]:
        reflected_grid.append(row)
    return reflected_grid


def vertical_reflection(grid):
    reflected_grid = deepcopy(grid)
    j = -1
    k = 0
    for i in range(len(reflected_grid)):
        row = reflected_grid[i]
        row[k], row[j] = row[j], row[k]
    return reflected_grid


def main_diagonal_reflection(grid):
    reflected_grid = deepcopy(grid)
    i = 0
    j = 0
    k = 0
    while k < (len(reflected_grid) * 2):
        if j >= len(reflected_grid):
            i += 1
            j = 0
        if i != j and j > i:
            reflected_grid[i][j], reflected_grid[j][i] = (
                reflected_grid[j][i],
                reflected_grid[i][j],
            )

        j += 1
        k += 1
    return reflected_grid


def anti_diagonal_reflection(grid):
    reflected_grid = deepcopy(grid)
    center_cell = (len(grid) + 1) // 2
    center_cell_i, center_cell_j = center_cell - 1, center_cell - 1
    for i in range(len(reflected_grid)):
        row = reflected_grid[i]
        for j in range(len(row)):
            if i <= 1 and j <= 1:
                if (i == 0 and j == len(grid) - 1) or (
                    i == center_cell_i and j == center_cell_j
                ):
                    pass
                else:
                    swap_i_pos = len(reflected_grid) - 1 - j
                    swap_j_pos = len(reflected_grid) - 1 - i
                    reflected_grid[i][j], reflected_grid[swap_i_pos][swap_j_pos] = (
                        reflected_grid[swap_i_pos][swap_j_pos],
                        reflected_grid[i][j],
                    )
    return reflected_grid


def rotate_90(grid):
    reverse_grid = grid[::-1]
    rotated_grid = []
    k = 0
    i = 0
    j = 0
    row = []

    while k < (len(reverse_grid) ** 2):
        row.append(reverse_grid[i][j])
        i += 1
        if i >= len(grid):
            rotated_grid.append(row)
            row = []
            i = 0
            j += 1
        k += 1
    return rotated_grid

def rotate_180(grid):
    rotated_90 = rotate_90(grid)
    rotated_180 = rotate_90(rotated_90)
    return rotated_180

def rotate_270(grid):
    rotated_180 = rotate_180(grid)
    rotated_270 = rotate_90(rotated_180)
    return rotated_270


