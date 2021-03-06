from feat import *

import sys

reader = open('../TrainingFile/train_rel_2.tsv', 'r' )
SET = 1 #This number should be changed for each set 

possible_answers, fmatch = feat() # It reads the predefined possible answers
possible_answer = possible_answers[SET]

data = {}
num_labels = 0

for row in reader:
	line = row.split('\t')
	if not line[1] == str(SET):  continue
	Id = int(line[0])
	s1 = int(line[2])
	text = line[4]
	labels = [0] * len ( possible_answer )

	if s1 > 0:
		print '\nEssay score:\t%d\n%s' % (s1, text ) 
		print 'Which of the following answers does the essay have?\n'

		for i in range( len( possible_answer ) ):
		
			print '%d\t%s' % (i, possible_answer[i])
		
		print '%d\t%s' % ( len( possible_answer ) , 'Other')

		labels_entered = (raw_input ('\nWrite the numbers of the answers:\n')).split()

		for id_label in labels_entered:
			if int(id_label) == len( possible_answer): # It adds new answers to the possible answers.
				num_new_labels = int( ( (raw_input ('How many new answers do you want to add?\t')).split() )[0] )
				for i in range(num_new_labels):
					new_answer = raw_input( 'Type the new answer for this essay?\n')
					possible_answer.append( new_answer)
					labels.append( 1 )
				continue
			labels [ int(id_label) ] = 1

	data[Id] = labels 
	num_labels = len( possible_answer)
	print 'Do you wsh to continue?\n'
	cb = input('1. Continue \n 2. End\n')
	if cb == 2: break


ofile ="../TrainingCode/training/training_%d_label.csv" % ( SET )
filew = open(ofile, "w")	
filew.write("Id")

for i in range(num_labels):
	filew.write(",label_" + str(i) )

for Id in data:
	
	filew.write( '\n' + str(Id) )

	for i in range( num_labels ):
		if i < len( data[Id] ):
			filew.write( ',' + str(data[Id][i] ) )
		else:
			filew.write( ',0' )
