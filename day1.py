import re
DEBUG = False
TEST = False
SMALL = False

inputs = []

filepath = "data/day1.txt" if not TEST else "data/day1-test.txt"
with open(filepath, 'r') as file:
    for line in file :
        instruction = line.strip()
        split_intruction = re.findall(r'\d+|\D+', instruction)
        inputs.append(split_intruction)


if SMALL:
    inputs = inputs[:10]

starting_position = 50 
count_total_zero = 0
count_end_zero = 0
current_position = starting_position

if DEBUG:
    print("")

for i,instruction in enumerate(inputs) :
    direction = 1 if instruction[0] == "R" else -1
    steps = int(instruction[1])

    for _ in range(steps):
        current_position = (current_position + direction) % 100
        if current_position == 0 :
            count_total_zero += 1
    if current_position == 0:
        count_end_zero += 1

    if (DEBUG):
        print(f"After instruction #{i} : {instruction}")
        print(f"current position : {current_position}")
        print(f"count_zero : {count_total_zero}")
        print(f"count_passingbyzero : {count_end_zero}\n")

print(count_end_zero)
print(count_total_zero)


