import random

# get random word from file
def random_word(file):
	f = open(file)
	lines = f.readlines()
	l = []

	for i in range(0, len(lines)):
		line = lines[i]
		word = line[:len(line)-1]
		l.append(word)

	return random.choice(l)
	f.close()

random_adj = random_word('english-adjectives.txt')
random_noun = random_word('english-nouns.txt')

print(random_adj + ' ' + random_noun)
