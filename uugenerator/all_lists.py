import os, glob


def getFiles():
	os.chdir('collections/') # change working directory to the collections folder
	global choices # allow to edit the dict outside of function
	global filesList
	noOfFiles = len(glob.glob('*.txt')) # counts number of txt files
	# print(f"No of files {noOfFiles}")
	num = 1 # initiate starting number for dict keys
	for file in glob.glob('*.txt'): # for ech item in the collections folder ending with '.txt'
		
		filenameEnd = file.index('.') # find where filename ends
		filename = file[0:filenameEnd] # extract the filename
		
		with open(file) as f:
			newlist = f.readlines()
			choices.update({num:list(newlist)})
		    
		filesList.update({num:filename}) # create file list for help command.
		num+=1 # increment number for the key
		
choices = {
	
}
filesList = {
	0:"General Nouns",
}