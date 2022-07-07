documents = ['a', 'a one']

def tfidf(documents):
    import math
    
    res = set()
    
    words = []
    for string in documents:
        string_words = []
        string_words = string.split()
        words.append(string_words)   # [['a'], ['a', 'one']]
        
        
    for sublista in words:
        for elem in range(len(sublista)):
            if sublista[elem] not in res:
                res.add(sublista[elem])  # {'one', 'a'}
                res[elem] = 0
            else:
                res[elem] += 1
    
    return res

print(tfidf(documents))