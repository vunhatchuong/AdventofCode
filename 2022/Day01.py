# My solution
file = open("./input/Day01.in", "r", encoding="UTF-8").read().splitlines()

number_of_person = 0
output = [0]
for line in file:
    if line == "":
        number_of_person += 1
        output.append(0)
        continue

    output[number_of_person] += int(line)

print("Number of person", number_of_person)
print("Max Calories", max(output))

# Part two

print("Sum of top 3 values", sum(sorted(output)[-3:]))


## Optimized
file = open("./input/Day01.in", "r", encoding="UTF-8").read()


# Part one
print(max(
    sum(int(line) for line in part.splitlines())
    for part in file.split("\n\n")
        )
    )

# Part Two
print(sum(sorted(
    sum(int(line) for line in part.splitlines())
    for part in file.split("\n\n")
        )
      [-3:]))
