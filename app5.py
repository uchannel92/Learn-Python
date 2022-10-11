class TextFile:
	"""docstring for ClassName"""
	def __init__(self, arg=''):
		self.arg = arg


	def create_file(self):
		""" create the text file """
		filename = input('Save Filename as: ')
		file = f'{filename}.txt'

		with open(file, 'w') as file_object:
			print(f'Filename has been saved: {file}')

	def read_file(self):

		file_to_read = input('Type the filename you want to open: ')
		filename = f'{file_to_read}.txt'

		with open(file_to_read, 'r') as file_object:
			data = file_object.read()

	def append_to_file(self):
		
		file_to_read = input('Type the filename you want to edit: ')
		text = input('Enter the text you want to write: ')

		with open(file_to_read, 'a') as file_object:
			file_object.write(text)
			print(f'You entered: {text}')


chen_test = TextFile()
chen_test.create_file()
chen_test.append_to_file()
chen_test.read_file()

# create while loop which asks the citizen what they want to do.


print('\nGoodbye')