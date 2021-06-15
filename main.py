print("\n" * 5)                  #Starting after 5x empty lines.

import datetime                    #Deltatime library, to get Real Date information.
import os                          #OS (Operating system) , To provide cross-platform compatibility
import sqlite3
conn=sqlite3.connect('database.db')

list_foods = []                    #Variable List of foods, names + prices.
list_price = []                   #Variable List of drinks, names + prices.
list_services = []                 #Variable List of other services, names + prices.
log=[0,'None','None']
list_item_price = [0] * 100        #Variable List of item prices. Index: 0-39 for foods, index: 40-79 for drinks,
                                   #Index: 80-99 for other services.
var_discount_1 = 200                      #First discount starts.
var_discount_2 = 1000                     #Second discount starts.
var_discount_3 = 5000                     #Third discount starts.
var_discount_1_rate = 0.05                #First discount rate.
var_discount_2_rate = 0.10                #Second discount rate.
var_discount_3_rate = 0.15                #Third discount rate.


navigator_symbol = "/" # This will make the program runnable on any unix based enviroument because it has differnet file system
if os.name == "nt":
    navigator_symbol = "\\" # This will make the program runnable on Windows


def def_default():
    global list_foods, list_services, list_item_order, list_item_price     
    list_item_order = [0] * 100                    #Create a list, length 100. Max index number is 99.
def_default()                                      #Index: 0-39 for foods, index: 40-79 for drinks,
                                                   #Index: 80-99 for other services. Global variables.
def def_login():
    use_id=str(input("Enter User Id \t\t"))
    user_password=str(input('Enter User Password \t'))
    cursor=conn.execute("SELECT * FROM LOGIN")
    for row in cursor:
        if( use_id== row[0]):
            if(user_password==row[2]):
                log[0]=1
                log[1]=row[1]
                log[2]=row[0]
                break
            print('username or password not match')
            break
    

def def_sigin():
    userid=str(input('Enter You email: \t'))
    name=str(input('Enter Your Name: \t'))
    passcode=str(input('Enter Your Password:\t'))
    conn.execute('INSERT INTO LOGIN VALUES("'+str(userid)+'","'+str(name)+'","'+str(passcode)+'")')
    conn.commit()
    print("*" * 30 + "Successfully Created" + "*" * 25 + "\n")

    

def def_main():
    while True:
        if(log[0]==0):

            print("*" * 31 + "Food Odering" + "*" * 30 + "\n")
            print("\t(L) Login\n")
            print("\t(S) Sign In\n")
            input_1=str(input(" Please Select Your operation: ")).upper()
            
            if (len(input_1) == 1):                                           #Checking input length.
                if (input_1 == 'L'):                                          #If input is "O".
                    print("\n" * 10)                                         #Create 100 empty lines.
                    def_login()                                          #Start Order Menu function.
                    continue                                                     #Stop repeating Main Menu.
                elif (input_1 == 'S'):                                        #If input is "R".
                    print("\n" * 10)                                         #Create 100 empty lines.
                    def_sigin()                                              #Start Report function.
                    continue                                                     #Stop repeating Main Menu.                                                  #Stop repeating Main Menu.
                else:                                                                                 #If O, R, P, E not inserted then...
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")     #Invalid input.
            else:                                                                                     #If input length not equal to 1...
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")         #Invalid input.
        else:
                
            print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     #Design for Main Menu.
                "\t(O) ORDER\n"                              #"*" * 31 means, write (*) 31 times.
                "\t(R) REPORT\n"
                "\t(E) EXIT\n" +
                "_" * 72)

            input_1 = str(input(str(log[1])+ " Select Your Operation: ")).upper()    #Input, have to choose operation. Make everything UPPER symbol.
            if (len(input_1) == 1):                                           #Checking input length.
                if (input_1 == 'O'):                                          #If input is "O".
                    print("\n" * 10)                                         #Create 100 empty lines.
                    def_food_drink_order()                                        #Start Order Menu function.
                    break                                                     #Stop repeating Main Menu.
                elif (input_1 == 'R'):                                        #If input is "R".
                    print("\n" * 10)                                         #Create 100 empty lines.
                    def_report()                                              #Start Report function.
                    break                                                     #Stop repeating Main Menu.                                                    #Stop repeating Main Menu.
                elif (input_1 == 'E'):                                        #If input is "E".
                    print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")           #Good bye comment.
                    break                                                     #Stop repeating Main Menu.
                else:                                                                                 #If O, R, P, E not inserted then...
                    print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")     #Invalid input.
            else:                                                                                     #If input length not equal to 1...
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")         #Invalid input.


def def_file_sorter(): # Applying Sorting to the array to be sorted from A-Z ASC ((AND)) Extracting out prices after sorting and appending them to a prices array accordingly to a parrallel indexes
    global list_foods, list_services
    list_foods = sorted(list_foods)
    # list_drinks = sorted(list_drinks)
    list_services = sorted(list_services)

    i = 0
    while i < len(list_foods):
        list_item_price[i] = float(list_foods[i][int(list_foods[i].index("RM") + 3):]) # Extracting Out "RM" + [SPACE] from and cast out the string into an integer
        i += 1

    i = 0
    # while i < len(list_drinks):
    #     list_item_price[40 + i] = float(list_drinks[i][int(list_drinks[i].index("RM") + 3):]) # Applying extraction on 40 and above items which are the drinks
    #     i += 1

    i = 0
    while i < len(list_services):
        list_item_price[80 + i] = float(list_services[i][int(list_services[i].index("RM") + 3):]) # Applying extraction on 80 and above items wich are Services
        i += 1
def_file_sorter()

def def_food_drink_order():
    while True:
            print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
            print(" |NO| |FOOD NAME| \t\t |PRICE|   ")
            food_menu_list=conn.execute('select * from menu')
            list_foods.clear()
            list_price.clear()
            for row in food_menu_list:
                list_foods.append(row[0])
                list_price.append(row[1])
            i = 0
            while i < len(list_foods) :
                # var_space = 1
                # if i <= 8:                      # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                #     var_space = 2

                # if i < len(list_foods):
                #     food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + " \t\t "+ # Styling out the index number for the food or item and starting out from 1 for better human readability
                # else:
                #     food = " " * 36 + "| " # 36 is a constant for indention in console to fixup list in print
                print("  "+str(i+1)+" .   "+str(list_foods[i])+" \t\t\t   "+str(list_price[i]))
                i += 1
            print("*"*61)
            print("\n (M) MAIN MENU                   (C) Check                   (E) EXIT\n" + "_" * 72)

            input_1 = input(str(log[1])+" Select Your Operation: ").upper() #Handling Menu Selection
            if (input_1 == 'M'):
                print("\n" * 3)
                def_main() # Return to main menu by calling it out
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") # Handling Exit and print out thank you
                break
            if (input_1 == 'C'):
                print("\n" * 3)
                def_payment(list_price)
                break
            try:        #Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0)):
                     try:
                        print("\n" + "_" * 72 + "\n") # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                     except:
                        pass
                     input_2 = input("How Many "+str(list_foods[int(input_1) - 1])+" You Want to Order?: ").upper() # Handling Quantity input
                     if int(input_2) > 0:
                        list_item_order[int(input_1) - 1] += int(input_2) # adding item to Orders Array
                        print("\n" * 3)
                        print("Successfully Added")
                        def_food_drink_order() # Return food/drinks Menu
                        break
                     else:
                        print("\n" * 3 + "bbERROR: Invalid Input (" + str(input_2) + "). Try again!")
            except:
                print("\n" * 3 + "aaERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_report():
    while True:
        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
        rep_data=conn.execute('select * from order_hist')
        print("Bill No\t\t    Total Amount\t Date Time\t        User Id")
        for rep in rep_data:
            
            print(str(rep[0])+"\t"+str(rep[1])+"\t\t"+str(rep[2])+"\t\t"+str(rep[3]))
            print

        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'M'):
            print("\n" * 3)
            def_main() # Navigate back to menu
            break
        elif (input_1 == 'E'):
            print("*" * 32 + "THANK YOU "+str(log[1])+ "*" * 31 + "\n") # Exit and break up the loop
            break
        else:
            print("\n" * 3 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_payment(list_price_fun):
    for b in range(0,10):

        print("*" * 32 + "PAYMENTs" + "*" * 33) # Header & Styling
        total_price = 0
        i = 0
        while i < len(list_item_order):
            if (i >= 0) and (i < 40) and (int(list_item_order[i])!= 0):
                print(str(i+1)+"\t"+str(list_foods[i])+"\t *   "+str(list_item_order[i])+"\t=  "+str(list_price_fun[i] * list_item_order[i]))
                total_price += list_price_fun[i] * list_item_order[i] # Calculating the total price for food
            
            i += 1
        print(" "*15+"Total Amount:"+str(total_price))

        print("\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
        input_1 = str(input(str(log[1])+" Select Your Operation: ")).upper()
        if (input_1 == 'P') and (int(total_price) != 0):
            a=datetime.datetime.now()
            bill_id=a.strftime("%d%m%y%H%M%S%f")
            date_current=a.strftime("%d-%m-%y %H:%M")
            conn.execute('insert into order_hist values("'+str(bill_id)+'","'+str(total_price)+'","'+str(date_current)+'","'+str(log[2])+'")')
            conn.commit()
            for a in range(0,99):
                if list_item_order[a]!=0:
                    item_tem_name=list_foods[a]
                    item_tem_quan=list_item_order[a]
                    conn.execute('insert into item_puch values("'+str(bill_id)+'","'+str(item_tem_name)+'","'+str(item_tem_quan)+'")')
                    conn.commit()
            print("\n" * 3)
            print(str(log[1])+" you have Successfully Paid!")

            # file_report = open('files'+navigator_symbol+'report.fsd', 'a') # Save it into a file
            # file_report.write(report_new)
            # file_report.close()
            def_default() #Reset the program for the name order
        elif (input_1 == 'M'):
            print("\n" * 10)
            def_main() #Navigate back to the main menu
            break
        elif (input_1 == 'R'):
            print("\n" * 10)
            def_report() # Navigate to the reports
            break
        elif ('E' in input_1) or ('e' in input_1):
            print("*" * 32 + "THANK YOU " +str(log[1])+ "*" * 31 + "\n")
            break
        else:
            print("\n" * 5 + "ERROR: Invalid Input (" + str(input_1) + "). Try again! or you have nothing to pay")
        
def_main() # Execute Main menu Loop
