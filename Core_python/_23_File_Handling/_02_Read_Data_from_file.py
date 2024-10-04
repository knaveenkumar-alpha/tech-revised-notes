# my_file = open("C:/Users/naveen.kuruva/Desktop/sample.txt", 'r')
#
# # Read data from file
# str_1 = my_file.read()
#
# for each in str_1.split(" "):
#     if each == "appended":
#         print("Appended word exists in file")
#
# print("data to read from file ==> ", str_1)
#
# my_file.close()

file_path = "D:\\all_tech_revised_notes\\Core_python\\_23_File_Handling\\data\\test_data.txt"
with open(file_path, 'r') as f:
    data = f.readline()
    print(data)
    print(type(data))


