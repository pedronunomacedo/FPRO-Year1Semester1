words = ['apple', 'apply', 'ape', 'april']

def longest_prefix(words):
    words_sorted = sorted(words) # ['apple', 'apply', 'ape', 'april']
    first = words_sorted[0] # primeiro elemento da lista words_sorted
    
    for word in words:
        if first not in word:
            first = first[:-1]
    
    return first

print(longest_prefix(words))