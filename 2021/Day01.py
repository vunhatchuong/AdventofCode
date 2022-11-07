file = open("./input/Day01.in", "r", encoding="utf-8").read().splitlines()
depths = [int(x) for x in file]

# Part One
increases = sum(x < y for x, y in zip(depths, depths[1:]))
print(increases)

# Part Two

increases = sum(x < y for x, y in zip(depths, depths[3:]))
print(increases)
