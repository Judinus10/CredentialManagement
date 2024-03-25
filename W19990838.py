credit_range=[0,20,40,60,80,100,120]  #range of crdits
count=0 #count the number of times that the data entered
count_p=0  #count the number of times that outcome=progress
count_t=0  #count the number of times that outcome=progress_module trailer
count_r=0  #count the number of times that outcome=do not progress_module retriever
count_e=0  #count the number of times that outcome=exclude

def inputs(message):
    while True:
        try:
            credit= int(input(message))  
        except ValueError:  #checking that user enter a valid integer
            print("Integer required")
        else:
            if credit not in credit_range:   #checkinng the range of the pass
                print("Out of range")
            else:
                break
    return credit

while count==0:
    while True:
        try:
            mode=int(input("Hello \n For Student mode Enter '1' , For Staff mode Enter '2' \n Enter Here : "))  #asking user to choose the mode
        except ValueError:
            print("Please Enter 1 or 2")
        else:
            if int(mode)==1:
                while count!=1:
                    #ASKING INPUT FROM USER
                    Pass=inputs("Please enter your credit at PASS  : ")  #get an input from user for pass
                    defer=inputs("Please enter your credit at DEFER : ")  #get an input from user for defer
                    fail=inputs("Please enter your credit at FAIL  : ")  #get an input from user for fail
                    #CHECKING FOR TOTAL
                    total = Pass+defer+fail  #adding pass,defer,fail
                    if total!=120:  #checking for total
                        print("Total incorrect")
                        continue
                    #CHECKING FOR OUTCOME
                    if Pass==120:
                        status="Progress"
                    elif Pass==100:
                        status="Progress (module trailer)"
                    elif fail<80:
                        status="Do not progress(module retriever)"
                    else:
                        status="Exclude"
                    count+=1  #adding 1 to count for breaking the loop
                    print(status)
                break  #breaking the student mode
                

            elif int(mode)==2:
                reenter="y"  #creating a veriable and named as reenter
                mark=[]  #create an empty list (part2)
                student_data={}  #create an empty dictionary(part4)
                while reenter.lower()=="y":
                    try:
                        user_name=input("\nEnter your UOW user name : ")  #asking staff to enter student number (part4)
                        if user_name[0].lower()!="w" or len(user_name)!=8:
                            print("Enter a valid user name")
                            continue
                    except IndexError:
                        print("Enter a valid user name")
                        continue
                #ASKING INPUT FROM USER
                    Pass=inputs("Please enter your credit at pass  : ")#get an input from user for pass
                    defer=inputs("Please enter your credit at defer : ")#get an input from user for defer
                    fail=inputs("Please enter your credit at fail  : ")#get an input from user for pass fail
                #CHECKING FOR TOTAL
                    total=Pass+defer+fail  #adding pass,defer,fail
                    if total!=120:  #checking for the total is correct
                        print("Total incorrect")
                        continue
                #CHECKING FOR OUTCOME
                    if Pass==120:
                        count_p+=1
                        status="Progress"
                    elif Pass==100:
                        count_t+=1
                        status="Progress (module trailer)"
                    elif fail<80:
                        count_r+=1
                        status="Do not progress(module retriever)"
                    else:
                        count_e+=1
                        status="Exclude"
                    count+=1
                    print(status)

                    mark.append(f"{status} - {Pass},{defer},{fail}\n")  #insert credit in mark list (part2)
                    student_data[user_name]=str(status)+'-'+str(Pass)+','+str(defer)+','+str(fail) #inset in dictionary (part4)
                   
                    while total==120:
                        reenter=input("\nwould you like to Enter annother set of data ?\nEnter 'y' for yes or 'q' to quit and view result :")  #asking user to add more detatils or end the progrmming
                        if reenter.lower()=="y":
                            total-=120  #turning total=0 for loop the function
                            continue
                        elif reenter.lower()=="q":
                            print("-" *77)
                            print(f"Histogram\nProgress {count_p}: {'*'*count_p}")
                            print(f"Trailer  {count_t}: {'*'*count_t}")
                            print(f"Retriever{count_r}: {'*'*count_r}")
                            print(f"Excluded {count_e}: {'*'*count_e}")
                            print(f"\n{count} outcomes in total")
                            print("-"*77)
                        #printing the list called mark (part2)
                            print("\nPART 2 LIST\n")
                            for i in mark:
                                print(i,end="")
                        #part3
                                file=open("credit_data","tw") #create a file called credit data for writting purpose
                                file.writelines(mark)  #write in to the file
                                file.close()  #close the file
                        #printing the dictionary student_data
                            print("\nPART 4 DICTIONARY\n")
                            for key,value in student_data.items():
                                print(f"{key} : {value} ",end="")
                            break
                        else:
                            print("\nPlease enter 'y' or 'q'")
                            continue
                break        
  
            else:
                print("Please enter 1 or 2")
                continue
