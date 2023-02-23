import requests
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup, NavigableString, Tag
from collections import OrderedDict

schedule_url = 'https://student.guc.edu.eg/Web/Student/Schedule/GroupSchedule.aspx'
# username = str(input("Enter your username: "))
# password = str(input("Enter your password: "))

import tkinter as tk
from tkinter import ttk
import tkinter.font as font
    
root = tk.Tk()
root.title("GUC Schedule")
root.configure(bg="#eeeeee")
root.geometry("3000x500")

username_label = tk.Label(root, text="username:", fg="black", bg="#eeeeee")
username_label.grid(row=0, column=0)
username = tk.Entry(root)
username.grid(row=0, column=1)

password_label = tk.Label(root, text="password:", fg="black", bg="#eeeeee")
password_label.grid(row=1, column=0)
password = tk.Entry(root, show="*")
password.grid(row=1, column=1)

#create a label for each day and each slot per day
saturday = tk.Label(root, text="Saturday", fg="black", bg="#aaaaaa")
saturday.grid(row=5, column=1)
sunday = tk.Label(root, text="Sunday", fg="black", bg="#aaaaaa")
sunday.grid(row=6, column=1)
monday = tk.Label(root, text="Monday", fg="black", bg="#aaaaaa")
monday.grid(row=7, column=1)
tuesday = tk.Label(root, text="Tuesday", fg="black", bg="#aaaaaa")
tuesday.grid(row=8, column=1)
wednesday = tk.Label(root, text="Wednesday", fg="black", bg="#aaaaaa")
wednesday.grid(row=9, column=1)
thursday = tk.Label(root, text="Thursday", fg="black", bg="#aaaaaa")
thursday.grid(row=10, column=1)
first = tk.Label(root, text="First Slot", fg="black", bg="#aaaaaa")
first.grid(row=4, column=2)
second = tk.Label(root, text="Second Slot", fg="black", bg="#aaaaaa")
second.grid(row=4, column=3)
third = tk.Label(root, text="Third Slot", fg="black", bg="#aaaaaa")
third.grid(row=4, column=4)
fourth = tk.Label(root, text="Fourth Slot", fg="black", bg="#aaaaaa")
fourth.grid(row=4, column=5)
fifth = tk.Label(root, text="Fifth Slot", fg="black", bg="#aaaaaa")
fifth.grid(row=4, column=6)
sat_1 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sat_1.grid(row=5, column=2)
sat_2 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sat_2.grid(row=5, column=3)
sat_3 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sat_3.grid(row=5, column=4)
sat_4 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sat_4.grid(row=5, column=5)
sat_5 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sat_5.grid(row=5, column=6)
sun_1 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sun_1.grid(row=6, column=2)
sun_2 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sun_2.grid(row=6, column=3)
sun_3 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sun_3.grid(row=6, column=4)
sun_4 = tk.Label(root, text="", fg="black", bg="#aaaaaa")   
sun_4.grid(row=6, column=5)
sun_5 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
sun_5.grid(row=6, column=6)
mon_1 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
mon_1.grid(row=7, column=2)
mon_2 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
mon_2.grid(row=7, column=3)
mon_3 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
mon_3.grid(row=7, column=4)
mon_4 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
mon_4.grid(row=7, column=5)
mon_5 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
mon_5.grid(row=7, column=6)
tue_1 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
tue_1.grid(row=8, column=2)
tue_2 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
tue_2.grid(row=8, column=3)
tue_3 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
tue_3.grid(row=8, column=4)
tue_4 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
tue_4.grid(row=8, column=5)
tue_5 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
tue_5.grid(row=8, column=6)
wed_1 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
wed_1.grid(row=9, column=2)
wed_2 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
wed_2.grid(row=9, column=3)
wed_3 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
wed_3.grid(row=9, column=4)
wed_4 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
wed_4.grid(row=9, column=5)
wed_5 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
wed_5.grid(row=9, column=6)
thu_1 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
thu_1.grid(row=10, column=2)
thu_2 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
thu_2.grid(row=10, column=3)
thu_3 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
thu_3.grid(row=10, column=4)
thu_4 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
thu_4.grid(row=10, column=5)
thu_5 = tk.Label(root, text="", fg="black", bg="#aaaaaa")
thu_5.grid(row=10, column=6)

def get_day_index(day_name: str):
    day_name = day_name.lower()
    index = -1
    if day_name == 'saturday':
        index = 0
    elif day_name == 'sunday':
        index = 1
    elif day_name == 'monday':
        index = 2
    elif day_name == 'tuesday':
        index = 3
    elif day_name == 'wednesday':
        index = 4
    elif day_name == 'thursday':
        index = 5
    return index

def get_day_schedule(day_index: int):
    day_schedule = []
    r = requests.get(schedule_url, auth=HttpNtlmAuth(username.get(), password.get()))
    soup = BeautifulSoup(r.content, 'html.parser')
    table: NavigableString = soup.find("table", id="scdTbl")
    children = table.findChildren("tr", recursive=False)
    children.pop(0)
    day = children[day_index]
    day_sessions = day.findChildren("td", recursive=False)
    for slot in day_sessions:
        tables = slot.findChildren("table", recursive=False)
        if len(tables) == 0:
            continue
        elif len(tables) == 1: #its a tutorial
            tut_infos = tables[0].findChildren("td", recursive=True)
            day_schedule.append(tut_infos[2].text)
        elif len(tables) > 1:
            table = tables[1]
            data = table.find("span")
            day_schedule.append(data.text)
    return day_schedule

def get_schedule():
    new_schedule = [[],[],[],[],[],[]]
    days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday"]
    for day in days:
        index = get_day_index(day)
        schedule = get_day_schedule(index)
        formatted_schedule = []
        for item in schedule:
            formatted_schedule.append(item.replace("\r\n\t\t\t\t\t\t\t\t\t\t\t\tTut\r\n\t\t\t\t\t\t\t\t\t\t\t\n", " Tut").replace("\r\n\t\t\t\t\t\t\t\t\t\t\t\tLab\r\n\t\t\t\t\t\t\t\t\t\t\t\n", " Lab"))
        new_schedule[index] = formatted_schedule
        if formatted_schedule == []:
            new_schedule[index] = ['Free', 'Free', 'Free', 'Free', 'Free']
        
    for i in range(len(days)):
        print(str(days[i]) + str(new_schedule[i]))

    sat_1.configure(text=new_schedule[0][0])
    sat_2.configure(text=new_schedule[0][1])
    sat_3.configure(text=new_schedule[0][2])
    sat_4.configure(text=new_schedule[0][3])
    sat_5.configure(text=new_schedule[0][4])
    sun_1.configure(text=new_schedule[1][0])
    sun_2.configure(text=new_schedule[1][1])
    sun_3.configure(text=new_schedule[1][2])
    sun_4.configure(text=new_schedule[1][3])
    sun_5.configure(text=new_schedule[1][4])
    mon_1.configure(text=new_schedule[2][0])
    mon_2.configure(text=new_schedule[2][1])
    mon_3.configure(text=new_schedule[2][2])
    mon_4.configure(text=new_schedule[2][3])
    mon_5.configure(text=new_schedule[2][4])
    tue_1.configure(text=new_schedule[3][0])
    tue_2.configure(text=new_schedule[3][1])
    tue_3.configure(text=new_schedule[3][2])
    tue_4.configure(text=new_schedule[3][3])
    tue_5.configure(text=new_schedule[3][4])
    wed_1.configure(text=new_schedule[4][0])
    wed_2.configure(text=new_schedule[4][1])
    wed_3.configure(text=new_schedule[4][2])
    wed_4.configure(text=new_schedule[4][3])
    wed_5.configure(text=new_schedule[4][4])
    thu_1.configure(text=new_schedule[5][0])
    thu_2.configure(text=new_schedule[5][1])
    thu_3.configure(text=new_schedule[5][2])
    thu_4.configure(text=new_schedule[5][3])
    thu_5.configure(text=new_schedule[5][4])
    
submit = tk.Button(root, text="Get schedule", command=get_schedule)
submit.grid(row=3, column=1)
        
root.mainloop()