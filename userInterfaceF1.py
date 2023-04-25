import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
#ADD THIS
import mysql.connector
from PIL import ImageTk, Image

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

#loads bg image
image_path = "C:\\Users\\jglor\\Documents\\1- GitHub\\formulaOneDB\\F1Image.png"
image = Image.open(image_path)
image = image.resize((400,400))
photo = ImageTk.PhotoImage(image)
#adds image 
bg = tk.Label(root, image=photo)
bg.pack()

#create treeview
tv = ttk.Treeview(root)

variable1 = tk.StringVar(root)
variable1.set(options1[0])
menu1 = tk.OptionMenu(root, variable1, *options1)
menu1.place(x = 30, y = 95)

variable2 = tk.StringVar(root)
variable2.set(options2[0])
menu2 = tk.OptionMenu(root, variable2, *options2)
menu2.place(x = 150, y = 95)

variable3 = tk.StringVar(root)
variable3.set(options3[0])
menu3 = tk.OptionMenu(root, variable3, *options3)
menu3.place(x = 270, y = 95)

label = tk.Label(root, text='Show All')
label.place(x = 45, y = 70)

label2 = tk.Label(root, text='Basic Queries')
label2.place(x = 150, y = 70)

label3 = tk.Label(root, text='Advanced Queries')
label3.place(x = 270, y = 70)

title_label = tk.Label(root, text='F1 Database', font=('Arial', 24, 'bold'))
title_label.place(x=100, y=10)

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

        desc1 = tk.Label(win, text = 'Select * from driver')
        desc1.place(x = 0, y = 10) 

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

        desc1 = tk.Label(win, text = 'Select * from team')
        desc1.place(x = 0, y = 10) 

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

        desc1 = tk.Label(win, text = 'Select * from seasons')
        desc1.place(x = 0, y = 10) 

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

        desc1 = tk.Label(win, text = 'Select * from course')
        desc1.place(x = 0, y = 10) 

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

        desc1 = tk.Label(win, text = 'Select * from raceresults')
        desc1.place(x = 0, y = 10) 

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

        desc1 = tk.Label(win, text = 'Select * from sponsors')
        desc1.place(x = 0, y = 10) 

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

        desc1 = tk.Label(win, text = 'Select * from teamstandings')
        desc1.place(x = 0, y = 10) 

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

        desc1 = tk.Label(win, text = 'Select * from driverstandings')
        desc1.place(x = 0, y = 10) 

        tv.heading(1, text="driver_standing_ID")
        tv.heading(2, text="year")
        tv.heading(3, text="place")
        tv.heading(4, text="total_points")

        for x in data:
            tv.insert('', 'end', values=x)

#BUTTON 2 BASIC QUERIES
def show_selected2():
    selected2 = variable2.get()
    win = Tk()
    win.geometry('800x400')
    win.title('Basic Queries')
    frm = Frame(win)
    frm.pack(side=tk.LEFT, padx=5)

    if(selected2 =="Query 1"):
        win.geometry('1150x400')
        mycursor.execute("SELECT * FROM DRIVER order by SEASON_POINTS asc;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4,5,6,7,8,9,10,11), show="headings", height="15") 
        
        i = 1
        while i < 12:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'SELECT * FROM DRIVER order by SEASON_POINTS asc;')
        desc1.place(x = 0, y = 10) 

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
    elif(selected2 == "Query 2"):
        win.geometry('450x400')
        
        mycursor.execute("Select team_ID, wins, team_points, championship_count from team where team_points > 500 order by team_points desc;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="15")
        i = 1
        while i < 5:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'Select team_ID, wins, team_points, championship_count from team where team_points > 500 order by team_points desc;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="team_ID")
        tv.heading(2, text="wins")
        tv.heading(3, text="team_points")
        tv.heading(4, text="championship_count")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected2 == "Query 3"):
        win.geometry('200x200')
        
        mycursor.execute("Select driver_Num from driver where birth_Country = 'Saudi Arabia' and championships > 0;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1), show="headings", height="5")
        tv.column('1', width=100)
        tv.pack()

        desc1 = tk.Label(win, text = 'Select driver_Num from driver where birth_Country = Saudi Arabia and championships > 0;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="driver_Num")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected2 == "Query 4"):
        win.geometry('450x400')
        
        mycursor.execute("Select * from course where total_length <= 200 and record_lap <= 115;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="15")
        i = 1
        while i < 5:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'Select * from course where total_length <= 200 and record_lap <= 115;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="num_of_laps")
        tv.heading(2, text="total_length")
        tv.heading(3, text="record_lap")
        tv.heading(4, text="location")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected2 == "Query 5"):
        win.geometry('200x200')
        
        mycursor.execute("Select sum(championships=0)*100/count(*) as NoChamps from driver;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1), show="headings", height="5")
        tv.column('1', width=100)
        tv.pack()

        desc1 = tk.Label(win, text = 'Select sum(championships=0)*100/count(*) as NoChamps from driver;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="NoChamps")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected2 == "Query 6"):
        win.geometry('200x200')
        
        mycursor.execute("Select count(distinct birth_Country) as NumCountries from driver;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1), show="headings", height="5")
        tv.column('1', width=100)
        tv.pack()

        desc1 = tk.Label(win, text = 'Select count(distinct birth_Country) as NumCountries from driver;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="NumCountries")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected2 == "Query 7"):
        win.geometry('200x200')
        
        mycursor.execute("Select count(*) from sponsors;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1), show="headings", height="5")
        tv.column('1', width=150)
        tv.pack()

        desc1 = tk.Label(win, text = 'Select count(*) from sponsors;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="Num of sponsors")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected2 == "Query 8"):
        win.geometry('450x400')
        
        mycursor.execute("Select team_Name, base, team_Chief, tech_chief from team where championship_count >= 10 order by championship_count asc;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="15")
        i = 1
        while i < 5:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'Select team_Name, base, team_Chief, tech_chief from team where championship_count >= 10 order by championship_count asc;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="team_Name")
        tv.heading(2, text="base")
        tv.heading(3, text="team_chief")
        tv.heading(4, text="tech_chief")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected2 == "Query 9"):
        win.geometry('400x400')
        
        mycursor.execute("Select last_Name, driver_num, podiums from driver order by podiums desc;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3), show="headings", height="15")
        i = 1
        while i < 4:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'Select last_Name, driver_num, podiums from driver order by podiums desc;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="last_Name")
        tv.heading(2, text="driver_Num")
        tv.heading(3, text="podiums")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected2 == "Query 10"):
        win.geometry('400x400')
        
        mycursor.execute("Select driver_Standing_ID, total_points, year from driverstandings where year < 2000 order by total_points desc;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3), show="headings", height="15")
        i = 1
        while i < 4:
            tv.column(i, width=110)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'Select driver_Standing_ID, total_points, year from driverstandings where year < 2000 order by total_points desc;')
        desc1.place(x = 0, y = 10)

        tv.heading(1, text="driver_Standing_ID")
        tv.heading(2, text="total_points")
        tv.heading(3, text="year")

        for x in data:
            tv.insert('', 'end', values=x)

#BUTTON 3 ADV QUERIES
def show_selected3():
    selected3 = variable3.get()
    win = Tk()
    win.geometry('800x400')
    win.title('Advanced Queries')
    frm = Frame(win)
    frm.pack(side=tk.LEFT, padx=5)
    
    if(selected3 =="Query 1A"):
        win.geometry('1150x400')
        mycursor.execute("SELECT first_name, last_name, driver_Num, season_points, ROW_NUMBER() OVER (ORDER BY season_points) row_num, CUME_DIST() OVER (ORDER BY season_points) cume_dist_val FROM driver;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4,5,6,7,8,9,10,11), show="headings", height="15") 
        
        i = 1
        while i < 12:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'SELECT first_name, last_name, driver_Num, season_points, ROW_NUMBER() OVER (ORDER BY season_points) row_num, CUME_DIST() OVER (ORDER BY season_points) cume_dist_val FROM driver;')
        desc1.place(x = 0, y = 10) 

        tv.heading(1, text="first_name")
        tv.heading(2, text="last_name")
        tv.heading(3, text="driver_Num")
        tv.heading(4, text="season_points")
        tv.heading(5, text="row_num")
        tv.heading(6, text="cume_dist_val")
     

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected3 == "Query 2A"):
        win.geometry('450x400')
        mycursor.execute("SELECT team_Name, team_ID, num_of_races, team_points, NTILE (4) OVER (ORDER BY team_points) bucket_no from seasons inner join team on team.year_of_comp = seasons.year_of_comp;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="15")
        i = 1
        while i < 5:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'SELECT team_Name, team_ID, num_of_races, team_points, NTILE (4) OVER (ORDER BY team_points) bucket_no from seasons inner join team on team.year_of_comp = seasons.year_of_comp;')
        desc1.place(x = 0, y = 10) 

        tv.heading(1, text="team_Name")
        tv.heading(2, text="team_ID")
        tv.heading(3, text="num_of_races")
        tv.heading(4, text="team_points")
        tv.heading(5, text="quartile")

        for x in data:
            tv.insert('', 'end', values=x)
    elif(selected3 == "Query 3A"):
        win.geometry('450x400')
        mycursor.execute("SELECT event_date, location, fastest_lap, DENSE_RANK() OVER(ORDER BY fastest_lap asc) AS Ranks FROM raceresults ORDER BY Ranks;")
        data = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="15")
        i = 1
        while i < 5:
            tv.column(i, width=100)
            i += 1
        tv.pack()

        desc1 = tk.Label(win, text = 'SELECT event_date, location, fastest_lap, DENSE_RANK() OVER(ORDER BY fastest_lap asc) AS Ranks FROM raceresults ORDER BY Ranks;') 
        desc1.place(x = 0, y = 10) 

        tv.heading(1, text="event_date")
        tv.heading(2, text="location")
        tv.heading(3, text="fastest_lap")
        tv.heading(4, text="Ranks")

        for x in data:
            tv.insert('', 'end', values=x)


#Make buttons
button = tk.Button(root, text='Show selected', command=show_selected1)
button.place(x = 30, y = 145)
button = tk.Button(root, text='Show selected', command=show_selected2)
button.place(x = 150, y = 145)
button = tk.Button(root, text='Show selected', command=show_selected3)
button.place(x = 270, y = 145)

# Run the main loop
root.mainloop()