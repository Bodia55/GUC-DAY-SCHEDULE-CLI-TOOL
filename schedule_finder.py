import requests
from requests_ntlm import HttpNtlmAuth
from bs4 import BeautifulSoup, NavigableString, Tag
from collections import OrderedDict

schedule_url = 'https://student.guc.edu.eg/Web/Student/Schedule/GroupSchedule.aspx'
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

while (username.strip() == "" or password.strip() == ""):
    print("Username/Password Cannot Be Empty")
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))

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
    r = requests.get(schedule_url, auth=HttpNtlmAuth(username, password))
    if r.status_code != 200:
        print("An Error Occurred. Check Credentials And Try Again.")
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


day = str(input("Enter a day:"))
index = get_day_index(day)
if index == -1:
    print("Day Is Invalid. \n Try [saturday, sunday, monday, tuesday, wednesday, thursday]")
else:
    schedule = get_day_schedule(index)
    formatted_schedule = []
    for item in schedule:
        formatted_schedule.append(item.replace("\r\n\t\t\t\t\t\t\t\t\t\t\t\tTut\r\n\t\t\t\t\t\t\t\t\t\t\t\n", " Tut").replace("\r\n\t\t\t\t\t\t\t\t\t\t\t\tLab\r\n\t\t\t\t\t\t\t\t\t\t\t\n", " Lab"))
    print(formatted_schedule)