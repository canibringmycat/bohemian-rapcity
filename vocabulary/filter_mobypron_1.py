rap_list = open("mobypron.txt", 'r')
target = open('mobypron_revised.txt', 'a')

with open("mobypron.txt") as myfile:
	content = myfile.readlines()

for line in content:
	curr_line = line.split(":")[0][1:]
	if ("-" in curr_line) or (" " in curr_line):
		continue;
	else:
		target.write(str(line))

rap_list.close()
target.close()
