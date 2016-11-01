def word(sentence):
	count_dict = {}
	for word in sentence.split():
		if word.isdigit():
			count_dict.setdefault(int(word),0)
			count_dict[int(word)] += 1
		else:
			count_dict.setdefault(word,0)
			count_dict[word] += 1

	print count_dict
word('i am a a a boy')