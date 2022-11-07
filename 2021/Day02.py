file = open("./input/Day02.in", "r", encoding="utf-8").read().splitlines()

instructions = [x.split(" ") for x in file]
depths = 0
horizontal = 0
# for cmd, val in instructions:
#     if cmd == "forward":
#         horizontal += int(val)
#     if cmd == "down":
#         depths += int(val)
#     if cmd == "up":
#         depths -= int(val)

# print(horizontal * depths)

# Part Two

aim, d, h = 0, 0, 0
for cmd, val in instructions:
    if cmd == "forward":
        h += int(val)
        d += int(val) * aim
    if cmd == "down":
        aim += int(val)
    if cmd == "up":
        aim -= int(val)

print(h * d)
