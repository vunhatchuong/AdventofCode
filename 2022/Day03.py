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

for i in EXAMPLE.splitlines():
    compartment_1, compartment_2 = i[0:int(len(i)/2)], i[int(len(i)/2):]
    # print(compartment_1, compartment_2)
    wrong_item, = set(compartment_1).intersection(set(compartment_2))
    print(wrong_item, ord(wrong_item))
    if wrong_item.islower():
        print("e")
