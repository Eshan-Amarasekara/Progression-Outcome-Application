# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1999731 (IIT ID:20221570)
# Date: 21/04/2023

import time    #https://www.programiz.com/python-programming/time
print()
print("-"*117)
print("""
░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀▀█ ░█▀▀▀█ ▀█▀ ░█▀▀▀█ ░█▄─░█ 　 ░█▀▀▀█ ░█─░█ ▀▀█▀▀ ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀ 
░█▄▄█ ░█▄▄▀ ░█──░█ ░█─▄▄ ░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ ─▀▀▀▄▄ ░█─ ░█──░█ ░█░█░█ 　 ░█──░█ ░█─░█ ─░█── ░█─── ░█──░█ ░█░█░█ ░█▀▀▀ 
░█─── ░█─░█ ░█▄▄▄█ ░█▄▄█ ░█─░█ ░█▄▄▄ ░█▄▄▄█ ░█▄▄▄█ ▄█▄ ░█▄▄▄█ ░█──▀█ 　 ░█▄▄▄█ ─▀▄▄▀ ─░█── ░█▄▄█ ░█▄▄▄█ ░█──░█ ░█▄▄▄      
""")        #https://fsymbols.com/generators/carty/
print("-"*117)
print()



#Variables: 
name_list=["PASS","DEFER","FAIL"]
pro_list=[]     # progression list
pro_total=0     # progress total
tr_total=0      # trailer total
re_total=0      # retriever total
ex_total=0      # exclude total
tot_count=0     # total entries
run="y"         # running mode
r_error=""      # range error
c_list=[]       # credit list
tot=0           # credit total 
mode=0         # student or staff mode

#functions:

def pro_check():
    """Check progression status"""
    if c_list[0] == 120:
        print("","-"*50,"\nProgress\n","-"*50)
        global pro_total                         #https://www.w3schools.com/python/python_variables_global.asp
        pro_total+=1
        pro_list.append(["Progress - ",c_list[0],", ",c_list[1],", ",c_list[2]])
        file.write("Progress - "+str(c_list[0])+", "+str(c_list[1])+", "+str(c_list[2])+"\n")

    elif c_list[0] == 100:
        print("","-"*50,"\nProgress (module trailer)\n","-"*50)
        global tr_total
        tr_total+=1
        pro_list.append(["Progress (module trailer) - ",c_list[0],", ",c_list[1],", ",c_list[2]])
        file.write("Progress (module trailer) - "+str(c_list[0])+", "+str(c_list[1])+", "+str(c_list[2])+"\n")

    elif c_list[2] >= 80:
        print ("","-"*50,"\nExclude\n","-"*50)
        global ex_total
        ex_total+=1
        pro_list.append(["Exclude - ",c_list[0],", ",c_list[1],", ",c_list[2]])
        file.write("Exclude - "+str(c_list[0])+", "+str(c_list[1])+", "+str(c_list[2])+"\n")

    else:
        print("","-"*50,"\nDo not progress - module retriever\n","-"*50)
        global re_total
        re_total+=1
        pro_list.append(["Do not progress - module retriever - ",c_list[0],", ",c_list[1],", ",c_list[2]])
        file.write("Do not progress - module retriever - "+str(c_list[0])+", "+str(c_list[1])+", "+str(c_list[2])+"\n")

def histogram():
    """Create histogram"""
    
    print("-"*50)
    print("Histogram\n")
    print("Progress  ",pro_total,"  :",pro_total*"*")
    print("Trailer   ",tr_total,"  :",tr_total*"*")
    print("Retriever ",re_total,"  :",re_total*"*")
    print("Exclude   ",ex_total,"  :",ex_total*"*")    
    print()
    print(tot_count,"outcomes in total.")
    print("-"*50)

def inputs():
    global c_list,tot,name_list,c,tot_count  #https://stackoverflow.com/questions/40992931/python-easiest-way-to-define-multiple-global-variables
    c_list=[]       
    tot=0
    while True:
        for i in name_list:
            while True:
                try:                   
                    c =int(input("Please enter your credit at "+str(i)+":"))
                    if c not in range (0,121,20):       #checking the input whether it"s in range or not
                        print("\nOut of range")
                        continue
                    else:
                        c_list.append(c)        #adding each input to the credit list
                        tot=tot+c
                        break
                except ValueError:
                    print("\nInteger required")   #only allowing integers
                    continue
        if tot!=120:        
            print("\nTotal incorrect")
            tot=0
            continue    
        else:
            tot_count+=1
            break

print("Student version        - 1\nStaff member version   - 2")
try:
    mode=int(input("Run with student version or staff member version ? (1/2) :")) #Choosing version
    print()
except ValueError:
    print("Please choose either 1 or 2")
print("Loading",end="")
time.sleep(1/2)
print(".",end="")
time.sleep(1/2)
print(".",end="")
time.sleep(1/2)
print(".")
time.sleep(1/2)
#Staff member version

if mode==2:
    #part 3 - File Handling
    file = open("ProgressionOutcome-staff.txt", "a")          #creating/opening file                                
    file.write("_"*50)
    file.write("\n")

    while run =="y":
        inputs()
        pro_check()     #call progression checking funcion and display

        run=input("Enter a new set of credits again or quit ? (y/q) :").lower()     #convert to lowercase
        print("")
        while run!="y" and run!="q":                                                #limit correct input
            print("Invalid input")
            run=input("Enter a new set of credits again or quit ? (y/q) :").lower()
            print()
            
    time.sleep(1)                                                                         
    histogram()                                             #call histogram funcion and display

    #Part 2 - List
    time.sleep(1)
    print("Part-2")
    for i in range (len(pro_list)):                         #prints the data from pro_list
        print(*pro_list[i],sep="")                       

    print()
    file.close()                                            #close the file

    #Part 3 - File Handling
    time.sleep(1)
    print("-"*50,"\nPart-3")                                                                 
    file = open("ProgressionOutcome-staff.txt", "r")
    print(file.read())                                      #reads and prints all the content in the file
    file.close()

#student mode
else:
    file = open("ProgressionOutcome-student.txt", "a")      #creating/opening file                                
    file.write("_"*50)
    file.write("\n")
    c_list=[]       
    tot=0
    while True:
        inputs()
        break

    pro_check()                                                 #call progression checking funcion and display

    #Part 2 - List
    time.sleep(1)
    print("Part-2")
    for i in range (len(pro_list)):                             #prints the data from pro_list
        print(*pro_list[i],sep="")                       

    print()
    file.close()                                                #close the file

    time.sleep(1)
    print("Part-3")                                                
    file = open("ProgressionOutcome-student.txt", "r")
    print(file.read())                                          #reads and prints all the content in the file
    file.close()
    open("ProgressionOutcome-student.txt", 'w').close()         #Erase history : https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python

print("Exiting",end="")
time.sleep(1/2)
print(".",end="")
time.sleep(1/2)
print(".",end="")
time.sleep(1/2)
print(".")
time.sleep(2)
