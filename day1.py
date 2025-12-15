# Advent of Code - Puzzle Day 1

## read input file into list
with open('input_day1.txt', 'r') as file:
    input_list = file.read().splitlines()

print(f'Input Text: {type(input_list), input_list}')                     # note: input_list contains values > 99; cyclic adaption necessary!

## algorithm for Part 1 (range in between 0-99; rotation left/right; steps of varying sizes (no limit); count number of times that pointer is on 0 after each input)

safe_position = 50
count_zero = 0

for i in input_list:

    rotation = i[0]
    distance = int(i[1:])
    
    if rotation == 'L':
        safe_position = (safe_position - distance) % 100
    elif rotation == 'R':
        safe_position = (safe_position + distance) % 100

    if safe_position == 0:
        count_zero += 1

print(f'Solution Part 1: {count_zero}')

## algorithm for Part 2 (count every time pointer is on 0, even while clicking)

safe_position = 50
count_zero = 0

for i in input_list:

    rotation = i[0]
    distance = int(i[1:])

    for _ in range(distance):

        if rotation == 'L':
            safe_position = (safe_position - 1) % 100
        elif rotation == 'R':
            safe_position = (safe_position + 1) % 100

        if safe_position == 0:
            count_zero += 1

print(f'Solution Part 2: {count_zero}')