heroes = [{'name': 'Genos', 'health': 5500, 'category': 'S', 'score': 0}, {'name': 'King', 'health': 7000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}]
villain = {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}

def fight(heroes,villain):
    for person in heroes:
        if villain['category'] == person['category']:
            if villain['health'] > person['health']:
                villain['health'] = villain['health'] - (person['health'] / 2)

                
            elif person['health'] >= villain['health']:
                person['score'] += 1
                return f"{person['name']} defeated the villain and now has a score of {person['score']}"
    
    return f" {villain['name']} prevailed with {villain['health']}HP left"

print(fight(heroes, villain))