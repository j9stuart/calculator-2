"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
	
	calculation = raw_input(">").rstrip(" ")
	token = calculation.split(" ")
	print token

	if token[0] == "q": 
		break
	else:
		nums = []
		for item in token[1:]:
			nums.append(int(item))

		if token[0] == "+":
			print add(*nums)

		elif token[0] == "-":
			print subtract(*nums)

		elif token[0] == "*":
			print multiply(*nums)

		elif token[0] == "/":
			print divide(*nums)

		elif token[0] == "square":
			print square(nums[0])

		elif token[0] == "cube":
			print cube(nums[0])

		elif token[0] == "pow":
			print power(nums[0], nums[1])

		elif token[0] == "mod":
			print mod(nums[0], nums[1])

		else: 
			print "Your input is not a valid operator!"

