from datetime import datetime 

print("M for Mileage tips, P for Problem analyzer, E for Expense calculator")
selection=input("Enter your need: ")
if(selection=="M"):
    print("1. Drive Smoothly.")
    print("2. Use the right gear.")
    print("3. Maintain correct Tyre Pressure.")
    print("4. Reduce extra weight.")
    print("5. Regular servicing.")

elif(selection=="P"):
    problem=input("Enter your problem:")
    if(problem=="Temperature gauge high" or problem=="steam from bonnet"):
        print("Issue = Engine Overheating")
        print("Causes = Low coolant, radiator leak, faulty fan")
        print("Estimate cost = ₹500 – ₹8,000")
    elif(problem=="Car won’t start" or problem=="dim lights" or problem=="clicking sound"):
        print("Issue = Battery Failure")
        print("Causes = Old battery, loose terminals, alternator issue")
        print("Estimate cost = ₹3,000 – ₹8,000")
    elif(problem=="Screeching noise" or problem=="vibration" or problem=="weak braking"):
        print("Issue = ⁠Brake Problems")
        print("Causes = Worn brake pads, low brake oil")
        print("Estimate cost = ₹1,500 – ₹6,000")
    elif(problem=="Frequent refueling" or problem=="poor performance"):
        print("Issue = ⁠Low Mileage")
        print("Causes = Dirty air filter, aggressive driving, low tyre pressure")
        print("Estimate cost = ₹200 – ₹3,000")
    elif(problem=="Jerking" or problem=="vibration" or problem=="power loss"):
        print("Issue = ⁠Engine Misfiring")
        print("Causes = Bad spark plug, injector issue, faulty ignition coil")
        print("Estimate cost = ₹1,000 – ₹10,000")
    elif(problem=="Uneven wear" or problem=="frequent punctures"):
         print("Issue = Tyre Issues")
         print("Causes = Wrong alignment, low tyre pressure")
         print("Estimate cost = ₹300 – ₹6,000 per tyre")
    elif(problem=="Hard gear shift" or problem=="slipping clutch"):
         print("Issue = ⁠Clutch Problems (Manual)")
         print("Causes = Worn clutch plate")
         print("Estimate cost = ₹4,000 – ₹12,000")
    elif(problem=="Bumpy ride" or problem=="knocking noise"):
         print("Issue = Suspension Problems")
         print("Causes = Worn shock absorbers, broken bush")
         print("Estimate cost = ₹3,000 – ₹15,000")
    elif(problem=="Engine cranks but doesn’t start"):
         print("Issue = Starting Trouble")
         print("Causes = Battery, starter motor, fuel supply issue")
         print("Estimate cost = ₹1,000 – ₹9,000")
    elif(problem=="Poor pickup" or problem=="engine stalling"):
         print("Issue = ⁠Fuel System Issues")
         print("Causes = Clogged fuel filter, dirty injectors")
         print("Estimate cost = ₹1,500 – ₹7,000")

elif(selection=="E"):
    file_name="expensehistory.txt"

    print("Expense manager:")
    print("1.Add new expense")
    print("2.Edit entry")
    print("3.View expense history")
    print("4.Delete an entry")
    print("5.Clear history")

    user_choice=input("Select an option(1-5):")

# 1 adding expense
    if (user_choice=="1"):
        file_open=open(file_name,"a")

        total=0
        highest=0
        highest_name=""

        count=int(input("Number of expenses you want to add:"))

        for i in range(count):
            name=input("Expense name:")
            amount=int(input("Enter amount:₹"))
            total=total+amount
            if (amount>highest):
                highest=amount
                highest_name=name
            today=datetime.now().strftime("%Y-%m-%d")
            line= today+"|"+ name + "|₹" + str(amount)
            file_open.write(f"{today}|{name}|₹{amount}\n")
            print(f"{name}, added=₹{amount}")
        

        print("Your Expense Summary:")
        print(f"Total number of expense:{count}")
        print(f"Total expenditure= ₹{total}")
        print(f"Highest money spent on {highest_name} is ₹{highest}")
        print(f"Average expense= ₹{total/count}")

# 2 editing entry
    if(user_choice=="2"):
        f=open(file_name,"r")
        lines=f.readlines()
        f.close()
        
        if not lines:
            print("Your history is empty.")
        else:
            print("Current entries:")
            for i, line in enumerate(lines):
                    print(i+1, ":", line.strip())

            number = int(input("Enter entry number to edit: "))
            index = number-1

            if (index < 0 or index >= len(lines)):
                    print("Invalid entry number.")
            else:
                    new_name = input("Enter new expense name : ")
                    new_amount = input("Enter new amount : ₹ ")

                    today = datetime.now().strftime("%Y-%m-%d")
                    lines[index] = today + " | " + new_name + " | ₹ " + str(new_amount) 

                    f = open(file_name, "w")
                    f.writelines(lines)
                    f.close()
                    print("Entry updated.")

# 3 expense history
    if(user_choice=="3"):
         print("Your expense history:")
         f=open(file_name,"r")
         data=f.read()
         f.close()

         if (data.strip()==""):
            print("History is empty")
         else:
            print(data)

# 4 delete entry
    if(user_choice=="4"):
     f=open(file_name,"r")
     lines=f.readlines()
     f.close()

     if not lines:
        print("History is empty")
     else:
         print("Your current entries: ")
         for i, line in enumerate(lines):
           print(i+1,":",line.strip())

         number=int(input("Enter number to delete:"))
         index=number-1

         if(index<0 or index>=len(lines)):
            print("Invalid entry number")
         else:
            delete=lines[index].strip()
            del lines[index]

            f=open(file_name,"w")
            f.writelines(lines)
            f.close()
            print(f"Deleted:,{delete}")

# 5 clear history
    if (user_choice == "5"):
        confirm = input("Sure you want to clear history? (yes/no): ")
        if confirm == "yes":
            open(file_name, "w").close()   
            print("Expense history cleared.")
        else:
            print("Clear cancelled")

else:
    print("Invalid option.")