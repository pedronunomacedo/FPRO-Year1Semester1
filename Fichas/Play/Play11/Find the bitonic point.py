def bitonic_point(f):
    return max(f())

print(bitonic_point(lambda: [2, 6, 10, 25, 60, 30, 25, 10, 0]))