message = 'HELLO WORLD!'

import math

def caesar(message):
    MESSAGE = message.upper()
    ciphered_message = ""
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   # or ALPHABET = string.ascci_uppercase
    
    def fn(n):
        fn = int((((1+math.sqrt(5))**n) - ((1-math.sqrt(5))**n)) / ((2**n) * math.sqrt(5)))
        return fn
    
    for i in range(len(message)):
        fibo = fn(i)
        index_letter = ALPHABET.find(MESSAGE[i])
        if MESSAGE[i] == ' ':
            ciphered_message += ' '
        elif MESSAGE[i] == '!':
            ciphered_message += '!'
        elif MESSAGE[i] == '?':
            ciphered_message += '?'
        elif MESSAGE[i] == '.':
            ciphered_message += '.'
        elif MESSAGE[i] == ':':
            ciphered_message += ':'
        else:
            ciphered_message += ALPHABET[int(index_letter - fibo) % 26]
        
    return ciphered_message

print(caesar(message))