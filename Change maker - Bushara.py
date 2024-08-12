change_change_choice = 'yes'
while change_change_choice == 'yes':    
    choice_change_type = input("Do you want to enter your change in dollars (i.e. 12.50) or in cents (i.e. 1250)?")
    choice_change_type = choice_change_type.lower()

    while choice_change_type != "dollars" and choice_change_type != "cents":
        print("You entered:", choice_change_type, "that is invalid response, please try again.")
        choice_change_type = input("Do you want to enter your change in dollars (i.e. 12.50) or in cents (i.e. 1250)?")
        choice_change_type = choice_change_type.lower()

    print("Thank you, your selection is:", choice_change_type)

    print("How to change or keep your selection:")
    print("If you would like to keep your current selection, which is:", choice_change_type, " enter \"no\"")
    print("If you would like to change your selection enter \"yes\"")
    
    change_change_choice = input("Do you want to change your selection?")
    change_change_choice = change_change_choice.lower()

    while change_change_choice != "yes" and change_change_choice != "no":
        print("You entered:", change_change_choice, "that is an invalid response, please try again.")
        change_change_choice = input("Do you want to change your selection?")
        change_change_choice = change_change_choice.lower()
        
    if change_change_choice == 'yes':
        continue
    else:
        break

print("Thank you, your form of change entry is:", choice_change_type)


change_money_value = 'yes'
while change_money_value == 'yes': 
    while True:
        if choice_change_type == "dollars":
            try:
                money_value = input("How much money do you need change for? (Enter in dollars I.E. 12.50) Note:Your number will be rounded to two decimal places to a multiple of 0.05, you must enter only one '.'")
                if float(money_value) < 0:
                    raise ValueError
                
                    
                cuts = money_value.count('.')
                money_value_list = money_value.split('.')
                
                
                if cuts != 1:
                    raise ValueError
                if len(money_value_list[0]) == 0:
                    raise ValueError
                if len(money_value_list[1]) != 2:
                    raise ValueError                
        
            except ValueError:
                print("You must enter a float number, it must have a \'.\'")
            else:
                money_value_display = str(money_value_list[0]) + '.' + str(money_value_list[1])
                money_math = int(str(money_value_list[0]) + str(money_value_list[1]))
                break
        else:
            try:
                money_value = input("How much money do you need change for? (Enter in cents I.E. 1250) Note:Your number will be rounded to two 0 places to a multiple of 5, you must zero '.'")
                if int(money_value) < 0:
                    raise ValueError
            except ValueError:
                print("You must enter a float number, it must have a \'.\'")
            else:
                money_value_display = money_value
                money_math = int(money_value)
                break

    print("Thank you, your amount of change needed is:", money_value_display)
    
    print("How to change or keep your selection:")
    print("If you would like to keep the amount of change needed, which is:", choice_change_type, " enter \"no\"")
    print("If you would like to change the amount of change needed enter \"yes\"")

    change_money_value = input("Do you want to change your entry?")
    change_money_value = change_money_value.lower()

    while change_money_value != "yes" and change_money_value != "no":
        print("You entered:", change_money_value, "that is an invalid response, please try again.")
        change_money_value = input("Do you want to change your selection?")
        change_money_value = change_money_value.lower()
            
    if change_money_value == 'yes':
        continue
    else:
        break


print("Your change amount is " + money_value_display)

#Round the change value given, in the integer/only cents form
rounded = round(money_math / 5) * 5


change_calculation_choice = 'yes'
while change_calculation_choice == 'yes':
    choice_calculation_type = input('Do you want to calculate change using dollars, coins or both?')
    choice_calculation_type = choice_calculation_type.lower()

    while choice_calculation_type != "both" and choice_calculation_type != "dollars" and choice_calculation_type != "coins":
        print("You entered:", choice_calculation_type, "that is invalid response, please try again.")
        choice_calculation_type = input('Do you want to calculate change using dollars, coins or both?')
        choice_calculation_type = choice_calculation_type.lower()

        print("Thank you, your selection is:", choice_calculation_type)

        

    print("How to change or keep your selection:")
    print("If you would like to keep your current selection, which is:", choice_calculation_type, " enter \"no\"")
    print("If you would like to change your selection enter \"yes\"")

    
    change_calculation_choice = input("Do you want to change your selection?")
    change_calculation_choice = change_calculation_choice.lower()

    while change_calculation_choice != "yes" and change_calculation_choice != "no":
        print("You entered:", change_calculation_choice, "that is an invalid response, please try again.")
        change_calculation_choice = input("Do you want to change your selection?")
        change_calculation_choice = change_calculation_choice.lower()
        
    if change_calculation_choice == 'yes':
        continue
    else:
        break



if choice_calculation_type == 'both':
    print("Thank you, your form of change calculation is: both dollars and coins")

else:
    print("Thank you, your form of change calculation is:", choice_calculation_type)

     


#all combinations of coins containg the half dollar or not, and containing dollars or not are canonical and thus work in the greedy method
#algorithmic test used: https://www.sciencedirect.com/science/article/abs/pii/S0167637704000823 ,golfier was not tested

bills_cents_value_list = [10000,5000,2000,1000,500]
coins_cents_value_list = [200, 100, 25, 10, 5]

bills_needed = []
coins_needed = []

money_calculated = 0

print('You will need:')
bills_change_needed = '{} one hundred dollar bills,  {} fifty dollar bills,  {} twenty dollar bills,  {} ten dollar bills,  {} five dollar bills'
coins_change_needed = '{} toonies, {} loonies, {} quarters, {} dimes, {} nickels'

if choice_calculation_type == 'dollars':
    for i in range(5):
        needed, money_math = divmod(money_math, bills_cents_value_list[i])
        bills_needed.append(needed)
        money_calculated += bills_needed[i] * bills_cents_value_list[i]
    bills_result = bills_change_needed.format(bills_needed[0],bills_needed[1],bills_needed[2],bills_needed[3],bills_needed[4])
    print(bills_result)
    

        
elif choice_calculation_type == 'coins':
    for i in range(5):
        needed, money_math = divmod(money_math, coins_cents_value_list[i])
        coins_needed.append(needed)
        money_calculated += coins_needed[i] * coins_cents_value_list[i]
    
    coins_result = coins_change_needed.format(coins_needed[0],coins_needed[1], coins_needed[2],coins_needed[3], coins_needed[4])
    print(coins_result)

    
else:
    for i in range(5):
        needed, money_math = divmod(money_math, bills_cents_value_list[i])
        bills_needed.append(needed)
        money_calculated += bills_needed[i] * bills_cents_value_list[i]
    bills_result = bills_change_needed.format(bills_needed[0],bills_needed[1],bills_needed[2],bills_needed[3],bills_needed[4])
    
    
    for i in range(5):
        neededc, money_math = divmod(money_math, coins_cents_value_list[i])
        coins_needed.append(neededc)
        money_calculated += coins_needed[i] * coins_cents_value_list[i]
  
    coins_result = coins_change_needed.format(coins_needed[0],coins_needed[1], coins_needed[2],coins_needed[3], coins_needed[4])
    
    print(bills_result + ', ' + coins_result)
    
        
        
        

money_calculated = str(money_calculated)
if choice_change_type == 'dollars':      
    money_calculated = money_calculated[:len(money_calculated)-2] + '.' + money_calculated[2:]
            
if money_calculated != money_value:
    print('Sorry! The best we can do with your selections equals: ' + money_calculated + ' ' + choice_change_type + ' instead of: ' + money_value_display + ' ' + choice_change_type)
        
else:
    print('to create ' + money_value_display + ' ' + choice_change_type)
