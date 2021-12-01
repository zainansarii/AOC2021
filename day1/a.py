f = open("input.txt", "r")
data = []

for line in f.readlines():
    data.append(int(line))

res = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        res += 1

print(res)
