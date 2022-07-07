args = ('map', lambda x: 2*x, [1, 2, 3])



def reduce_map_filter(args):
    import functools
    
    if (type(args) == list):
        return args
    
    if (type(args[-1] == list)):
        
        if (args[0] == 'map'):
            return list(map(args[1], reduce_map_filter(args[-1])))
    
        elif (args[0] == 'filter'):
            return list(filter(args[1], reduce_map_filter(args[-1]))
                    
        elif (args[0] == 'reduce'):
            return functools.reduce(args[1], reduce_map_filter(args[-1]))
        
     
print(reduce_map_filter(args))