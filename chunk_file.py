import os
import json
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__)) # Root directory for the folder
file = "10kSample-json.json" #Name of the file
file_path = os.path.join(dir_path,file) # you need to add you path here

new_file_name= "Testing" # The name of the output file
size_of_the_split= 3000 #Number of each row
key_names = ["Sheet1","Sheet2","Sheet3"] # Key for the array 
# key_name2 =  # Key for the array 
# Reading the json file
with open(file, 'r', encoding='utf-8-sig') as f1:
    line = []
    datas = json.load(f1)
    # print(datas)
    for key_name in key_names:
        for data in datas[key_name]:
            # Putting each line into the array
            # {'Serial Number': '9788189999599', 'Company Name': 'TALES OF SHIVA', 'Employee Markme': 'Mark', 'Description': 'mark', 'Leave': '0'}
            # print(data)
            line.append(data)

    
# this is the total length size of the json file
    print(len(line))

# in here 2000 means we getting splits of 2000 tweets
# you can define your own size of split according to your need
total = len(line) // size_of_the_split


# in here you will get the Number of splits
print(total+1)
for key_name in key_names:
    for i in range(total+1):
        json.dump(line[i * size_of_the_split:(i + 1) * size_of_the_split-1], open(
            f"{dir_path}/{key_name}-" + str(i+1) + ".json", 'w',
            encoding='utf8'), ensure_ascii=False, indent=True)

# in here you need to provide the number spilts

for i in range(0,total+1):
    for key_name in key_names:
        id =i+1
        print(id)
        print(key_name)

        json_file =f"{key_name}-{id}.json"
        csv_file =f"{key_name}-{id}.csv"
        df = pd.read_json(json_file)
        df.to_csv (csv_file, index = None)

