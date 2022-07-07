def last_man_standing(alist, step):
    
    if len(alist) == 1:
        return alist[0]
    else:
        a = (step - 1) % len(alist)
        alist.remove(alist[a])
        
        alist = alist[a:] + alist[:a]
        
        return last_man_standing(alist, step)
    
print(last_man_standing(['Andre', 'Rui', 'Silva', 'Madalena', 'Leonor', 'Francisco', 'Filomena'], 7))