a_string ='Str1nG$'

def count_chars(a_string):
    a = 0
    b = 0
    c = 0
    for i in str.lower(a_string):
        if i in "abcdefghijklmnopqrstuvwxyz":
            a += 1
        elif i in "0123456789":
            b += 1
        else:
            c += 1
        
    return (a,b,c)

print(count_chars(a_string))