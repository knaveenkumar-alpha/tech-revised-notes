# import os
# import json
# import datetime
# import pytz
# import sys
# import time
#
#
# def Output(file):
#     f = open(file, "r")
#     return f.readlines()
#
#
# def getfile(filename):
#     data = {
#         "volume.txt": "/home/nityaobject/Desktop/prasanna/posttxt/volume.txt",
#         "volumespace.txt": "C:/Users/manne/Documents/test.txt"
#
#     }
#
#     if filename in data.keys():
#         return Output(data.get(filename))
#
#     else:
#         print("give proper file name")
#
#
# if __name__ == "__main__":
#     # filename= sys.argv[1]
#     filename = 'test.txt'
#     # fi = sys.argv[2]
#     # print(fi)
#     str1 = " "
#     data = getfile(filename)
#     print(data)
#     jsondata = json.loads(str1.join(data))
#
#     for i in jsondata:
#         time.sleep(30)
#         # print(i)
#         # print(i.keys())
#         if "time" in i.keys():
#             t_val = i.get("time")
#             t1 = t_val.replace('T', ' ')
#             t1 = t1.rstrip('Z')
#             datetime_tz = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
#             datetime_in_utc = datetime_tz.astimezone(pytz.utc)
#             date_UTC = datetime_in_utc.strftime('%Y-%m-%d %H:%M:%S %Z')
#
#             print(date_UTC)
#             # print(t_val)
# import datetime
#
# import xlsxwriter
#
#
# d = datetime.datetime.now()
# # st = d.strftime('%Y-%m-%d-%H-%m-%s')
# print(d, type(d))
# file_name = str(d) +".xls"
# print(file_name)
# workbook = xlsxwriter.Workbook(file_name)
# worksheet = workbook.add_worksheet()
#
# my_list = ('Dosa', 3)
#
# worksheet.write_row(0, 1, my_list)
# # worksheet.write_column(1, 0, my_list)
#
# workbook.close()
import os

import xlsxwriter
import datetime

d = datetime.datetime.now()
st = d.strftime('%d-%m-%Y')
file_name = "Bill-" + str(st) + '.xlsx'

dire = os.getcwd() + '\\data'
bills = [f for r, d, f in os.walk(dire, topdown=True)]
if file_name in bills:
    file_name = file_name
else:
    pass

bill_name = d.strftime('%d-%m-%Y-%H-%M-%S')

workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet()

my_list = [(bill_name, None, None), ('Items', 'Quatity', 'Price'), ('Dosa', 2, 100), ('Idli', 3, 75), ('Poori', 4, 100),
           ('Vada', 5, 125)]
total = 0
for i in my_list[2:]:
    total += i[2]
print(total)
my_list.extend([('Total', None, total), (None, None, None)])
for row_num, row_data in enumerate(my_list):
    for col_num, col_data in enumerate(row_data):
        worksheet.write(row_num, col_num, col_data)

workbook.close()
