f = open("input.txt", "r")
data = []

for line in f.readlines():
    data.append(line.strip())

gamma_rate = []
epsilon_rate = []

for i in range(12):
    one_count = 0
    zero_count = 0

    for elem in data:
        if elem[i] == '0':
            zero_count += 1
        elif elem[i] == '1':
            one_count += 1

    if one_count > zero_count:
        gamma_rate.append('1')
        epsilon_rate.append('0')
    elif zero_count > one_count:
        gamma_rate.append('0')
        epsilon_rate.append('1')

gamma_rate = ''.join(gamma_rate)
epsilon_rate = ''.join(epsilon_rate)

res = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(res)
