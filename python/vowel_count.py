import input

def count_vowels(in_str, includeY = False):
	vowels_ref = 'aeiou'
	vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
	if(includeY):
		vowels['y']=0
		vowels_ref += 'y'
	for letter in in_str:
		if letter.lower() in vowels_ref:
			vowels[letter.lower()]+=1
	return vowels


def vowel_summary(vowels):
	total = 0;
	for key in vowels:
		print "%s : %s"%(key, vowels[key])
		total += vowels[key]
	str = "Total Number of Vowels"
	if('y' in vowels):
		str += "(Now including Y!)"
	print("=====================================")
	print("%s: %s")%(str,total)
	print("=====================================")

def main():
	input_string = input.get_input()
	vowels = count_vowels(input_string, True)
	vowel_summary(vowels)

if __name__ == '__main__':
	main()