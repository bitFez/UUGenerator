# Ultimate Username Generator (uugenerator)
Simple Python Library to generate random usernames for websites.
Originally put together to integrate into a Django website that would create random usernames for a website aimed at students ensuring anonimity of where younger target audience may be the case.
The website is currently a work in progress: http://booqmarq.tk or bqmq.tk

## Collaboration
Would definitely welcome any help/ideas from others, especially in collating more lists.

## credit to
based on the idea of creating random usernames from https://jimpix.co.uk/ and another Python Library, http://pypi.org/project/random-username by williexu.

Lists taken from:
- https://www.listchallenges.com/
- nouns and adjectives taken from https://github.com/marstr/randname


## TODO
- ~~make default nouns list the generic list from marstr if no parameter is given~~
- ~~Add optional parameter to list a number of generated usernames~~
- ~~read all files from collections folder via a startup script as opposed to manually adding each list into the choices dictionary in the all_lists.py file.~~
- ~~consider limiting usernames to 12 characters long~~
- Add optional parameter to choose maximum length of username
- Testing the module in test.PyPI has resulted in difficulties reading text files. Maybe convert to .py files & seperate files not needed to generate them from the distribution.
- upload as a library to PyPi
- Create help command to display list of options
- Clear up really obscure names from lists?
 