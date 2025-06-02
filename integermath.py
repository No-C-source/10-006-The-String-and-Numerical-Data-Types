#Pseudocode
#Ask the user to enter three different integers. 
#Then print out: 
#The sum of all the numbers 
#The first number minus the second number 
#The third number multiplied by the first number 
#The sum of all three numbers divided by the third number


#Python code
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

print(f"You entered: {num1}, {num2}, {num3}")

# Perform calculations

sum_all = num1 + num2 + num3
subtract = num1 - num2
multiply = num3 * num1
division = sum_all / num3  

print("Sum of all numbers:", sum_all)
print("First number minus second number:", subtract)
print("Third number multiplied by first number:", multiply)
print("Sum of all three numbers divided by third number:", division)




