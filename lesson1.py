# Hello This is lesson 1 of Github 

# Commit these changes and merge it with main.

import random 

def print_random_num():

	numbers = list(range(1,11))

	random_number = random.choice(numbers)

	return random_number


rand = print_random_num()
print(rand)

rand_two = print_random_num()
print(rand_two)