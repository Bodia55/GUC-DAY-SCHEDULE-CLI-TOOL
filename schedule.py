from tkinter import messagebox
import requests
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup, NavigableString, Tag
from collections import OrderedDict
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

schedule_url = 'https://student.guc.edu.eg/Web/Student/Schedule/GroupSchedule.aspx'
# username = str(input("Enter your username: "))
# password = str(input("Enter your password: "))

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

# Create a list of column headers
column_headers = ["First Slot", "Second Slot", "Third Slot", "Fourth Slot", "Fifth Slot"]

# Create a list of row headers
row_headers = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

# Create a table using a nested for loop
for i in range(1, 8):
    for j in range(1, 7):
        # Skip the first cell
        if i == 1 and j == 1:
            continue
        # Create the column headers in the first row
        elif i == 1:
            label = tk.Label(root, text=column_headers[j-2], padx=10, pady=10, relief=tk.RIDGE)
            label.grid(row=i+1, column=j+1, sticky=tk.NSEW)
        # Create the row headers in the first column
        elif j == 1:
            label = tk.Label(root, text=row_headers[i-2], padx=10, pady=10, relief=tk.RIDGE)
            label.grid(row=i+1, column=j+1, sticky=tk.NSEW)
        # Create the empty cells
        else:
            label = tk.Label(root, text="", padx=10, pady=10, relief=tk.RIDGE)
            label.grid(row=i+1, column=j+1, sticky=tk.NSEW)

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
    
    try:
    
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

        for i in range(1, 8):
            for j in range(1, 7):
                # Skip the first cell
                if i == 1 and j == 1:
                    continue
                # Create the column headers in the first row
                elif i == 1:
                    label = tk.Label(root, text=column_headers[j-2], padx=10, pady=10, relief=tk.RIDGE)
                    label.grid(row=i+1, column=j+1, sticky=tk.NSEW)
                # Create the row headers in the first column
                elif j == 1:
                    label = tk.Label(root, text=row_headers[i-2], padx=10, pady=10, relief=tk.RIDGE)
                    label.grid(row=i+1, column=j+1, sticky=tk.NSEW)
                # Create the empty cells
                else:
                    label = tk.Label(root, text=new_schedule[i-2][j-2], padx=10, pady=10, relief=tk.RIDGE)
                    label.grid(row=i+1, column=j+1, sticky=tk.NSEW)
                    
    except:
        
        messagebox.showerror("Error", "Something went wrong. Please check your credentials and try again.")
    
submit = tk.Button(root, text="Get schedule", command=get_schedule)
submit.grid(row=3, column=1)
        
root.mainloop()