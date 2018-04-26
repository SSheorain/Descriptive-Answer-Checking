# This script contains some predefined answers for some of the sets.
# This script is called from label.py
import collections, re, math


def feat():

	feat = collections.defaultdict(lambda: [] )
	feat[1] =[]
	
	feat[1].append(	'comput')
	feat[1].append(	'electron')
	feat[1].append(	'machin')
	feat[1].append(	'program')
	feat[1].append(	'set of instruct')
	feat[1].append(	'manipul')
	feat[1].append(	'solv')
	feat[1].append(	'problem')
	feat[1].append(	'data')
	feat[1].append(	'programm')
	feat[1].append(	'devic')
	feat[1].append(	'perform')
	feat[1].append(	'gener result')
	feat[1].append(	'accept')
	feat[1].append(	'mathemat and logic oper')
	feat[1].append(	'execut')
	feat[1].append(	'oper')

	# With set 6, indexes of the answers were changed so that 
	# they have the same indexes as the regular expressions.
	# However, this is not necessary. They are only included
	# because they were part of the development phase.
	
	return feat, feat


