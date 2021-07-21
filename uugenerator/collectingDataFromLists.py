def makelist():
	names = []
	marvel = open('collections/toystory.txt', 'r')
	d = list(marvel)
	for i in range(0,len(d)):
		line = d[i]
		start = line.index(' ')
		name = line[start+1:-1]
		temp=''
		for j in name:
			if j !=' ':
				temp = temp+ j
		if temp not in names:
			names.append(temp)
	marvel.close()

	f = open('temp.txt', 'a')

	for i in names:
		nj = i+'\n'
		f.write(nj)
	f.close()