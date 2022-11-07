file = open("./input/Day03.in", "r", encoding="utf-8").read().splitlines()

gamma_str = ""
epsilon_str = ""
bit_0 = 0
bit_1 = 0
for x in range(len(file[0])):
    bit_0 = sum(1 for line in file if line[x] == '0')
    bit_1 = len(file) - bit_0
    if bit_0 > bit_1:
        gamma_str += "0"
        epsilon_str += "1"
    else:
        gamma_str += "1"
        epsilon_str += "0"

print(gamma_str)
print(epsilon_str)

gamma_dec = int(gamma_str, 2)
epsilon_dec = int(epsilon_str, 2)
print(gamma_dec * epsilon_dec)

# Part Two

