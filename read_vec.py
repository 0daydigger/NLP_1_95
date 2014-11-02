import math
#the synset part
# NOTICE! In this part, the array dict_synsets[s_key] is always has more 
# 1 item in it. So when normalizing the vector, plz make sure use len(xxx) - 1
f_synsets = open('synsets','r')
dict_synsets = {'LU YuXun': 'A great guy'}
word_list = []
for s_line in f_synsets:
	s_str = s_line.split(' ')
	s_key = s_str[0]
	word_list.append(s_key)
#	print 'origin:',s_line
	del s_str[0] #NOTICE! IF THE POOLING NEED THE WORD ITSELF,THIS SHOULD BE DELETED
	#print '1:',s_str[ len(s_str) - 1]
	#print '2:',s_str[ len(s_str) - 2]
	del s_str[ len(s_str) - 1 ] #the '\n'
	dict_synsets[s_key] = s_str
#	print 'The key:',s_key
#	print 'The value:',dict_synsets[s_key]
#	print 'The length:',len(dict_synsets[s_key])
#	raw_input('Press any key to continue')
f_synsets.close()

#print word_list
print 'Word List Construction Compelete'


#the vector part
F_NAME1 = 'vectors_origin_'
F_NAME2 = ['100','200','300','400','500','600','700','800','900','1000']
F_NAME3 = ['3','4','5','6','7','8','9','10']
for fname2 in F_NAME2:
	for fname3 in F_NAME3:
		file_name = F_NAME1+fname2+'_'+fname3
		print 'Current Processing:',file_name
		h_file = open(file_name,'r')
		#dummy one
		print 'Building Vector Dictionary'

		dict = {'LU YuXun':-0.123}
		for lines in h_file:
			l_str = lines.split(' ')
			#get the key
			dict_key = l_str[0]
			#preprocess the vector
			del l_str[0] #the first one, A.K.A the key
			del l_str[ len(l_str) - 1 ] #the '\n'
			vec = map(float, l_str) #get the vector
			dict[dict_key] = vec#build the dictionary
		#	print 'the vec is:',dict[dict_key]
		#	print 'the vect is',dict[dict_key]
		#	print 'the key is',dict_key
			#dict.get('key','deafult') is another solution
		#	print dict.has_key(dict_key)#judge if the dict has the key
		#	raw_input('Press any key to continue')
		h_file.close()
		for wds in word_list:
			if not dict.has_key(wds):
				print 'Warning:',wds,'has no vector'
		#After building the vector-dictionary
		#find the word in wordlist
		print 'Pooling...'
		pool_dict = {'Lu YUXUN':-0.123}
		unique_word_list = set(word_list)
		for wd in unique_word_list:
			div_factor = len(dict_synsets[wd]) - 1;
			for keys in dict_synsets[wd]:
				if not ( len(keys) == 0 ):
					if dict.has_key(keys):
					#The synsets not in vector dictionary would be 0
						if pool_dict.has_key(wd):#pooling
			#				print wd,'found in pool_dict'
							i = 0
							while i < len(pool_dict[wd]):
								pool_dict[wd][i] = (pool_dict[wd][i] + dict[keys][i])
								i = i + 1
						else:	#initiallization
			#				print wd,'initiallization'
							pool_dict[wd] = dict[keys]
		#			else:
		#				print 'No vector:',keys
				#i = 0
				#while i < len(pool_dict[wd]):	
				#	pool_dict[wd][i] = pool_dict[wd][i] /( len(dict_synsets[wd])-1 )
				#	i = i + 1
				#print wd
		#The pool_dict has one more item(Dummy item) than unique_word_list, so len(pool_dict) - (unique_word_list) = 1
		#print len(pool_dict)
		#print len(unique_word_list)
		for wd in unique_word_list:
			i = 0
			while i < len(pool_dict[wd]):
				pool_dict[wd][i] = pool_dict[wd][i] / ( len(dict_synsets[wd]) - 1)
				i = i + 1
		#Calculate the cosine similarity
		print 'Calculating the similarity...'
		i = 0
		file_name_result = file_name + '_res'
		f_result = open(file_name_result,'w')
		while i < len(word_list):
			up = 0
			down = 0
			wd1 = word_list[i]
			wd2 = word_list[i+1]
			j = 0
			while j < len(pool_dict[wd1]):
				up = up + pool_dict[wd1][j] * pool_dict[wd2][j]
				j = j + 1
			wd1_down = 0
			wd2_down = 0
			j = 0
			while j < len(pool_dict[wd1]):
				wd1_down = wd1_down + pool_dict[wd1][j] * pool_dict[wd1][j]
				wd2_down = wd2_down + pool_dict[wd2][j] * pool_dict[wd2][j]
				j = j + 1
			wd1_down = math.sqrt(wd1_down)
			wd2_down = math.sqrt(wd2_down)
			down = wd1_down * wd2_down
			sim = up/down
			#print wd1 + '-' + wd2,sim
			f_result.write(wd1 + '-' + wd2 + ',' + str(sim) + '\n' )
			i = i + 2
		f_result.close()
