with open("./input/Day04.in","r",encoding="utf-8") as f:
    s = f.read()

EXAMPLE = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

EXAMPLE2 = """6-65,4-5
2-88,3-88
23-69,23-98
1-99,2-60
15-70,15-71
45-67,2-68
37-64,5-59
3-79,2-79
38-83,38-83
4-4,5-98
43-74,43-75
4-99,2-5
31-42,42-42
24-28,27-30
2-80,2-81
33-66,30-62
80-93,80-80
30-81,81-93
17-96,16-84
48-86,47-62
"""

assigned_pair = [[i for i in part.split(",")] for part in EXAMPLE.splitlines()]

# count_pair = 0
# for i,j in assigned_pair:
#     if (int(i.split("-")[0]) <= int(j.split("-")[0]) and (int(i.split("-")[1]) >= int(j.split("-")[1]))) or (int(i.split("-")[0]) >= int(j.split("-")[0]) and int(i.split("-")[1]) <= int(j.split("-")[1])):
#         count_pair += 1

# print(count_pair)

# Part two
count_pair = 0
for i,j in assigned_pair:
    print(i,j)
