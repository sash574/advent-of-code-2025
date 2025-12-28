# Advent of Code 2025 - Day 6

import re
import math

# preprocessing for Part 1
lines = []

with open('input_day6.txt', 'r') as file:
    for line in file:
        clean_string = re.sub('\s+', ',', line).strip()
        clean_list = clean_string.split(',')
        lines.append(clean_list)

num1_list = [int(x) for x in lines[0] if x is not '']
num2_list = [int(x) for x in lines[1] if x is not '']
num3_list = [int(x) for x in lines[2] if x is not '']
num4_list = [int(x) for x in lines[3] if x is not '']
operator_list = [x for x in lines[4] if x != '']

print(len(num1_list), len(num2_list), len(num3_list), len(num4_list), len(operator_list))

# algorithm for Part 1
total = 0

for i in range(len(operator_list)):

    first_num = num1_list[i]
    second_num = num2_list[i]
    third_num = num3_list[i]
    fourth_num = num4_list[i]

    num_list = [first_num, second_num, third_num, fourth_num]

    operator = operator_list[i]

    if operator == '*':
        result = math.prod(num_list)
    elif operator == '+':
        result = sum(num_list)

    total += result

print(f'Solution to Part 1: {total}')

# preprocessing & algorithm for Part 2
with open('input_day6.txt', 'r') as file:
    lines = file.read().splitlines()
   
new_numbers = []
total_new = 0

for i in range(len(lines[0])):

    curr_num = ''

    for j in range(len(lines)):

        if lines[j][i].isdigit():
            curr_num += lines[j][i]

        elif lines[j][i] == '*' or lines[j][i] == '+':
            operator = lines[j][i]

    if curr_num == '':

        if operator == '*':
            total_new += math.prod(new_numbers)

        elif operator == '+':
            total_new += sum(new_numbers)

        new_numbers = []

    else:
        new_numbers.append(int(curr_num))
        
if operator == '*':
    total_new += math.prod(new_numbers)

elif operator == '+':
    total_new += sum(new_numbers)
    
print(f'Solution to Part 2: {total_new}')