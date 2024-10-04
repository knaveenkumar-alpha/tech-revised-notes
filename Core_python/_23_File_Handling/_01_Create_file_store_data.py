# fname = input('Enter a new file name:')
# my_file = open(fname, 'w')
#
# data = input("Enter text : ")
#
# my_file.write(data)
#
# my_file.close()
# print("---Completed")

import json
file_path = "D:\\all_tech_revised_notes\\Core_python\\_23_File_Handling\\data\\test_data.json"
with open(file_path, 'w') as f:
    data = {"Name": "Naveen",
            "Job": "Software",
            "Salary": 1000000}
    print(data, type(data))
    json_data = json.dumps(data)
    print(json_data, type(data))
    f.write(json_data)
    print("file write successfully complete")
