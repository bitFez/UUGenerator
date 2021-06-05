# nouns and adjectives taken from https://github.com/marstr/randname

# Most other lists taken from https://www.listchallenges.com/

'''
For generateUN parameter, lChoice represents a chosen list to pull the random noun from:
    0 --> General Nouns
    1 --> Countries
    2 --> LOTR
    3 --> Star Wars
    4 --> Marvel 
    5 --> Harry Potter

    The program can be run without a parameter and will default to the general nouns list.
    A second argument can be used to specify how many usernames to generate in a list.
'''
# importing modules
from random import randint, choice

# collecting lists
nounsFile = open('nouns.txt', 'r')
nouns=list(nounsFile)
adjFile = open('adjectives.txt', 'r')
adjectives=list(adjFile)

from all_lists import choices

def generateUN(lChoice=0, requiredNumber=1):
    usernames = []
    for i in range(0,requiredNumber):
        if lChoice == 0:
            noun = nouns[randint(0,len(nouns))].rstrip()
        else:
            randNoun = len(choices[lChoice])
            noun = choices[lChoice][randint(0,randNoun)].rstrip()
        adj = adjectives[randint(0,len(adjectives))].rstrip()
        num = randint(1,999)
        username = adj+noun+str(num)
        usernames.append(username)
    if len(usernames)==1:
        usernames = usernames[0] # preventing the output from returning an array
    return usernames

print(generateUN(1))