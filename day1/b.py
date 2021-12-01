f = open("input.txt", "r")
data = []

for line in f.readlines():
    data.append(int(line))

new_data = []
for i in range(len(data) - 2):
    temp = data[i] + data[i+1] + data[i+2]
    new_data.append(temp)

res = 0

for i in range(1, len(new_data)):
    if new_data[i] > new_data[i - 1]:
        res += 1

print(res)