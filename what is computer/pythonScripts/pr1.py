import re, time, sys, time
from correct2 import * 
def cleantext(text, cr, SET):
	text=text.lower()
	text = text.replace('mr .', 'mr')
	textn = ""
	for let in text:
		if let.isalpha():		textn = textn + let
		elif let == '.':		textn = textn + " . "
		elif SET == '10' and let.isdigit():	#Keep digits for set 10
			textn = textn + let
		else:					textn = textn + ' '
	text = textn

	while text.find('  ') >= 0:		text = text.replace('  ', ' ')
	sentences = text.split()

	text = cr.correct(sentences[0]) #Correct the first word of an essay
	wordn = ""
	for i in range(len(sentences)-1):
		word = sentences[i+1]
		wordp = sentences[i]
		if i + 2 < len(sentences):	wordn = sentences[ i + 2 ]
		else: wordn = ""
		cword = cr.correct(word, wordp, wordn) #Correct mispelled words
		text = text + " " + cword

	return text #Return cleaned essay

def process1( nameFileIn, nameFileOut, test):
 
	print 'Correcting Mispelled Words'
		
	reader = open( nameFileIn, 'r' )
	fi = open( nameFileOut, 'w' )

	for row in reader: 
		line = row.split('\t')
		fi.write( "%s\t%s\t" % ( line[0] , line[1] ) )
		if not test: fi.write( "%s\t%s\t" % ( line[2] , line[3] ) )
		fi.write( line[len(line) -1] )
		print "hello"
		break

	lines = []

	for row in reader:
		lines.append( row.split('\t') )

	print "SET:\t1"
	cr = correct2(1)	# Initialization of spell corrector
	SET = str(1)

	now = 0
	for line in lines:				
		if not line[1] == SET : continue
		fi.write( "%s\t%s\t" % ( line[0] , line[1] ) )
		if not test: fi.write( "%s\t%s\t" % ( line[2] , line[3] ) )
		now += 1
		if now % 2 == 0: print  line[0] 
		text =  cleantext(line[ len(line) -1 ], cr, SET) # It corrects the essay
		text = text.replace( '  ', ' ')
		fi.write( text + '\n')

	
