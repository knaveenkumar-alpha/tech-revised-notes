import csv


with open('D:\\all_tech_revised_notes\\all_packages.csv', 'r+') as fdata:
    data = fdata.readlines()
    print(data)
    print(len(data))