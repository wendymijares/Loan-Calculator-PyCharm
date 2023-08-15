## How much money do you need in dollars? ##
money_owed = float(input("How much money do you owe in dollars?\n")) #$50,000

## Anual % rate##
anual_rate = float(input("What is the anual percentage  rate?\n")) #3%

## Montly Payement
montly_rate = float(input("What will you monthly payment be, in dollars.\n")) #$1000

## Month do you want to see the result for
month_result = int(input("How many month do you want to see the result for ?.\n")) #24

## Divide annual rate by 100 to make %, then divide by 12 to make it monthly
month = anual_rate/100/ 12


for i in range(month_result):  #the loop is to be able to ask for any month
        ## Add interests
        interest_paid = money_owed*month
        money_owed = money_owed + interest_paid

        if (money_owed - montly_rate < 0): ## If the payment is made zero
           print("The last payment is", money_owed)
           print("Yoy pay of the Loan in", i + 1,"months")
           break   ## To break the loop

        money_owed = money_owed - montly_rate  ## Make the payement
        print("Paid", montly_rate, "of which", interest_paid, "was interest", end=' ')   #$ Print the result after this month
        print("Now I owe", money_owed)

