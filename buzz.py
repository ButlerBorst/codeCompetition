import fileinput

inp = fileinput.input()
num1, num2 = map(int, next(inp).split())
word1, word2 = next(inp).split()

for line in inp:
    n = int(line)
    if not (num1 % n) and not (num2 % n):
        print(word1, word2)
    elif not (num1 % n):
        print(word1)
    elif not (num2 % n):
        print(word2)
    else:
        print(n)
