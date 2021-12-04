f = open("input.txt", "r")
data = []

for line in f.readlines():
    data.append(line.strip())

aim = 0
vertical = 0
horizontal = 0

for elem in data:
    word = elem.split(' ', 1)[0]
    number = elem.split(' ', 1)[1]
    if word == 'up':
        aim = aim - int(number)
    elif word == 'down':
        aim = aim + int(number)
    elif word == 'forward':
        horizontal = horizontal + int(number)
        vertical = vertical + (aim * int(number))

print(vertical*horizontal)
