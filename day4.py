# Advent of Code 2025 - Puzzle Day 4

# read input file into list of strings
with open('input_day4.txt', 'r') as file:
    grid = file.read().splitlines()

# helper function
def adj_pos(grid, row, row_index, i):
    '''
    Checks up to 8 adjacent positions to current roll and
    returns number of rolls next to it.
    '''
    adj_rolls = 0
    max_row = len(grid)
    max_col = len(row)

    ## relative neighbor coordinates: 8 directions
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),  # above
        (0, -1),           (0, 1),   # left, right
        (1, -1),  (1, 0),  (1, 1)    # below
    ]

    for ind_row, ind_col in neighbors:
        new_row = row_index + ind_row
        new_col = i + ind_col

        ## bounds check before accessing
        if 0 <= new_row < max_row and 0 <= new_col < max_col:
            if grid[new_row][new_col] == '@':
                adj_rolls += 1

    return adj_rolls


# algorithm for task 1
num_rolls = 0

for row_index, row in enumerate(grid):
    for i in range(len(row)):
        curr_roll = row[i]

        if curr_roll == '@':
            adj_rolls = adj_pos(grid, row, row_index, i)
            if adj_rolls < 4:
                num_rolls += 1

print(num_rolls)

# algorithm for task 2
removed_rolls = 0

while True:
    to_remove = []

    for row_index, row in enumerate(grid):
        for i in range(len(row)):
            curr_roll = row[i]

            if curr_roll == '@':
                adj_rolls = adj_pos(grid, row, row_index, i)
                if adj_rolls < 4:
                    to_remove.append((row_index, i))

    if not to_remove:
        break

    removed_rolls += len(to_remove)

    for row_index, i in to_remove:
        row_list = list(grid[row_index])
        row_list[i] = 'x'
        grid[row_index] = ''.join(row_list)

print(removed_rolls)