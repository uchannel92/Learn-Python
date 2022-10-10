class TextFile:
	"""docstring for ClassName"""
	def __init__(self, arg=''):
		self.arg = arg


	def read_text_file(self):
		""" create the text file """

		#hard coding the filename
		filename = 'coldplay.txt'

		with open(filename, 'r') as file_object:
			data = file_object.read()

		print('file has been read')
		return data

	def display_data(self):

		track = self.read_text_file()
		print(track)


new_file = TextFile()

while True:

	prompt = input('Enter any key to continue or press q to quit: ')

	if prompt == 'q':
		break

	else:
		pass

	prompt_two = input('1) add data 2) read file: ')

	if prompt_two == '1':
		new_file.read_text_file()
		continue

	elif prompt_two == '2':
		new_file.display_data()
		break


print('\nGoodbye')