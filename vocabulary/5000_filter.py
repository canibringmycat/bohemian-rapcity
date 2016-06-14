rap_list = open("5000.txt", 'r')
target = open('5000_revised_list.txt', 'a')

with open("5000.txt") as myfile:
	content = myfile.readlines()

for line in content:
	word = line.split(" ")[3:][0].split('\t')[0]
	target.write(word + ", ")

rap_list.close()
target.close()
