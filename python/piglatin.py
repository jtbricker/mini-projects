import input

def pig_latin_word(word):
	out = ""
	if word[0].lower() in ['a','e','i','o','u']:
		out = word+"way"
	else:
		out = word[1:]+word[0]+"ay"
	return out

def pig_latin_phrase(phrase):
	outphrase = []
	phrase = phrase.split(' ')
	for i in range(len(phrase)):
		outphrase.append(pig_latin_word(phrase[i]))
	return ' '.join(outphrase)

def main():
	input_string = input.get_input()
	pl_string = pig_latin_phrase(input_string)
	print pl_string

if __name__ == '__main__':
	main()