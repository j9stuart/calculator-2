"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
	
	calculation = raw_input(">")
	token = calculation.split(" ")
	print token

	if token[0] == "q": 
		break
	else:

		if token[0] == "+":
			
			nums=[]
			for item in token[1:]: 
				nums.append(int(item))
		
			print add(*nums)

		elif token[0] == "-":
			
			nums = []
			for item in token[1:]:
				nums.append(int(item))

			print subtract(*nums)

		elif token[0] == "*":
			print multiply(num1, num2)

		elif token[0] == "/":
			num1 = int(token[1])
			num2 = int(token[2])
			print divide(num1, num2)

		elif token[0] == "square":
			num1 = int(token[1])
			print square(num1)

		elif token[0] == "cube":
			num1 = int(token[1])
			print cube(num1)

		elif token[0] == "pow":
			num1 = int(token[1])
			num2 = int(token[2])
			print power(num1, num2)

		elif token[0] == "mod":
			num1 = int(token[1])
			num2 = int(token[2])
			print mod(num1, num2)

		else: 
			print "Your input is not a valid operator!"

