import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
#ADD THIS
import mysql.connector

# Create a database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="DATABASEmanagement!",
  database="f1Data"
)
# Create a cursor object
mycursor = mydb.cursor()

# Create the main window
root = tk.Tk()
root.geometry('400x400')
root.title('F1 Database')

# Create the drop-down menus
options1 = ['Drivers', 'Teams', 'Seasons', 'Courses', 'Race Results', 'Sponsors', 'Team Standings', 'Driver Standings']
options2 = ['Query 1', 'Query 2', 'Query 3', 'Query 4', 'Query 5', 'Query 6', 'Query 7', 'Query 8', 'Query 9', 'Query 10']
options3 = ['Query 1A', 'Query 2A', 'Query 3A']

#create treeview
tv = ttk.Treeview(root)

variable1 = tk.StringVar(root)
variable1.set(options1[0])
menu1 = tk.OptionMenu(root, variable1, *options1)
menu1.place(x = 50, y = 75)

variable2 = tk.StringVar(root)
variable2.set(options2[0])
menu2 = tk.OptionMenu(root, variable2, *options2)
menu2.place(x = 150, y = 75)

variable3 = tk.StringVar(root)
variable3.set(options3[0])
menu3 = tk.OptionMenu(root, variable3, *options3)
menu3.place(x = 250, y = 75)

label = tk.Label(root, text='Show All')
label.place(x = 65, y = 50)

label2 = tk.Label(root, text='Basic Queries')
label2.place(x = 150, y = 50)

label3 = tk.Label(root, text='Advanced Queries')
label3.place(x = 250, y = 50)

title_label = tk.Label(root, text='F1 Database', font=('Arial', 24, 'bold'))
title_label.pack(side='top', padx=10, pady=10)

# BUTTON FUNCTIONS
#BUTTON 1 SHOW ALL
def show_selected1():
    selected1 = variable1.get()
    win = Tk()
    win.geometry('1150x400')
    win.title('Tables')
    frm = Frame(win)
    frm.pack(side=tk.LEFT, padx=5)

    if(selected1 == "Drivers"):
        mycursor.execute("SELECT * FROM DRIVER")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4,5,6,7,8,9,10,11), show="headings", height="15") 
        i = 1
        while i < 12:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        #clear table
        for item in tv.get_children():
            tv.delete(item)

        tv.heading(1, text="driver_Num")
        tv.heading(2, text="last_Name")
        tv.heading(3, text="first_Name")
        tv.heading(4, text="racing_Country")
        tv.heading(5, text="birth_Country")
        tv.heading(6, text="DOB")
        tv.heading(7, text="highest_grid")
        tv.heading(8, text="highest_finish")
        tv.heading(9, text="podiums")
        tv.heading(10, text="season_points")
        tv.heading(11, text="championships")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected1 == "Teams"):
        win.geometry('1050x400')

        mycursor.execute("SELECT * FROM TEAM")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="15")
        i = 1
        while i < 11:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        #clear table
        for item in tv.get_children():
            tv.delete(item)

        tv.heading(1, text="team_Name")
        tv.heading(2, text="team_ID")
        tv.heading(3, text="team_points")
        tv.heading(4, text="base")
        tv.heading(5, text="team_chief")
        tv.heading(6, text="tech_chief")
        tv.heading(7, text="chassis")
        tv.heading(8, text="engine")
        tv.heading(9, text="championship_count")
        tv.heading(10, text="wins")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected1 == "Seasons"):
        win.geometry('300x400')

        mycursor.execute("SELECT * FROM SEASONS")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2), show="headings", height="15")
        i = 1
        while i < 3:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        #clear table
        for item in tv.get_children():
            tv.delete(item)

        tv.heading(1, text="num_of_races")
        tv.heading(2, text="year_of_comp")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected1 == "Courses"):
        win.geometry('600x400')
        
        mycursor.execute("SELECT * FROM COURSE")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4,5), show="headings", height="15")
        i = 1
        while i < 6:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        #clear table
        for item in tv.get_children():
            tv.delete(item)

        tv.heading(1, text="location")
        tv.heading(2, text="record_lap")
        tv.heading(3, text="num_of_laps")
        tv.heading(4, text="total_length")
        tv.heading(5, text="event_date")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected1 == "Race Results"):
        win.geometry('600x400')
        
        mycursor.execute("SELECT * FROM raceresults")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4,5), show="headings", height="15")
        i = 1
        while i < 6:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        #clear table
        for item in tv.get_children():
            tv.delete(item)

        tv.heading(1, text="event_date")
        tv.heading(2, text="fastest_lap")
        tv.heading(3, text="laps")
        tv.heading(4, text="points_awarded")
        tv.heading(5, text="finishing_Place")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected1 == "Sponsors"):
        win.geometry('400x400')
        
        mycursor.execute("SELECT * FROM SPONSORS")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3), show="headings", height="15")
        i = 1
        while i < 4:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        #clear table
        for item in tv.get_children():
            tv.delete(item)

        tv.heading(1, text="sponsor_ID")
        tv.heading(2, text="company_Name")
        tv.heading(3, text="sponsor_website")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected1 == "Team Standings"):
        win.geometry('400x400')
        
        mycursor.execute("SELECT * FROM TEAMSTANDINGS")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3), show="headings", height="15")
        i = 1
        while i < 4:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        #clear table
        for item in tv.get_children():
            tv.delete(item)

        tv.heading(1, text="team_standing_ID")
        tv.heading(2, text="ranking")
        tv.heading(3, text="year")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected1 == "Driver Standings"):
        win.geometry('450x400')
        
        mycursor.execute("SELECT * FROM DRIVERSTANDINGS")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="15")
        i = 1
        while i < 5:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        #clear table
        for item in tv.get_children():
            tv.delete(item)

        tv.heading(1, text="driver_standing_ID")
        tv.heading(2, text="year")
        tv.heading(3, text="place")
        tv.heading(4, text="total_points")

        for x in data:
            tv.insert('', 'end', values=x)

#BUTTON 2 BASIC QUERIES
def show_selected2():
    selected2 = variable2.get()
    print(f'Selected options: {selected2}')


    mycursor.execute("SELECT * FROM driver;")
    data = mycursor.fetchall()

    frm = Frame(root)
    frm.pack(side=tk.LEFT, padx=5)

    tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="5")
    tv.pack()

    tv.heading(1, text="Name")
    tv.heading(2, text="CRN")
    tv.heading(3, text="ID Num")
    tv.heading(4, text="Year")

    for x in data:
        tv.insert('', 'end', values=x)

#BUTTON 3 ADV QUERIES
def show_selected3():
    selected3 = variable3.get()
    print(f'Selected options: {selected3}')

#Make buttons
button = tk.Button(root, text='Show selected', command=show_selected1)
button.place(x = 50, y = 125)
button = tk.Button(root, text='Show selected', command=show_selected2)
button.place(x = 150, y = 125)
button = tk.Button(root, text='Show selected', command=show_selected3)
button.place(x = 250, y = 125)

# Run the main loop
root.mainloop()