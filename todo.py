class ToDo:
	"""A ToDo list"""

	def __init__(self, todo=''):
		self.todo = todo
		self.todo_list = {}

		self.number = 0

	def add_todo(self, new_item):

		self.number += 1
		self.todo_list[self.number] = new_item

		return self.todo_list

	def delete_todo(self, number):

		index = int(number)

		try:
			self.todo_list.pop(number)
			self.number -= 1
		except KeyError:
			print('The number you entered does not exist check the ref number!')
		else:
			return self.todo_list
	
	def view_todo_list(self):

		print(f'The current todo list:')
		for key, value in self.todo_list.items():
			print(f'\t{key} - {value}')

todo = ToDo()

print(todo.number)

todo.add_todo('Learn how to program')
todo.add_todo('Learn how to swim')
todo.add_todo('Learn how to ride bike')
print(todo.todo_list)
print(todo.view_todo_list())
# todo.delete_todo(1)
# todo.delete_todo(2)
# todo.delete_todo(3)
# todo.delete_todo(3)
# todo.delete_todo(3)
# print(todo.todo_list)
# print(todo.todo_list)
#print(todo.number)
