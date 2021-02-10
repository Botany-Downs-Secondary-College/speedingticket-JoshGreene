warrant_list = ["Bob", "John", "Cassey"]
print("Please insert name of fugitive")
warrant = input("Insert: ")


Bob = "Wanted for faliure to appear in Court"
Bob1 = "Wanted for:\n1 Count of aggrevated assault\n2 Counts of Grand Theft Auto"

if warrant in warrant_list:
    print(warrant,"has a warrant for their arrest. Would you like to see their warrant and record? Yes or no?")
    record = input("Yes or No?: ")
    if record == "Yes":
        for warrant in warrant_list:
            if warrant == "Bob":
                print(Bob1)
            elif warrant == "John":
                print("This works!")
        

elif warrant not in warrant_list:
        print("Please input new offender")
        newoffender = input("Input: ")
        
    