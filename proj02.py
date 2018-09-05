########################################################
#  Computer Project #2
#   Say welcome to change making program
#   Update user about stock
#  Prompt purchasing price
#   Prompt dollars paid
#   Display Change
#   Prompt for purchasing price again
##########################################################


print("Welcome to change-making program.")
nq_int= 10
nd_int= 10
nn_int = 10
np_int = 10
print("Stock:", nq_int, "quarters,", nd_int, "dimes,", nn_int, "nickels, and", np_int, "pennies")
in_str= input("Enter the purchase price (xx.xx) or 'q' to quit: ")
in_float = float(in_str)
while in_float < 0 :
    print("Error: purchase price must be non-negative.")
    print("Stock:",nq_int, "quarters,", nd_int,"dimes,", nn_int, "nickels, and", np_int,"pennies")
    in_str= input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    in_float = float(in_str)
while in_str != 'q' :
    in_float = float(in_str)
    cents_float= in_float * 100
    cents_int= int(cents_float)
    dl_stng= input("Input dollars paid (int): ")
    dl_float= (float(dl_stng))     
    dl_float= ((dl_float)) * 100
    change_int= dl_float- cents_float
    dimes = 0
    qrts= 0
    nickels= 0
    pennies = 0
    if change_int == 0:
        print("No change.")
    elif change_int < 0:
        print("Error: insufficient payment.")
        dl_stng= input("Input dollars paid (int): ")
        dl_float= (float(dl_stng))     
        dl_float= ((dl_float)) * 100
        change_int= dl_float- cents_float
        if change_int > 0:
            print("Collect change below: ")
    elif change_int > ((nq_int * 25) + (nd_int * 10) + (nn_int * 5) + (np_int* 1)):
        print("Error: ran out of coins.")
        nq_int = 0
        nd_int = 0
        nn_int = 0
        np_int = 0
    elif change_int > 0:
        print("Collect change below: ")
    
    while change_int >= 25 and nq_int > 0:
        nq_int -= 1
        change_int -= 25
        if (10- nq_int) > 0:
           qrts = 10 - nq_int 
    while change_int >= 10 and nd_int > 0 :
        nd_int -= 1
        change_int -= 10
        if(10 - nd_int) > 0 :
            dimes = 10 - nd_int
    while change_int >= 5 and nn_int >0 :
        nn_int -= 1
        change_int -= 5
        if (10 - nn_int) > 0:
            nickels = 10 - nn_int 
    while change_int >= 1 and np_int > 0:
        np_int -= 1
        change_int-= 1
        if (10 - np_int) > 0:
            pennies = 10 - np_int

    if qrts > 0:
        print("Quarters:", qrts)
    if dimes > 0:
        print("Dimes:", dimes)
    if nickels > 0:
        print("Nickels:", nickels)
    if pennies > 0:
        print("Pennies:", pennies)

    if nq_int != 0 or nd_int != 0 or nn_int != 0 or np_int != 0:   
        print("Stock:",nq_int, "quarters,", nd_int,"dimes,", nn_int, "nickels, and", np_int,"pennies",)
        in_str= input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    if change_int > ((nq_int * 25) + (nd_int * 10) + (nn_int * 5) + (np_int* 1)):
        break

