import collections, re
from util import *

def feature1(**kwargs):
	# This function searches if an essay of a given set has the answers needed 
	# for a high score using regular expressions.

	# 'answer' is the list of having answer or not.
	# 'index' is the index of the current answer that is being looking for.
	# 'pats' is the list of regular expressions used to find an answer.
	# If a match is found for a text, 'line_match' that match
	#  'fi' is the list of answers as vectors of words. 'fi' is updated 
	# in this function.
	# 'fi2' is the dictionary of of words for each match of each answer,
	# 'matchs' is a list of matches for each answer.
	# 'fet' is the function that actually searches for an answer in an 
	# essay given the list of regular expressions and the text of the essay.
	# 'update_ans' updates the list 
	# 'reset' (in some sets used) reset the necessary values to search for a
	# new answer.

	text = kwargs['text']
	fi = kwargs['fi'] 
	Id = kwargs['Id']
	score = kwargs['score']
	score2 = kwargs['score2']
	fi2 = kwargs['fi2']
	line_match = None
	answer = []
	matchs = []
	
	index = 0
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(comput|computer|Computer)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(electron|electronic|electric)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(machin|machine|machines)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(program|programmable)+\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(set of (instruct|instruction|instructions))+\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(manipul|manipulate|manipulates)+\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(solv|solve|solves)+\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(problem|problems|prob)+\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(data|inform|information)+\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(programm|programming)+\w*( \w+){0,4}") )	
	ans, line_match = fet(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(devic|device|devices)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)		
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(perform|performs)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)((gener|generate) result)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(accept|accepts)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)((mathemat|mathematical) and logic (oper|operations))+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(execut|execute|executes)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}\w*(.*?)(oper|operation|operations)+\w*( \w+){0,4}") )
	ans, line_match = fet(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	return answer, fi, fi2
