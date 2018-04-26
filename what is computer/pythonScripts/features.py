from features1 import *

def feature(**kwargs):
	
	Id = kwargs['Id'] 			
	set = kwargs['set'] 		
	if int(Id) % 100 == 0: print  Id
	# It calls a different function for each set.
	if set == 1:			return feature1(**kwargs)
	else: 
		return [0], fi, fi2


