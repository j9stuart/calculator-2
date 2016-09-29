def add(*nums):
	"""Returns the sum of the inputs"""
	result = 0

	for n in nums:
		result += n

	return result

def subtract(*nums):
    """Returns the result of subtracting the second number from the first"""
    
    result = nums[0]
    
    for n in nums[1:]:
    	result -= n

    return result

def multiply(*nums):
	"""Returns the product of the inputs"""

	result = nums[0]

	for n in nums:
		result *= n

	return result

def divide(*nums):
	"""Divides the first input by the second, returning a floating point number"""
	
	result = float(nums[0])

	for n in nums[1:]:
		result /= n

	return result

def square(num1):
	"""Returns the square of the input"""
	return num1 ** 2

def cube(num1):
	"""Returns the cube of the input"""
	return num1 ** 3

def power(num1, num2):
	"""Returns the result of raising the first input to the power of the second input"""
	return num1 ** num2

def mod(num1, num2):
	"""Returns the remainder when the first input is divided by the second input"""
	return num1 % num2
