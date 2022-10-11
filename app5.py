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
		""" read contents of text file entered """
		filename = input('Type the filename you want to open: ')
		file_to_read = f'{filename}.txt'

		with open(file_to_read, 'r') as file_object:
			data = file_object.read()
			print(data)

	def append_to_file(self):
		""" write data to text file """
		question = input('Type the filename you want to edit: ')
		file_to_read = f'{question}.txt'
		text = input('Enter the text you want to write: ')

		with open(file_to_read, 'a') as file_object:
			file_object.write(text)
			print(f'You entered: {text}')


new_file = TextFile()
# create while loop which asks the citizen what they want to do.
while True:

	question = input('To write to file press any key to continue. press "q" to quit')

	if question == 'q':
		print('\nGoodbye')
		break

	elif question != 'q':

		new_file.create_file()
		new_file.append_to_file()
		new_file.read_file()