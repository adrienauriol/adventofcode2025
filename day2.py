import re
DEBUG = False
TEST = False
SMALL = False

inputs = []

filepath = "data/day2.txt" if not TEST else "data/day2-test.txt"
with open(filepath, 'r') as file:
    for line in file :
        instructions = line.split(",")
        for instruction in instructions :
            split_instruction = instruction.split("-")
            inputs.append( [int(split_instruction[0]), int(split_instruction[1])] )

if SMALL : 
    inputs = inputs[:3]

def isInvalid_t1(id):
    pattern = re.compile(r'^(\d+)\1$')
    if (pattern.match(str(id))):
        return True
    return False

def isInvalid_t2(id):
    pattern = re.compile(r'^(\d+)\1+$')
    if (pattern.match(str(id))):
        return True
    return False


def find_invalid_id(idrange):
    invalid_ids_t1 = []
    invalid_ids_t2 = []
    beg, end = idrange
    range_to_test = [i for i in range(beg,end+1)]
    for id in range_to_test:
        if isInvalid_t1(id) :
            invalid_ids_t1.append(id)
        if isInvalid_t2(id) :
            invalid_ids_t2.append(id)
    return (invalid_ids_t1,invalid_ids_t2)

def task1(inp):
    solution = 0
    for idrange in inp:
        list_invalid_ids = find_invalid_id(idrange)[0]
        for invalid_id in list_invalid_ids:
            solution += invalid_id
    print(solution)

def task2(inp):
    solution = 0
    for idrange in inp:
        list_invalid_ids = find_invalid_id(idrange)[1]
        for invalid_id in list_invalid_ids:
            solution += invalid_id
    print(solution)

task1(inputs)
task2(inputs)
