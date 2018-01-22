recent_num, i = 0, 0
whole = [temp for temp in range(10000)]
self_num = []
while i <= 10000:
    sum = i
    for j in str(i):
        sum += int(j)
    self_num.append(sum)
    i += 1
self_num.sort()
result = list(set(whole) - set(self_num))
result.sort()
for ans in result:
    if ans > 10000:
        break
    print(ans)