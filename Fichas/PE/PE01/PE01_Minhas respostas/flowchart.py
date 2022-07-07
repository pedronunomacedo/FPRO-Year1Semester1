i = int(input())
if (i % 2 != 1):
    print(i * i)
else:
    if (i % 7 == 0):
        if (i % 11 == 0):
            print(3 * i + 2)
        else:
            if (i % 3 == 0):
                if (i % 5 == 0):
                    print(-i)
                print(5 - i)
            print(0)
    else:
        print(i - 2)
