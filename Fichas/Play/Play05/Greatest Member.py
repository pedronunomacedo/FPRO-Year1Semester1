a_tuple = ('hyde', 'jekyll')
import string

def score_of_tuple(tup):
    score = 0
    for member in tup:
        if type(member) == tuple:
            score += score_of_tuple(member)
        else:
            for char in member:
                score += ord(char)
    
    return score

def greatest_member(a_tuple):
    highest_score = 0
    winner = ""
    for member in a_tuple:
        score = 0
        if type(member) == tuple:
            score += score_of_tuple(member)
        else:
            for char in member:
                score += ord(char)
        if (score > highest_score):
            highest_score = score
            winner = member
    return winner

print(greatest_member(a_tuple))