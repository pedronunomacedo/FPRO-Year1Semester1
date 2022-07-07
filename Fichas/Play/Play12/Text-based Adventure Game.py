def intro():
    print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.")
    print('A. Grab a nearby rock and throw it at the orc')
    print('B. Lie down and wait to be mauled')
    print('C. Run')
    prox = input()
    if prox in 'aA':
        rock()
    if prox in 'bB':
        print('Welp, that was quick. You died!')
    if prox in 'cC':
        run()

def rock():
    print('The orc is stunned, but regains control. He begins running towards you again.')
    print('A. Run')
    print('B. Throw another rock')
    print('C. Run towards a nearby cave')
    prox = input()
    if prox in 'aA':
        run()
    if prox in 'bB':
        print('The rock flew well over the orcs head. You missed. You died!')
    if prox in 'cC':
        cave()

def run():
    print('You run as quickly as possible.')
    print('A. Hide behind boulder')
    print('B. Trapped, so you fight')
    print('C. Run towards an abandoned town')
    prox= input()
    if prox in 'aA':
        print("You're easily spotted. You died!")
    if prox in 'bB':
        print("You're no match for an orc. You died!")
    if prox in 'cC':
        town()

def cave():
    print('Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?')
    x = input()
    if x in 'yY':
        spade = True
    else:
        spade = False
    print('What do you do next?')
    print('A. Hide in silence')
    print('B. Fight')
    print('C. Run')
    prox = input()
    if prox in 'aA':
        print('I think orcs can see very well in the dark, right? You died!')
    if prox in 'bB':
        if spade == 'True':
            print('As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!')
        else:
            print("You're defenseless. You died!")
    if prox in 'cC':
        print('The orc turns around and sees you running.')
        run()
        
def town():
    print('You notice a purple flower near your foot. Do you pick it up? Y/N')
    x = input()
    if x in 'yY':
        print('You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!')
    else:
        print('Maybe you should have picked up the flower. You died!')

intro()