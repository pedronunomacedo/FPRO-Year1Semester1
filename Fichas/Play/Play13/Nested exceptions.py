def nested_exceptions(tree):
    if callable(tree):
        try:
            tree()
        except:
            return True
        else:
            return False
    return tuple(map(nested_exceptions, tree))

print(nested_exceptions((lambda: 'a'+1)))
print(nested_exceptions((lambda: 1/0, (lambda: 0, (lambda: 1/0), lambda: 1/0))))