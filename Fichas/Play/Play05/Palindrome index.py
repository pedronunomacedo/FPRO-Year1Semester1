s = 'tattarrattat'

def palindrome(a_string):
    p = False
    if a_string == a_string[::-1]:
        p = True
    return p


def palindrome_index(s):
    l = []
    if palindrome(s):
        return -1
    else:
        for i in s:
            l += [i]
        for index,j in enumerate(l):
            l_2 = l.copy()
            l_2.pop(index)
            a_string = "".join(l_2)
            if palindrome(a_string):
                return index
            l_2 = 1
    return -1
    

print(palindrome_index(s))