alist = [('Best Picture', 'Moonlight'), ('Best Director', 'La La Land'), ('Best Actor', 'Manchester by the Sea'), ('Best Actress', 'La La Land'), ('Best Supporting Actor', 'Moonlight'), ('Best Supporting Actress', 'Fences'), ('Best Original Screenplay', 'Manchester by the Sea'), ('Best Original Score', 'La La Land')]

def academy_awards(alist):
    result = {}
    
    for category, winner in alist:
        if winner not in result.keys():
            result[winner] = 1
        else:
            result[winner] += 1
    
    return result


print(academy_awards(alist))