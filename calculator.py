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

			if question == 'q':
				break
			
			elif question == 'a':
				current_value += self.add_nums()
			
			elif question == 'e':
				print(current_value)

	def add_nums(self):

		fir_num = int(input('1st num: ' ))
		sec_num = int(input('2nd num: ' ))
		self.user_input_one = fir_num
		self.user_input_two = sec_num

		return self.user_input_one + self.user_input_two


maths = Calculator()
print('Welcome to Chens Calculator')
maths.show_current_value()