file = open("./input/Day03.in", "r", encoding="utf-8").read().splitlines()

filter_gamma = [x[y] for x, y in zip(file, range(len(file[0])))]

gamma = ""

# if filter_gamma.count("0") > filter_gamma.count("1"):
#     gamma += "0"
# else:
#     gamma += "1"

# print(gamma)
print(filter_gamma)
# print(range(len(file[0])))
