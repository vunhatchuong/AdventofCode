depths = [int(x) for x in open("Day01.in")]

p1_ans = 0
p2_ans = 0
for i in range(len(depths)):
    if i >= 1 and depths[i] > depths[i-1]:
        p1_ans += 1
    if i >=3 and (depths[i] + depths[i-1] + depths[i-2]) > (depths[i-1] + depths[i-2] + depths[i-3]):
        p2_ans += 1

print(p1_ans)
print(p2_ans)
