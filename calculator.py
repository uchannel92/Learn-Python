# Create a calculator app

class Calculator:
	""" Class for the calculator app """

	def __init__(self, user_input_one='', user_input_two=''):
		self.user_input_one = user_input_one
		self.user_input_two = user_input_two

	def show_current_value(self):
		current_value = 0

		while True:

			question = input('q to exit or any key to continue: ')

			# q means quit
			if question == 'q':
				break
			
			# a means add
			elif question == 'a':
				current_value += self.add()
			
			# e means evaluate
			elif question == 'e':
				print(current_value)

			elif question == 'c':
				current_value = 0

			else:
				print('we did not understand your input')
				continue

	def add(self):
		''' Add two values '''

		self.user_input_one = int(input('1st num: ' ))
		self.user_input_two = int(input('1st num: ' ))

		return self.user_input_one + self.user_input_two


	def subtract(self):
		''' Subtract two values '''

		self.user_input_one = int(input('1st num: ' ))
		self.user_input_two = int(input('1st num: ' ))

		return self.user_input_one - self.user_input_two

maths = Calculator()
print('Welcome to Chens Calculator')
#maths.show_current_value()
print(maths.subtract())