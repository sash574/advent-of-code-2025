# Advent of Code 2025 - Puzzle Day 5

with open('input_day5.txt', 'r') as file:
    input_string = file.read().splitlines()

fresh_ids = [val for val in input_string if input_string.index(val) < input_string.index('')]

fresh_ids_range = []
for id in fresh_ids:
    low_limit, high_limit = id.split(sep='-')
    fresh_ids_range.append((int(low_limit), int(high_limit)))

available_ids = [int(val) for val in input_string if input_string.index(val) > input_string.index('')]

# algorithm for task 1
fresh_count = 0

for avai_id in available_ids:
    if any(start <= avai_id <= end for start, end in fresh_ids_range):
        fresh_count += 1

print(fresh_count)

## short version
fresh_count2 = sum(any(start <= avai_id <= end for start, end in fresh_ids_range) for avai_id in available_ids)
print(fresh_count2)

# algorithm for task 2
fresh_ids_range.sort()

merged = []
for start, end in fresh_ids_range:
    if not merged:
        merged.append([start, end])
    else:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

fresh_ids_count = 0
for start, end in merged:
    fresh_ids_count += end - start + 1

print(fresh_ids_count)