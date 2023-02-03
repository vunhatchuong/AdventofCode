with open("./input/Day03.in","r",encoding="utf-8") as f:
    s = f.read()

rucksacks = [ i for i in s.splitlines()]

EXAMPLE = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

sum_ruck = 0

# for i in rucksacks:
#     compartment_1, compartment_2 = i[0:int(len(i)/2)], i[int(len(i)/2):]
#     # print(compartment_1, compartment_2)
#     wrong_item, = set(compartment_1).intersection(set(compartment_2))
#     if wrong_item.islower():
#         print(wrong_item, ord(wrong_item) - 96)
#         sum_ruck += ord(wrong_item) - 96
#     else:
#         print(wrong_item, ord(wrong_item) - 38)
#         sum_ruck += ord(wrong_item) - 38

# print(sum_ruck)

# Part Two

split_example = EXAMPLE.splitlines()
for index,i in enumerate(rucksacks):
    if index % 3 == 0:
        common_item, = set(rucksacks[index]).intersection(set(rucksacks[index+1]),set(rucksacks[index+2]))
        # print(common_item)
        if common_item.islower():
            print(common_item, ord(common_item) - 96)
            sum_ruck += ord(common_item) - 96
        else:
            print(common_item, ord(common_item) - 38)
            sum_ruck += ord(common_item) - 38

print(sum_ruck)
