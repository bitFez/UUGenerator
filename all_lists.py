countries = open('collections/countries.txt', 'r')
lotr = open('collections/lotr.txt', 'r') 
starwars= open('collections/starwars.txt', 'r')
marvel= open('collections/marvel.txt', 'r')
harrypotter = open('collections/harrypotter.txt', 'r') 


choices = {
	1:list(countries),
	2:list(lotr),
	3:list(starwars),
	4:list(marvel),
	5:list(harrypotter),

}