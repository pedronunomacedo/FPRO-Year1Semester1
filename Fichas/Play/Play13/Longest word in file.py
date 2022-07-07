def longest(filename):
    with open(filename, 'r') as file:
        content = file.read()
    l = content.split()
    l = sorted(l, key=len, reverse=True)
    return l[0]

print(longest('shakespeare.txt'))