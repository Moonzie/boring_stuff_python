def collatz(number):

	if number % 2 == 0:
		sequence = number // 2
		return(sequence)
	elif number % 2 == 1:
		sequence = 3 * number + 1
		return(sequence)
	else: 
		print ("errrrrrorrrrr")

def main():
	number_in = input('enter a number: ')
	
	while True:
		number_in = collatz(int(number_in))
		print(number_in)
		if number_in == 1:
			break
main()
