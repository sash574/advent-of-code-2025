# Advent of Code 2025 - Puzzle Day 2

## read input file into list
with open('input_day2.txt', 'r') as file:
    input_str = file.read().strip()

print(f'Input Text: {type(input_str), input_str}')

# extract current range
list_ranges = input_str.split(sep=',')
print(list_ranges)

# algorithm for part 1
invalid_ids_count1 = 0
invalid_ids_count2 = 0

for i in list_ranges:
    low_limit, high_limit = i.split(sep='-')

    for val in range(int(low_limit), int(high_limit) + 1):
        val = str(val)
        middle = int(len(val) / 2)
        left_part = val[:middle]
        right_part = val[middle:]
        if len(val) % 2 == 0 and left_part == right_part:
            invalid_ids_count1 += int(val)
        if any(val == val[:cut] * (len(val) // cut) for cut in range(1, middle + 1)):
            invalid_ids_count2 += int(val)

print(f'Solution to Part 1: {invalid_ids_count1}')
print(f'Solution to Part 2: {invalid_ids_count2}')