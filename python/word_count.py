import input

def count_words(in_str):
	words = in_str.split(' ')
	word_lengths = []
	for word in words:
		word_lengths.append(len(word))
	avg_len = sum(word_lengths)/len(words)
	max_len = max(word_lengths)
	min_len = min(word_lengths)
	return len(words), avg_len, max_len, min_len

def words_summary(num_words, avg_len, max_len, min_len):
	print "Number of words: %s"%num_words
	print "Average length words: %s"%avg_len
	print "Max length words: %s"%max_len
	print "Min length words: %s"%min_len

def main():
	input_string = input.get_input()
	num_words, avg_len, max_len, min_len = count_words(input_string)
	words_summary(num_words, avg_len, max_len, min_len)

if __name__ == '__main__':
	main()