from nltk.corpus import wordnet as wn
file = open('RG.csv')
dict_score = [[0]*2]*100
i = 0
for line in file:
	dict_score[i] = line.split(',')
	i = i + 1
for k in range(i):
	single_word = dict_score[k][0].split('-')
	noun_synsets1 = wn.synsets(single_word[0],pos=wn.NOUN)
        noun_synsets2 = wn.synsets(single_word[1],pos=wn.NOUN)
        #the first word
	print single_word[0],
	#print 'synset is',noun_synsets1
        for s1 in noun_synsets1:
                for lemma1 in s1.lemmas():
			print str(lemma1.name()),
	print ' '
	#the second word
	print single_word[1],
	for s2 in noun_synsets2:
		for lemma2 in s2.lemmas():
			print str(lemma2.name()),
	print ' '
