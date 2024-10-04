import datetime
import os
from tkinter import *
import csv

root = Tk()
root.geometry("1000x600")
root.title("Bill Generator")
root.resizable(False, False)


def Reset():
    entry_Dosa.delete(0, END)
    entry_Idli.delete(0, END)
    entry_Poha.delete(0, END)
    entry_Upma.delete(0, END)
    entry_Pongal.delete(0, END)
    entry_Poori.delete(0, END)
    entry_Sandwich.delete(0, END)
    entry_Vada.delete(0, END)
    entry_total.delete(0, END)


def Total():
    try:
        a1 = int(Dosa.get())
    except:
        a1 = 0

    try:
        a2 = int(Idli.get())
    except:
        a2 = 0

    try:
        a3 = int(Poha.get())
    except:
        a3 = 0

    try:
        a4 = int(Upma.get())
    except:
        a4 = 0

    try:
        a5 = int(Pongal.get())
    except:
        a5 = 0

    try:
        a6 = int(Poori.get())
    except:
        a6 = 0

    try:
        a7 = int(Sandwich.get())
    except:
        a7 = 0

    try:
        a8 = int(Vada.get())
    except:
        a8 = 0

    # define cost of each item per quantity
    c1 = 50 * a1
    c2 = 20 * a2
    c3 = 30 * a3
    c4 = 25 * a4
    c5 = 25 * a5
    c6 = 30 * a6
    c7 = 25 * a7
    c8 = 30 * a8

    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
    string_bill = "Rs.", str('%.2f' % totalcost)
    Total_bill.set(string_bill)

    data = []
    if a1:
        data.append((Dosa, a1, c1))
    elif a2:
        data.append((Idli, a2, c2))
    elif a3:
        data.append((Poha, a3, c3))
    elif a4:
        data.append((Upma, a4, c4))
    elif a5:
        data.append((Pongal, a5, c5))
    elif a6:
        data.append((Poori, a6, c6))
    elif a7:
        data.append((Sandwich, a7, c7))
    else:
        data.append((Vada, a8, c8))

    # Writing to an excel
    import xlsxwriter

    dire = os.getcwd() + '\\data'
    bills = [f for r, d, f in os.walk(dire, topdown=True)][0]
    d = datetime.datetime.now()
    st = d.strftime('%d-%m-%Y %H-%M-%S')
    file_name = "Bill-" + str(st) + '.xlsx'

    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()

    total = 0
    for i in data[1:]:
        total += i[2]
    print(total)
    data.append(('Total', None, total))
    for row_num, row_data in enumerate(data):
        for col_num, col_data in enumerate(row_data):
            worksheet.write(row_num, col_num, col_data)

    workbook.close()


Label(text="BILL GENERATOR", bg="orange", fg="white", font=("times new roman", 33), width="300", height="2").pack()

# MENU CARD
f = Frame(root, bg="skyblue", highlightbackground="white", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)

Label(f, text="MENU", font=("times new roman", 40), fg="green", bg="skyblue").place(x=80, y=0)

Label(f, font=("times new roman", 15, 'bold'), text="Dosa...........Rs.50/plate", fg="black", bg="skyblue").place(x=10,
                                                                                                                  y=80)
Label(f, font=("times new roman", 15, 'bold'), text="Idli...........Rs.20/plate", fg="black", bg="skyblue").place(x=10,
                                                                                                                  y=110)
Label(f, font=("times new roman", 15, 'bold'), text="Poha...........Rs.30/plate", fg="black", bg="skyblue").place(x=10,
                                                                                                                  y=140)
Label(f, font=("times new roman", 15, 'bold'), text="Upma...........Rs.25/plate", fg="black", bg="skyblue").place(x=10,
                                                                                                                  y=170)
Label(f, font=("times new roman", 15, 'bold'), text="Pongal.........Rs.25/plate", fg="black", bg="skyblue").place(x=10,
                                                                                                                  y=200)
Label(f, font=("times new roman", 15, 'bold'), text="Poori..........Rs.30/plate", fg="black", bg="skyblue").place(x=10,
                                                                                                                  y=230)
Label(f, font=("times new roman", 15, 'bold'), text="Sandwich.......Rs.25/plate", fg="black", bg="skyblue").place(x=10,
                                                                                                                  y=260)
Label(f, font=("times new roman", 15, 'bold'), text="Vada...........Rs.30/plate", fg="black", bg="skyblue").place(x=10,
                                                                                                                  y=290)

# BILL

f2 = Frame(root, bg="skyblue", highlightbackground="white", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Bill = Label(f2, text="BILL", font=("times new roman", 20, 'bold'), bg="skyblue")
Bill.place(x=120, y=10)

# ENTRY WORK
f1 = Frame(root, height=370, width=300, relief=RAISED)
f1.place(x=310, y=118)

Dosa = StringVar()
Idli = StringVar()
Poha = StringVar()
Upma = StringVar()
Pongal = StringVar()
Poori = StringVar()
Sandwich = StringVar()
Vada = StringVar()
Total_bill = StringVar()

# LABEL
lbl_Dosa = Label(f1, font=("times new roman", 20, 'bold'), text="Dosa", width=12, fg="green")
lbl_Idli = Label(f1, font=("times new roman", 20, 'bold'), text="Idli", width=12, fg="green")
lbl_Poha = Label(f1, font=("times new roman", 20, 'bold'), text="Poha", width=12, fg="green")
lbl_Upma = Label(f1, font=("times new roman", 20, 'bold'), text="Upma", width=12, fg="green")
lbl_Pongal = Label(f1, font=("times new roman", 20, 'bold'), text="Pongal", width=12, fg="green")
lbl_Poori = Label(f1, font=("times new roman", 20, 'bold'), text="Poori", width=12, fg="green")
lbl_Sandwich = Label(f1, font=("times new roman", 20, 'bold'), text="Sandwich", width=12, fg="green")
lbl_Vada = Label(f1, font=("times new roman", 20, 'bold'), text="Vada", width=12, fg="green")
lbl_total = Label(f2, font=("times new roman", 20, 'bold'), text="Total", width=16, fg="green", bg="white")

lbl_Dosa.grid(row=1, column=0)
lbl_Idli.grid(row=2, column=0)
lbl_Poha.grid(row=3, column=0)
lbl_Upma.grid(row=4, column=0)
lbl_Upma.grid(row=4, column=0)
lbl_Pongal.grid(row=5, column=0)
lbl_Poori.grid(row=6, column=0)
lbl_Sandwich.grid(row=7, column=0)
lbl_Vada.grid(row=8, column=0)
lbl_total.place(x=20, y=50)

# ENTRY
entry_Dosa = Entry(f1, font=("times new roman", 20, 'bold'), textvariable=Dosa, bd=6, width=8, bg="pink")
entry_Idli = Entry(f1, font=("times new roman", 20, 'bold'), textvariable=Idli, bd=6, width=8, bg="pink")
entry_Poha = Entry(f1, font=("times new roman", 20, 'bold'), textvariable=Poha, bd=6, width=8, bg="pink")
entry_Upma = Entry(f1, font=("times new roman", 20, 'bold'), textvariable=Upma, bd=6, width=8, bg="pink")
entry_Pongal = Entry(f1, font=("times new roman", 20, 'bold'), textvariable=Pongal, bd=6, width=8, bg="pink")
entry_Poori = Entry(f1, font=("times new roman", 20, 'bold'), textvariable=Poori, bd=6, width=8, bg="pink")
entry_Sandwich = Entry(f1, font=("times new roman", 20, 'bold'), textvariable=Sandwich, bd=6, width=8, bg="pink")
entry_Vada = Entry(f1, font=("times new roman", 20, 'bold'), textvariable=Vada, bd=6, width=8, bg="pink")
entry_total = Entry(f2, font=("times new roman", 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg="pink")

entry_Dosa.grid(row=1, column=1)
entry_Idli.grid(row=2, column=1)
entry_Poha.grid(row=3, column=1)
entry_Upma.grid(row=4, column=1)
entry_Pongal.grid(row=5, column=1)
entry_Poori.grid(row=6, column=1)
entry_Sandwich.grid(row=7, column=1)
entry_Vada.grid(row=8, column=1)
entry_total.place(x=20, y=100)

# BUTTONS
btn_reset = Button(f1, bd=5, fg="black", bg="skyblue", font=("times new roman", 16, 'bold'), width=10, text="Reset",
                   command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="skyblue", font=("times new roman", 16, 'bold'), width=10, text="Total",
                   command=Total)
btn_total.grid(row=8, column=1)

root.mainloop()
