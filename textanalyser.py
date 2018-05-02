

def count(passage, character):
	counter = 0
	for c in passage:
		if c == character:
			counter+=1
	return counter




file = input('filename: ')

with open(file, 'r', encoding='utf-8') as f: #remember, the word 'file' here is a variable, not a string!!! 
	text = f.read()




#u=count(text, 'a')
#print(u)
#print(len(text))
#print(u/len(text))


total=0 #NEVER PUT THIS STATEMENT IN THE FOR LOOP BELOW!!!!!!!!!!!

for i in "abcdefghijklmnopqrstuvwxyz":
	j=count(text, i)
	k=len(text)
	perc = 100 * j/k
	total= total + perc
	#print(total)
	print("{0} - {1}%".format(i, round(perc, 1)))

print()
print('the total is {0}%'.format(round(total, 1)))