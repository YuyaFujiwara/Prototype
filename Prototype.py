import nltk
import pprint
import re
from operator import itemgetter

from nltk import word_tokenize

Sentence="Two frogs, a father and his son, accidently fell into a bucket of milk. They started swimming for their lives. They swam for a long time, but there seemed no hope of their getting out. The father soon gave up and drowned. The son carried on swimming. During this time, the milk had begun to form a ball of butter. Using this island of butter as a platform, he managed to hop out of the bucket."

T_sentence=nltk.word_tokenize(Sentence)
Tagged=nltk.pos_tag(T_sentence)
instancelist=[]

print(Tagged)
print('\n')

print("1:")#progressive aspect
for tag in Tagged: 
	if tag[1]=="VBG":
		print(tag)
		instancelist.append(tag)
print('\n')
		
print("2:")#perfect aspect
for tag in Tagged: 
	if tag[0]=="had" or tag[0]=="have":
		print(tag)
		instancelist.append(tag)
print('\n')

print("3:")#past tense
for tag in Tagged:
	if tag[1]=="VBD":
		print(tag)
		instancelist.append(tag)
print('\n')

print("4:")#regular past tense 
for tag in Tagged:
	if tag[1]=="VBD" and tag[0]==r'.*ed$': #<-I do not know why this line does not work.
		print(tag)
		instancelist.append(tag)
print('\n')

print('5')#underline each verb group
for i,tag in enumerate(Tagged):
	if tag[1]=="VB"or tag[1]=="VBD"or tag[1]=="VBG" or tag[1]=="VBN" or tag[1]=="VBP" or tag[1]=="VBZ":
		'''print(tag)
		print(Tagged[i+1])
		if tag[1]=="IN":''' #I tried to make "IN(preposition)+VB~"->verb group but it does not work.
		print(tag)
		print(Tagged[i+1])
		
print('\n')

print('6') #found instances in alphabetical list
thelist=set(instancelist)
instancelist=list(thelist)
sorted(instancelist,key=itemgetter(0))#sorted does not work well, disorder.
print(instancelist)