with open('text.txt','r') as firstfile, open('copy.txt','a') as secondfile:
    for line in firstfile:
    	secondfile.write(line)
with open('text.txt','r') as firstfile, open('copy.txt','w') as secondfile:
	for line in firstfile:
        	secondfile.write(line)
