rap_list = open("all_girls_names.txt", 'r')
target = open('top_girls_names_real.txt', 'a')

with open("all_girls_names.txt") as myfile:
    content = myfile.readlines()

for line in content:
    line_array = line.split(",")
    for elem in line_array:
    	if len(elem) <= 1:
    		continue;
    	target.write(elem[0] + elem[2:] + ', ')

rap_list.close()
target.close()
