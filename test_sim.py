import math
#Calculate the cosine similarity
print 'Calculating the similarity...'
               # i = 0
               # file_name_result = file_name + '_res'
               # f_result = open(file_name_result,'w')
               # while i < len(word_list):
up = 0
down = 0
vec1 = [0.5,0.5]
vec2 = [-0.5,-0.5]
                #        wd1 = word_list[i]
                #        wd2 = word_list[i+1]
j = 0
while j < len(vec1):
	up = up + vec1[j] * vec2[j]
 	j = j + 1
wd1_down = 0
wd2_down = 0
j = 0
while j < len(vec1):
       	wd1_down = wd1_down + vec1[j] * vec1[j]
        wd2_down = wd2_down + vec2[j] * vec2[j]
        j = j + 1
wd1_down = math.sqrt(wd1_down)
wd2_down = math.sqrt(wd2_down)
down = wd1_down * wd2_down
sim = up/down
print 'vec1:',vec1
print 'vec2:',vec2
print 'sim:',sim
			#print wd1 + '-' + wd2,sim
                #        f_result.write(wd1 + '-' + wd2 + ',' + str(sim) + '\n' )
                	 
		#i = i + 2
                #f_result.close()
