# Advent of Code 2025 - Day 7

with open('input_day7.txt', 'r') as file:
    tach_manifold = file.read().splitlines()

# algorithm for Part 1
split_count = 0
beam_indexes = set([tach_manifold[0].index('S')])

for line in tach_manifold[1:]:

    split_indexes = set()

    for i in beam_indexes:

        if line[i] == '^':
            split_count += 1
            split_indexes.add(i-1)
            split_indexes.add(i+1)

        else:
            split_indexes.add(i)

    beam_indexes = split_indexes

print(f'Solution to Part 1: {split_count}')

# algorithm for Part 2
def count_timelines(row, col, manifold, helper_matrix):

    if row == len(manifold):
        return 1                                                                                                       # one timeline completed

    if helper_matrix[row][col] != 0:
        return helper_matrix[row][col]

    if manifold[row][col] == '^':
        helper_matrix[row][col] = count_timelines(row + 1, col - 1, manifold, helper_matrix) + count_timelines(row + 1, col + 1, manifold, helper_matrix)
        return helper_matrix[row][col]                                                                                 # split; new timelines left & right
    
    elif manifold[row][col] == '.' or manifold[row][col] == 'S':
        return count_timelines(row + 1, col, manifold, helper_matrix)                                                  # else: continue current timeline

start_col = tach_manifold[0].index('S')   
nullmatrix = [[0 for val in range(len(tach_manifold[0]))] for row in range(len(tach_manifold))] 
timeline_count = count_timelines(1, start_col, tach_manifold, nullmatrix)
print(f'Solution to Part 2: {timeline_count}')