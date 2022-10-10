prompt = """ What city is the capital of England?
a) Coventry
b) Glasgow
c) London
d) Manchester
"""

answers = [
	'Coventry', 'Glasgow', 
	'London', 'Manchester'
]

question_active = True

while question_active:
	
	question = input(f'{prompt}: ')

	if question == 'a':
		print(f'You picked {answers[0]}')

	elif question == 'b':
		print(f'You picked {answers[1]}')

	elif question == 'c':
		print(f'You picked {answers[2]}')
		print('You picked the correct answer!')
		question_active = False

	elif question == 'd':
		print(f'You picked {answers[-1]}')

	else:
		print("That is not an option:\nEnter (a, b, c, d)") 
