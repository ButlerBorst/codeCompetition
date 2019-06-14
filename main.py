import fileinput

for line in fileinput.input():
    print(''.join(reverse(line)))
