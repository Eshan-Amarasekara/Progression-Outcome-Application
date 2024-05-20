# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1999731 (IIT ID:20221570)
# Date: 21/04/2023

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
mode=0          # student or staff mode
pro_dict={}     #Empty dictionary for progression details
progress=()     #progress tuple  
num_range=["0","1","2","3","4","5","6","7","8","9"]
invalid="n"
#functions:
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
                        print("\nOut of range\n")
                        continue
                    else:
                        c_list.append(c)        #adding each input to the credit list
                        tot=tot+c
                        break
                except ValueError:
                    print("Integer required")   #only allowing integers
                    continue
        if tot!=120:        
            print("\nTotal incorrect\n")
            tot=0
            continue    
        else:
            tot_count+=1
            break


def pro_check():
    """Check progression status"""
    global progress,trailer,retriever,exclude
    if c_list[0] == 120:
        progress=("Progress - ",c_list)
        pro_dict[st_id]=c_list                  #adds the relevant "progress" data to the relevant student ID


    elif c_list[0] == 100:
        trailer=("Progress (Module Trailer) - ",c_list)
        pro_dict[st_id]=c_list

    elif c_list[2] >= 80:
        exclude=("Exclude - ",c_list)
        pro_dict[st_id]=c_list

    else:
        retriever=("Do not progress (Module Retriever) - ",c_list)
        pro_dict[st_id]=c_list

while run =="y":
    
# Student Id

    while True:
        st_id=input("Enter student ID, (format: wxxxxxxx) : ").lower()
        if len(st_id)!=8:                                   #https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths
            print("ID should contain 8 characters")
            continue
        if st_id[0]!="w":
            print("ID should start with 'w'")               # https://www.linode.com/docs/guides/how-to-slice-and-index-strings-in-python/
            continue
        for i in st_id[1:8]:
            if i not in num_range:
                print(i)
                print(st_id[1:8])
                invalid="y"
                break
        if invalid=="y":
            print("Invalid ID")
            continue
        if st_id in pro_dict:                                #Exisiting input error fix
            print("ID Already exists, Please enter again.\n")
            continue       
        else:                                                       
            break
            
    while run=="y":
        inputs()
        pro_check()
        break
                                                          
    run=input("Enter a new set of credits again or quit ? (y/q) :").lower()     #converts to lowercase
    print("")
    while run!="y" and run!="q":                                                #limit correct input
        print("Invalid input")
        run=input("Enter a new set of credits again or quit ? (y/q) :").lower()
        print()              
    
print("Part-4")

for key,value in pro_dict.items():      #Reads and prints student data
    print(key," : ",*value,end=" | ")   #https://medium.com/analytics-vidhya/the-magic-of-asterisks-in-python-aed3538deef9#:~:text=The%20asterisk%20(*)%20prefix%20in,of%20arguments%20into%20the%20function.
