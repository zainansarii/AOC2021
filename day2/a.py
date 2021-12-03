f = open("input.txt", "r")
data = []

for line in f.readlines():
    data.append(line.strip())

vertical = 0
horizontal = 0

for elem in data:
    word = elem.split(' ', 1)[0]
    number = elem.split(' ', 1)[1]
    if word == 'up':
        vertical = vertical - int(number)
    elif word == 'down':
        vertical = vertical + int(number)
    elif word == 'forward':
        horizontal = horizontal + int(number)

print(vertical*horizontal)
