"""
1. input X, O, random?
2. who goes first?
3. save data and update table
4. check win?
5. result
6. play again?
_ _ _
| | | | 
- - -
| | | |
- - -
| | | |
"""

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Are you choosing X or O?').upper()

    if letter == 'X':
        return ['X', 'O'] # [player, bot]  
    else:
        return ['O', 'X'] 

#print(inputPlayerLetter()) # check!
def printWelcome():
    menu = """
    Menu:
    1. Choice X 
    2. Choice O
    3. Random
    4. Input            