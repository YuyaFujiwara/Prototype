import nltk
import pprint

from nltk import word_tokenize

Sentence="Two frogs, a father and his son, accidently fell into a bucket of milk. They started swimming for their lives. They swam for a long time, but there seemed no hope of their getting out. The father soon gave up and drowned. The son carried on swimming. During this time, the milk had begun to form a ball of butter. Using this island of butter as a platform, he managed to hop out of the bucket."

T_sentence=nltk.word_tokenize(Sentence)
Tagged=nltk.pos_tag(T_sentence)

print(Tagged)
print('\n')

print("1:")#progressive aspect
for tag in Tagged: 
	if tag[1]=="VBG":
		print(tag)
		
print('\n')
		
print("2:")#perfect aspect
for tag in Tagged: 
	if tag[0]=="had" or tag[0]=="have":
		print(tag)

print('\n')

print("3:")#past tense
for tag in Tagged:
	if tag[1]=="VBD":
		print(tag)
	
print('\n')

print("4:")#regular past tense
for tag in Tagged:
	if tag[1]=="VBD":
		print(tag)
	
print('\n')

print('5')#underline each verb group
for i,tag in Tagged:
	if tag[1]=="VB" or tag[1]=="VBD" or tag[1]=="VBG" or tag[1]=="VBN" or tag[1]=="VBP" or tag[1]=="VBZ":
		print(tag)
	#	print(Tagged[i])
		
