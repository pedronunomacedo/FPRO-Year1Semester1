def interleave(f1, f2):
    lines1 = []
    lines2 = []
    with open(f1, "r") as f1:
        for the_line in f1:
           lines1.append(the_line)
    with open(f2, "r") as f2:
        for the_line in f2:
           lines2.append(the_line)
    small = min([lines1, lines2], key=len)
    
    result = ''
    for i in range(len(small)):
        result += lines1[i]
        result += lines2[i]
    
    return result

print(interleave('shakespeare.txt', 'monty.txt'))