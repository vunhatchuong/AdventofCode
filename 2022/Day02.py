with open("./input/Day02.in","r",encoding="UTF-8") as f:
    s = f.read()

rounds = [x for x in s.splitlines()]

score = 0

OUTCOMES = {
        "A X": 1+3,
        "A Y": 2+6,
        "A Z": 3+0,
        "B X": 1+0,
        "B Y": 2+3,
        "B Z": 3+6,
        "C X": 1+6,
        "C Y": 2+0,
        "C Z": 3+3
        }

# for round in rounds:
    # print(round, OUTCOMES[round])
    # score += OUTCOMES[round]

# print(score)

#Part two

score_part2 = 0

OUTCOMES_PART2 = {
        "A X": 3+0,
        "A Y": 1+3,
        "A Z": 2+6,
        "B X": 1+0,
        "B Y": 2+3,
        "B Z": 3+6,
        "C X": 2+0,
        "C Y": 3+3,
        "C Z": 1+6
        }

for round in rounds:
    print(round, OUTCOMES_PART2[round])
    score_part2 += OUTCOMES_PART2[round]

print(score_part2)
