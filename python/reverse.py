import input

def reverse_string(in_str):
	return in_str[::-1]

def main():
	input_string = input.get_input()
	reversed_string = reverse_string(input_string)
	print reversed_string

if __name__ == '__main__':
	main()