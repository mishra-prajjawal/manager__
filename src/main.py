from src import *
import json 
b=0
name  = input("Hi, what is your first name ?\n")
fname = name.split(" ") 
name = fname[0]
if __name__ == '__main__': 
    print("Hello ",name," make your choice ")
    while True: 
        greet(b)
        b = 1
        choice = input("Main\Program>>>")
        choice= (choice.lower()).strip()#extra bracket to make code snippet readable :) 
        if choice == "help": 
            help()
        elif choice == "end": 
            exit()
            break
            
#EMID, firstname, Designation, email, mobile number, address, gender, DOB, Joining date,Salary, Status, Department
        elif choice =="create":
            
            try:#if this is initial usage then obviously we need some initial unique id to auto increment after that value
                a = open("msdb.txt","r")
                f = a.readline()
                b = json.loads(f)
                Emid = b['Emid']
                #print(b['Emid'])
            except:# this is for initial value set if the file does not exists or it may exist but has nothing thus in that case we still need some key to start from
                Emid = input("Initial Employee ID: ")
            #no kill switch as this was done on purpose
            c=0;d=0
            Flname,Desig,MailE="","",""
            mobn,addre,gen="","",""
            dob,Jd,Salar="","",""
            Depart,worstat="",""
            while True: 
                if c ==0: 
                    q = input("Fullname of Employee:  ")
                    if q=="End": 
                        d=1
                        break
                    else:
                        Flname = q
                        c+=1
                elif c==1: 
                    q =input("Designation of Employee:  ")
                    if q=="End": 
                        d=1
                        break
                    else:
                        Desig = q
                        c+=1
                elif c==2: 
                    q = input("Email Address of Employee:  ")    
                    if q=="End": 
                        d=1
                        break
                    else:
                        MailE =q 
                        c+=1
                elif c==3: 
                    q =  input("Mobile Number of Employee:  ")
                    if q=="End": 
                        d=1
                        break
                    else:
                        mobn =q
                        c+=1
                elif c==4: 
                    q =input("Address of Employee:  ")
                    if q=="End": 
                        d=1   
                        break
                    else:
                        addre = q
                        c+=1
                elif c==5: 
                    q == input("Gender of Employee:  ")
                    if q=="End":    
                        d=1
                        break
                    else:
                        gen =q
                        c+=1
                elif c==6: 
                    q == input("Date Of Birth of Employee:  ")
                    if q=="End": 
                        d=1   
                        break
                    else:
                        dob = q
                        c+=1
                elif c==7: 
                    q == input("Joining Date of Employee:  ")
                    if q=="End":    
                        d=1
                        break
                    else:
                        Jd = q
                        c+=1
                elif c==8: 
                    q == input("Annual Salary of Employee:  ")
                    if q=="End":  
                        d=1  
                        break
                    else:
                        Salar = q
                        c+=1
                elif c==9: 
                    q == input("Current Working Satus of Employee for this company:   ")
                    if q=="End":
                        d=1    
                        break
                    else:
                        worstat = q
                        c+=1
                elif c==10: 
                    q == input("Department of Employee:  ")
                    if q=="End": 
                        d=1   
                        break
                    else:
                        Depart = q
                        c+=1
                else:
                    pass
                    break
            if d==0:
                create(Emid,Flname,Desig,MailE,mobn,addre,gen,dob,Jd,Salar,Depart,worstat)
            else: 
                continue
        elif choice == "time": 
            time_show()
        elif choice =="search": 
            a = "Emid,Flname,Desig,MailE,mobn,addre,gen,dob,Jd,Salar,Depart,worstat"
            data_set = a.split(",")
            search_by = input("Search By 'Value' for a unique value : ")
            if search_by in data_set: 
                print("<System-Failure> Value given is a data set Key Index, Please Provide an actual unique value to Search for")
                search_byy = input("Enter the specific unique value to search for:  ")
                search(search_byy)
            else:
                search(search_by)
        elif choice.split()==[]:# to work even if the person does not enter a letter and only gives a string
            continue
        elif choice  == "update": 
            seeach_by = input("Enter the detail of the employee to update the details:      ")
            a = search_f(seeach_by)
            #print(a)
            c=0 
            data_emp = {}
            Kswitch = 0 
            for i in a.values(): 
                if Kswitch == 0:
                    if c==0:
                        """ subject data {(1,): {'Emid': 102, 'flname': 'asda sdad', 'role': 'sada', 'mail_ID': 'd', 'mobile_number': 'asd', 'address': 'as', 'Gen': 'da', 'DOB': 'sda', 'DOJ': 'sd', 'Salary': 'as', 'Working-status': 'das', 'Department': 'dsa'}}"""
                        print("DATA found with the above search term, Loading all...")
                        c=1
                        #print(i)
                        data_emp = i.copy()
                    d=0
                    for k in i.items(): 
                        if d==0:
                            print("'"+str(k[0])+"'=>"+str(k[1]))
                            d=1
                            continue
                        ask_det = input(str(k[0])+"("+str(k[1])+")<-(old)[data change] New => ")#to change value 
                        if ask_det.strip() == "Help": 
                            print("Type 'Help'  to get help about 'update' method\nType 'Skip'   to skip the field and the data will not change\nType 'Blank'   to leave the field blank\nType 'Leave' to leave the entire row of a particular employee detail\nType 'KillAll'  to kill the operation and the data will not change")
                            Kswitch = 1
                            break
                        elif (ask_det.lower()).strip() == "skip": 
                            data_emp[k[0]] = k[1] 
                            continue
                        elif (ask_det.lower()).strip() =="blank": 
                            data_emp[k[0]] = "Null"
                        elif (ask_det.lower()).strip() == "leave": 
                            break
                        elif (ask_det.lower()).strip() == "killall":
                            Kswitch = 1
                            break
                        else:
                            data_emp[k[0]] = ask_det
                    if Kswitch == 0:
                        print(data_emp)
                        print("DATA Updated")
                    else:
                        pass
                else:
                    continue
        elif choice == "searchf":
            seeach_by = input("Enter the detail of the employee to update the details:      ")
            a = search_f(seeach_by)
            print(a)
        elif choice == "count": 
            a= count()
            print("Total Number of Employees in this organisation database/log file is => "+str(a))
        elif choice =="regreet":
            regreet()
        else:
            print("'"+choice+"' is not recognized as an internal command or operable program")
            continue


