column = (input("Are you getting the timestamp, or the strength values? (Enter timestamp or values)"))
option = column[0]
if (option == 't'):
        x = 0
elif (option == 'v'):
        x = 1

file = open("C:\\Users\\Kemal\\Documents\\outfile.txt", 'r')
for aline in file:
	values = aline.split()
	print(values[x])
file.close()
