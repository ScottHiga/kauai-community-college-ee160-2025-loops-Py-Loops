 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# HIGA_Loops.py shows how to use loops and loop controls in python.
#
# Created by Scott Higa, 2025-03-10
# Last edit: 2025-03-10
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

var1 = 1                 # Setting var1 to the int value 0

while (var1 <= 10):      # Writing a while loop so that while var1 is less than eleven, the script will run the function below...
    print (var1)         # This will print var1 so long as the while loop conditions are met
    var1 = var1 + 1      # *Tricky step* After the first print function, we assign a new assignment to var1, which is var1 + 1. The script jumps back to the "while" line and var1 is now equal to 2 and since 2 is <= 10, the script will run the print function and print the new assignment of var1.  This will continue until var1 = 10
                         # After the while condition is no longer met, the script will exit the loop
var1 = 10

for var2 in range(1,11):    # *For/In Loop: For the integers in the range of [1,11), we assign var2 to these integer values and...
    print (var2)            # Print var 2

var3 = 0                    # Setting var3 to 0

while (var3 < 50):          # While loop: While var3 is less than 50, the rest of the loop will run
    var3 = var3 + 1         # Assigning var3 a new value, the previous value (1st loop = 0) and adding 1 to it.  Basically listing all integers from 1-50
    if var3 % 3 == 0:       # If the modulus of var3 divided by 3 is equal to zero, then the next scope will run
        print (var3)        # printing all integers under 50 divisible by 3 (if an integer is divisible by 3, then it will also be divisible by 6 or 9)

# How many times can we divide 12 until the change in iterations becomes less than 0.0001
# (1) 12/2 = 6
# (2) 6/2 = 3
# (3) 3/2 = 1.5
# (4) 1.5/2 = 0.75
# (5) 0.75/2 = 0.375
# (6) 0.375/2 = 0.1875
# (7) 0.1875/2 = 0.09375
# (8) 0.09375/2 = 0.046875
# (9) 0.046875/2 = 0.0234375
# (10) 0.0234375/2 = 0.01171875
# (11) 0.01171875/2 = 0.005859375
# (12) 0.005859375/2 = 0.0029296875
# (13) 0.0029296875/2 = 0.00146484375
# (14) 0.00146484375/2 = 0.000732421875
# (15) 0.000732421875/2 = 0.0003662109375
# (16) 0.0003662109375/2 = 0.00018310546875
# (17) 0.00018310546875/2 = 0.000091552734375

# These are all global variables. Global variables can be used anywhere in the file. We assign these variables outside the scope of the loop so that we can manipulate them inside the loop while also maintaining their integrity throughout the file.
starting_value = 12                            # Setting a global variable for the starting point of the loop
number_of_iterations = 0                       # Setting a global variable for the number of times we can divide 12 by 2 such that the modulus becomes less than 0.0001
amount_of_change = 3                           # Setting a global variable for the modulus #0.0001000000000000001

#scope
while amount_of_change > 0.0001:                        # Loop to track the value of amount of change so the loop will end once this amount converges to 0.0001
    next_value = starting_value                         # Creating a new variable (next_value) and setting it to the global variable (starting_value). # 1st loop: next_value = 12
    starting_value = starting_value/2                   # Assigning variable (starting_variable) to itself and dividing by 2. # 1st loop: starting_value = 6
    amount_of_change = (next_value-starting_value)      # Creating a new variable (amount_of_change) and assigning it to the difference of (next_value) and the local variable, (starting_variable) that was redefined on line 53.  This line will continue to change until it breaks the while loop because the local variables, next_value and starting_value will be redefined during each loop.  1st loop: amount_of_change = 12-6 = 6 # Since 6 > 0.0001, the loop will jump back to the beggining of the local scope (1st indent) and repeat
    number_of_iterations = number_of_iterations + 1     # Tracking the number of times the loop will run.  Once the while loop breaks, the variable (number_of_iterations) will 'save' the value from the last time the loop ran.  1st loop: number_of_iterations = 1
    print (number_of_iterations)                        # Printing the number of times the loop reached this point (starting from zero)


print ("")
print("Done!")