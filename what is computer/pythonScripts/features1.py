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
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(comput|computer|Computer)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(electron|electronic|electric)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(machin|machine|machines)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(program|programmable)+( \w+){0,4}") )	
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)


	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(set of (instruct|instruction|instructions))+( \w+){0,4}") )	
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(manipul|manipulate|manipulates)+( \w+){0,4}") )	
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(solv|solve|solves)+( \w+){0,4}") )	
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(problem|problems|prob)+( \w+){0,4}") )	
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(data|inform|information)+( \w+){0,4}") )	
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(programm|programming)+( \w+){0,4}") )	
	ans, line_match = feat(text, pats)	
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(devic|device|devices)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)		
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(perform|performs)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)((gener|generate) result)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(accept|accepts)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)((mathemat|mathematical) and logic (oper|operations))+( \w+){0,4}") )
	ans, line_match = feat(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(execut|execute|executes)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(oper|operation|operations)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)
	
	index += 1
	if len(fi) < index +1:	fi.append( collections.defaultdict(lambda: 0.0) )
	ans = '0'
	pats = []
	pats.append( re.compile(r"(\w+ ){0,4}(.*?)(calcul|calculation|calculation)+( \w+){0,4}") )
	ans, line_match = feat(text, pats)
	answer, fi, matchs, fi2 = update_ans( ans, line_match, fi, index, matchs, answer, fi2)

	return answer, fi, fi2
