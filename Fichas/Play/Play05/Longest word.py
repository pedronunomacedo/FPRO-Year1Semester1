sentence = 'breakfast goodbye'
word_list = ['goodbye', 'hello', 'breakfast']

# sentence = 'dinosaur goodbye'
# word_list = ['goodbye', 'hello', 'breakfast']

def get_positions(sentence,word_list):
    position = ""
    words = sentence.split()
       # words = ['breakfast', 'goodbye']
    for a in range(0,len(words)):
        for b in range(0,len(word_list)):  
            if words[a] == word_list[b]:
                position += str(b) + " "
        if position == "":
            return ""
    
    return position

print(get_positions(sentence,word_list))