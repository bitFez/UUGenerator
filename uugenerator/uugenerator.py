'''
For generateUN parameter, lChoice represents a chosen list to pull the random noun from:
	0 --> General Nouns
	1 --> Countries
	2 --> LOTR
	3 --> Star Wars
	4 --> Marvel 
	5 --> Harry Potter
	6 --> Toy Story

	The program can be run without a parameter and will default to the general nouns list.
	A second argument can be used to specify how many usernames to generate in a list.
'''
# importing modules
from random import randint, choice
from . all_lists import choices, getFiles, filesList
import sys

if sys.version_info < (3, 9):
    # importlib.resources either doesn't exist or lacks the files()
    # function, so use the PyPI version:
    import importlib_resources
else:
    # importlib.resources has files(), so use that:
    import importlib.resources as importlib_resources


# collecting lists of nouns and adjectives
nounsFile = open('nouns.txt', 'r')
nouns=list(nounsFile)
adjFile = open('adjectives.txt', 'r')
adjectives=list(adjFile)

getFiles() # loads lists of text files from the collections folder.

for i in filesList:
	print(f"{i} --> {filesList[i]}")

def generateUN(lChoice=0, requiredNumber=1):
	usernames = []
	while len(usernames) < requiredNumber:
		if lChoice == 0:
			noun = nouns[randint(0,len(nouns)-1)].rstrip()
		else:
			randNoun = len(choices[lChoice])
			noun = choices[lChoice][randint(0,randNoun-1)].rstrip()
		adj = adjectives[randint(0,len(adjectives)-1)].rstrip()
		num = randint(1,999)
		username = adj+noun+str(num)
		if len(username) <=12:
			usernames.append(username)
	
	if len(usernames)==1:
		usernames = usernames[0] # preventing the output from returning an array
	return usernames

# adding a new list
#from collectingDataFromLists import makelist
#makelist()