from openpyxl import load_workbook

wb = load_workbook("D:\\all_tech_revised_notes\\Core_python\\_23_File_Handling\\data\\Bill-13-07-2022.xlsx")
# Mention the sheet where the data can be entered,

sheet = wb["Sheet1"]
# Assign multiple values to data
import datetime

d = datetime.datetime.now()

bill_name = d.strftime('%d-%m-%Y-%H-%M-%S')

my_list = [(bill_name, None, None), ('Items', 'Quatity', 'Price'), ('Dosa', 5, 250), ('Idli', 5, 125), ('Poori', 5, 125),
           ('Vada', 5, 125)]
total = 0
for i in my_list[2:]:
    total += i[2]
print(total)
my_list.extend([('Total', None, total), (None, None, None)])
# data = [('Emp Id', 'Emp Name', 'Designation'),
#         (1, 'XYZ', 'Manager'),
#         (2, 'ABC', 'Consultant')]
# Append all rows
for i in my_list:
    sheet.append(i)
wb.save("Bill-13-07-2022.xlsx")
