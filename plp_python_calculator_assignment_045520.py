# 🔢 Basic Calculator Assignment - PLP
# By Millicent Nabututu Makokha

# Step 1: Get input from user
print("🔢 Welcome to the Basic Python Calculator")

num1 = input( " Enter the first number: ")
num2 = input( " Enter the second number: ")
operation = input( "choose operation (+, -, *, / ) : ")

# Step 2 : Convert string input to float
num1 = float( num1 )
num2 = float( num2 )

# Step 3 : Perform the choosen operation
if operation == " + " :
	result = num1 + num2
elif operation == " - " :
	result = num1 - num2
elif operation == " * " :
	result = num1 * num2
elif operation == " / " :
	if num2 != 0 :
		result = num1 / num2
	else :
		result = " Error Division by zero "
				
# Step 4 : Data type exploration
print( " Data type check : ")
print( "Type on num1 : " , type( num1))
print( " Type on num2 : " , type( num2))

# Step 5 : Display result
print( " part 5 Result : { num1 } { operation } { num2 } { data type check }  = { result } " )



	     







	
	
	



	
		