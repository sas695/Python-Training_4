import os
import operator
import json

path=os.path.dirname(os.path.realpath(__file__)) + '/babies'

files=[]

for r,d,f in os.walk(path):
    for f1 in f:
        if '.txt' in f1:
            files.append(f1)
            
males_dict = {}
females_dict = {}

for file_name in files:
    #print('Reading ' + file_name + '..')
    with open(path +'/' + file_name) as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.split(',')
            if split_line[1] == 'F':
                new_count = int(split_line[2])
                name = split_line[0]
                if name in females_dict:
                    count=females_dict[name]
                    count=count + new_count
                    females_dict[name] = count
                else:
                    females_dict[name] = new_count
            else:
                new_count = int(split_line[2])
                name = split_line[0]
                if name in males_dict:
                    count= males_dict[name]
                    count = count + new_count
                    males_dict[name] = count
                else:
                    males_dict[name] = new_count
                    #print('Done with ' + file_name)
                    
sorted_males_dict = sorted(males_dict.items(), key=operator.itemgetter(1))
sorted_females_dict = sorted(females_dict.items(), key=operator.itemgetter(1))

count = 0
list_of_sorted_male_names = []
list_of_sorted_female_names = []

while count < 100:
    count += 1
    list_of_sorted_male_names.append(sorted_males_dict.pop())
    list_of_sorted_female_names.append(sorted_females_dict.pop())
    
final_dict = {'male' : list_of_sorted_male_names , 'female' : list_of_sorted_female_names}

#conversoin to json file
json_file = json.dumps(final_dict)
print(json_file)

