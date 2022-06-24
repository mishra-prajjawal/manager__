"""
/*
 * Manage++ BY PRAJJAWAL MISHRA,
 * Copyright © 2022 Prajjawal Mishra <https://www.msaksham.com/go?id=1d2202>
*/
    Copyright © Msaksham Incorporated 
    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
    REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
    INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
    LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.
"""
#this software has not used the class object relation of python language. 
#function for initial greeting and guidance 
import json
import time
import sys
import random

def color_schema(type): 
    try:
        color = sys.stdout.shell
        return ["",""]
    except AttributeError:
        type = (type.lower()).strip()
        if type =="success": 
            return ['\33[92m','\33[0m']
        elif type == "time": 
            return ['\33[33m','\33[0m']
        elif type == "failure": 
            return ['\33[31m','\33[0m']
        elif type =="important": 
            return ['\33[41m','\33[0m']
        elif type=="data":
            return ['\33[36m','\33[0m']
        else: 
            return ['\33[30m','\33[0m']
def greet(i):
    if i == 0 :
        print("""
    Manage++ Company Management System CLI by Prajjawal Mishra
        type "help" for command line help 
        type "create" for creating a new employee data block 
        type "search" for finding an Employee from the details 
        type "count" for fetching total count of employees
        type "FDD" for finding details about a particular department 
        type "FTD" for fetching total count of employees in a department  
        type "End" for Ending work   
        
    (c) Manage++ by Prajjawal Mishra
    **Made for school project.** 
    **Details of the programmer** 
    --start--
    Zone -> New Delhi 
    Board -> CBSE  
    School -> The Air Force School, Subroto Park, Delhi Cantt, New Delhi 
    Class -> 12 
    Section -> E 
    Name -> Prajjawal Mishra 
    --end--
    """)
    else:
        pass
def help(): 
    print("""
help        for getting help related to the command line operation and functions  
create      for creating a new employee data block , i.e. new employee data storage
update      for updating any part of the employee detail  
search      for finding an Employee 
searchF     for finding an Employee and fetching employee details
count       for counting total employees  
FDD         for finding details about a particular department 
FTD         for fetching total count of employees in a department 
end         for ending the program
--Easters-- 
regreet     for initial greeting of the cli to user 
time        for getting the device time 
--functions-- 
create      for creating a new employee data block , i.e. new employee data storage
update      for updating any part of the employee detail 
search      for finding an Employee 
searchF     for finding an Employee and fetching employee details
count       for counting total employees 
FDD         for finding details about a particular department
FTD         for fetching total count of employees in a department
download    for creating a json based log file for data management 
--credits--
credits     for showing the credits of this program 
cert        for giving you a word of appreciation that you had seen and run this program   
    """)
# data set ordr DSO 
#EMID, firstname, Designation, email, mobile number, address, gender, DOB, Joining-date, Salary , Department , Status
def create(Emid,flname,Desi,Email,MobNum,Addre,Gen,Dob,Doj,Sal,Drep,Stat): 
    j=0
    try:
        b = open("msdb.txt", "r")
        for i in b: 
            j+=1   
        b.close()
    except:
        pass
    if  j < 1: 
        j =int(Emid)
    else: 
        j+=int(Emid)
    #print(Emid)
    a = open("./msdb.txt","a")
    
    x = {"Emid":j,"flname":flname,"role":Desi,"mail_ID":Email,"mobile_number": MobNum,"address":Addre,"Gen":Gen,"DOB":Dob,"DOJ":Doj,"Salary":Sal,"Working-status":Stat,"Department":Drep}
    fm_wrt = json.dumps(x)
    #b = open("msdb.txt", "r")
    #print(b.read())
    
    try:

        a.write(fm_wrt)
        a.write('\n')
        print("Employee details saved.")
        a.close()
    except:
        print("<System-Failure> Could not store the details.")
def time_show():
    a = time.localtime(time.time())
    color_lights = color_schema("time")
    print(color_lights[0]+"The current time is: "+time.strftime("%H:%M:%S",a)+color_lights[1])
    
def search(by):
    b = []
    try: 
        a = open("D:\python\mstack\msdb.txt","r")#path is according to my configuration, to adjust the path bring the file in the python program list to make the ide access the data file or you can add the full path so the ide can find the file 
        for i in a: 
            b.append(json.loads(i))
        print("data loaded")
    except: 
        print("<WHOOPS> System could not find/open the database/log file named 'msdb.txt' ")
        pass 
    det = 0
    c = ()
    found=0 #works like a padlock to double check if we actually found the data or not 
    data = {}
    for i in b:#classic triple looping to find the key value pair just from the values
        #print(i) these print statements are there to understand each loop in accordance to how it functions  
        #to count total lines covered
        
        for j in i.items(): 
            #print(j)
            for k in j:
                #print(k)
                if str(k).strip() ==str(by): 
                    det+=1 #making sure both belong to same class or there might be come clashes :>
                    c+=(det,)
                    data[c]= i
                    #print(i)
                    found=1
                    break
    if found == 1:
        color1 = color_schema("success")
        color2 = color_schema("data") 
        print(color1[0]+"found at line->",c,"<file='msdb.txt'>"+color1[1])
        for k in data.values(): 
            print(color2[0]+str(k)+color2[1])
    else: 
        color = color_schema("failure")
        print(color[0]+"No data found with '"+str(by)+"' detail or related to it."+color[1])
def search_f(by):
    b = []
    try: 
        a = open("D:\python\mstack\msdb.txt","r")#path is according to my configuration, to adjust the path bring the file in the python program list to make the ide access the data file or you can add the full path so the ide can find the file 
        for i in a: 
            b.append(json.loads(i))
        print("data loaded")
    except: 
        print("<WHOOPS> System could not find/open the database/log file named 'msdb.txt' ")
        pass 
    det = 0
    c = ()
    found=0 #works like a padlock to double check if we actually found the data or not 
    data = {}
    for i in b:#classic triple looping to find the key value pair just from the values
        #print(i) these print statements are there to understand each loop in accordance to how it functions  
        #to count total lines covered
        for j in i.items(): 
            #print(j)
            for k in j:
                #print(k)
                if str(k).strip() ==str(by): #making sure both belong to same class or there might be come clashes :>
                    det+=1 
                    c+=(det,)
                    data[c]= i
                    #print(i)
                    found=1
                    break
    
    if found == 1:
        a.close()
        color1 = color_schema("success")
        print(color1[0]+"found at line->",c,"<file='msdb.txt'>"+color1[1])
        return data
        
    else: 
        a.close()
        color = color_schema("failure")
        print(color[0]+"No data found with '"+str(by)+"' detail or related to it."+color[1])
        a.close()
def count(): 
    c=0 
    b = []
    try: 
        a = open("D:\python\mstack\msdb.txt","r")#path is according to my configuration, to adjust the path bring the file in the python program list to make the ide access the data file or you can add the full path so the ide can find the file 
        for i in a: 
            b.append(json.loads(i))
        print("data loaded")
        
    except: 
        print("<WHOOPS> System could not find/open the database/log file named 'msdb.txt' ")
        pass 
    for i in b:
        c+=1
    return c 
def regreet(): 
    loading_anime = [
    "[        ]",
    "[>       ]",
    "[==>     ]",
    "[===>    ]",
    "[====>   ]",
    "[=====>  ]",
    "[======> ]",
    "[<======>]",
    "[ <======]",
    "[  <=====]",
    "[   <====]",
    "[    <===]",
    "[     <==]",
    "[      <=]",
    "[       <]",
    "[        ]",
    "[        ]"
    ]

    till_load = True

    i = 0

    while till_load:
        print(loading_anime[i % len(loading_anime)], end='\r')
        time.sleep(.1)
        i += 1
        if i >=random.randint(64,70): 
            break
    print("""
Manage++ Company Management System CLI by Prajjawal Mishra
    type "help" for command line help 
    type "create" for creating a new employee data block 
    type "search" for finding an Employee from the details 
    type "count" for fetching total count of employees
    type "FDD" for finding details about a particular department 
    type "FTD" for fetching total count of employees in a department  
    type "End" for Ending work   
    
(c) Manage++ by Prajjawal Mishra
**Made for school project.** 
**Details of the programmer** 
--start--
Zone -> New Delhi 
Board -> CBSE  
School -> The Air Force School, Subroto Park, Delhi Cantt, New Delhi 
Class -> 12 
Section -> E 
Name -> Prajjawal Mishra 
--end--    
Hope you have a great day of work, 
Thank you for using our software.
---Type 'help' for command line help---
        """)
