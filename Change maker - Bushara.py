from decimal import *
myothercontext = Context(rounding=ROUND_HALF_UP)
setcontext(myothercontext)

change_change_choice = 'yes'
while change_change_choice == 'yes':    
    choice_change_type = input("Do you want to enter your change in dollars (i.e. 12.50) or in cents (i.e. 1250)?").lower()

    while choice_change_type not in ['dollars', 'cents']:
        print("You entered:", choice_change_type, "that is invalid response, please try again.")
        choice_change_type = input("Do you want to enter your change in dollars (i.e. 12.50) or in cents (i.e. 1250)?").lower()
    
    change_change_choice = input("Do you want to change your entry {choice_change_type} ? (yes/no): ").lower()
        
    while change_change_choice not in ['yes', 'no']:
        print(f"You entered: {change_change_choice}, that is an invalid response, please try again.")
        change_change_choice = input("Do you want to change your selection?").lower()

print("Thank you, your form of change entry is:", choice_change_type)


change_money_value = 'yes'
while change_money_value == 'yes':
    while True:   
        if choice_change_type == "dollars":
            try:
                money_value = input("How much money do you need change for? (Enter in dollars I.E. 12.50) Note: Your number will be rounded to two decimal places to a multiple of 0.05, you must enter only one '.'")
                money_value = Decimal(money_value).quantize(Decimal('0.05'), rounding=ROUND_HALF_UP)
                if money_value < 0:
                    raise ValueError
            except Exception as e:
                print(f"Invalid input: {e}")
            else:
                money_value_display = str(money_value)
                money_math = int(money_value * 100)
                break
        else:
            try:
                money_value = input("How much money do you need change for? (Enter in cents I.E. 1250) Note: Your number will be rounded to two decimal places to a multiple of 1, you must enter only digits.")
                money_value = Decimal(money_value).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
                if money_value < 0:
                    raise ValueError
            except Exception as e:
                print(f"Invalid input: {e}")
            else:
                money_value_display = str(money_value)
                money_math = int(money_value)
                break

    print(f"Thank you, your amount of change needed is: {money_value_display}")

    change_money_value = input("Do you want to change your entry? (yes/no): ").lower()

    while change_money_value not in ["yes", "no"]:
        print(f"You entered: {change_money_value}, that is an invalid response, please try again.")
        change_money_value = input("Do you want to change your selection? (yes/no): ").lower()


print("Your change amount is " + money_value_display)



change_calculation_choice = 'yes'
while change_calculation_choice == 'yes':
    choice_calculation_type = input('Do you want to calculate change using dollars, coins or both?').lower()

    while choice_calculation_type not in ['both', 'dollars', 'coins']:
        print("You entered:", choice_calculation_type, "that is invalid response, please try again.")
        choice_calculation_type = input('Do you want to calculate change using dollars, coins or both?').lower()

        print("Thank you, your selection is:", choice_calculation_type)


    change_calculation_choice = input("Do you want to change your entry {choice_calculation_type} ? (yes/no): ").lower()

    while change_calculation_choice not in ['yes', 'no']:
        print("You entered:", change_calculation_choice, "that is an invalid response, please try again.")
        change_calculation_choice = input("Do you want to change your selection?").lower()
    


if choice_calculation_type == 'both':
    print("Thank you, your form of change calculation is: both dollars and coins")

else:
    print("Thank you, your form of change calculation is:", choice_calculation_type)

     


#all combinations of coins containg the half dollar or not, and containing dollars or not are canonical and thus work in the greedy method
#algorithmic test used: https://www.sciencedirect.com/science/article/abs/pii/S0167637704000823 ,golfier was not tested

bills_cents_value_list = [10000,5000,2000,1000,500]
coins_cents_value_list = [200, 100, 25, 10, 5]

def calculate_change(money_math, value_list):
    needed_list = []
    money_calculated = 0
    for value in value_list:
        needed, money_math = divmod(money_math, value)
        needed_list.append(needed)
        money_calculated += needed * value
    return needed_list

print('You will need:')
bills_change_needed = '{} one hundred dollar bills, {} fifty dollar bills, {} twenty dollar bills, {} ten dollar bills, {} five dollar bills'
coins_change_needed = '{} toonies, {} loonies, {} quarters, {} dimes, {} nickels'

if choice_calculation_type == 'dollars':
    bills_needed = calculate_change(money_math, bills_cents_value_list)
    bills_result = bills_change_needed.format(*bills_needed)
    print(bills_result)
elif choice_calculation_type == 'coins':
    coins_needed = calculate_change(money_math, coins_cents_value_list)
    coins_result = coins_change_needed.format(*coins_needed)
    print(coins_result)
else:
    bills_needed, money_calculated = calculate_change(money_math, bills_cents_value_list)
    bills_result = bills_change_needed.format(*bills_needed)
    
    coins_needed, money_calculated = calculate_change(money_math, coins_cents_value_list)
    coins_result = coins_change_needed.format(*coins_needed)
    
    print(bills_result + ', ' + coins_result)


money_calculated = str(money_calculated)
if choice_change_type == 'dollars':      
    money_calculated = money_calculated[:len(money_calculated)-2] + '.' + money_calculated[-2:]

if money_calculated != money_value_display:
    print(f'Sorry! The best we can do with your selections equals: {money_calculated} {choice_change_type} instead of: {money_value_display} {choice_change_type}')
else:
    print(f'to create {money_value_display} {choice_change_type}')


