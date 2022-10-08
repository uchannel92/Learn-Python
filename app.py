# string
# integear
# boolean True / False
# lists
# dictionaries
# tuples
# set
# range()
# NaN


# if age < 18:
# 		print('You cannot vote')
# 	elif age >= 18:
# 		print('You can vote')

# while loops - when youre not sure how many times you need to run
# for loops  - when the loop is set to run X amount of times
# list comprehension - usually write code in one line, syntax easier to read


# numbers = list(range(1,6))
# print(numbers)
# squared = [num * 2 for num in numbers]
# print(squared)


# for number in numbers:

# 	square = number * 2
# 	squared.append(square)
# print(squared)

# count = 0
# while count < 11:
# 	print(f'The count is {count}')
# 	count += 1
#

# count = 0
# string = '*'

# while count < 8:
# 	print(string)
# 	string += '*'
# 	count += 1


# def create_user():

# 	user = {}
# 	user['first'] = 'uchenna'
# 	user['city'] = 'london'

# 	user['city'] = 'Madrid'
# 	#user.popitem() # popitem method deletes last item in dictionary
# 	user.clear() # Clear a dictionary with this method
# 	print(user)

# create_user()


class Dog:
	"""docstring for Dog"""

	eyes = 2

	def __init__(self, breed='bulldog', name='toby', dog_years=5):
		self.breed = breed
		self.name = name
		self.dog_years = dog_years

	def wag_tail(self):
		return f'{self.breed} wags tail'

	def dog_bark(self):
		return 'woof!'

new_dog = Dog('beagle', 'patch')
another_dog = Dog('German Shepard', 'Max')

# print(new_dog.breed)
# new_dog.wag_tail()
# print(another_dog.breed)