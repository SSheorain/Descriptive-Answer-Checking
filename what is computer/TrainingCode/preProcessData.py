import sys
sys.path.append('../pythonScripts')

from pr1 import process1
from pr2 import process2
from pr3 import process3

nameTrainingIn = '../TrainingFile/train.tsv'
nameTrainingOut1 = '../AdditionalFiles/train_rel_2_2.tsv'
nameTrainingOut2 = '../AdditionalFiles/train_rel_2_3.tsv'


process1( nameTrainingIn, nameTrainingOut1, test = False) #correcting mispelled words
print '\nStemming'
process2( nameTrainingOut1, nameTrainingOut2 ) 
print 'Calculating Features'
process3( 1, False , nameTrainingOut2) 