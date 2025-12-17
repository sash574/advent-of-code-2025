# Advent of Code 2025 - Puzzle Day 3

with open('input_day3.txt', 'r') as file:
    input_list = file.read().splitlines()

## algorithm for both parts
def max_joltage(data, num_batteries):
    
    '''
    This function calculates the maximum joltage possible for each bank of batteries and then adds it up to the total maximum joltage.

    Input Parameters:
    - data: list containing banks as individual strings
    - num_batteries: number of batteries to turn on
    '''

    max_joltages = []

    for bank in data:

        batteries_on = []
        bat_remain = num_batteries

        bank_len = len(bank)
        batteries = list(bank)                                                          # list containing individual batteries for selected bank

        bat_index = -1                                                                  # initializer for searching in the battery

        while bat_remain > 0:
            bat_max = max(batteries[bat_index + 1 : bank_len - bat_remain + 1])         # max digit in available slice (ends early enough to leave toom for remaining required batteries to turn on and starts after last found max digit index)
            bat_index = batteries.index(bat_max, bat_index + 1)

            batteries_on.append(bat_max)
            print(batteries_on)
            bat_remain -= 1

        max_joltages.append(int(''.join(batteries_on)))                                 # concatenate max digits for final joltage number per bank
        print(max_joltages)
        max_jolt = sum(max_joltages)                                                    # total maximum joltage number

    return max_jolt

## calling the function
max_jolt1 = max_joltage(input_list, 2)
print(f'Solution to Part 1: {max_jolt1}')  

max_jolt2 = max_joltage(input_list, 12)
print(f'Solution to Part 2: {max_jolt2}')