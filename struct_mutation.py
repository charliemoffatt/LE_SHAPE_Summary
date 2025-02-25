'''
GOAL: Design oligos based on dot bracket structure derived from SHAPE data
1. Parse dot bracket structure into a more useful format
2. Annotate base pairs based on what double-stranded region they are found in and what stem they are part of
--> ds region will just be coninous runs of bases
--> stem is where all brakets in the strucutre so far are closed
'''

class base:
    def __init__(self):
        self.i = 0 # integer, must be overwritten, index of base within structure, between 1 and 260
        #self.j = 0 # integer, may be overwritten with the index of the base this one pairs to
       # self.stem = 0 # integer, may be overwritten with the index of the stem a base is found in, does not have to be paired!
        self.cr = False # logical, indicates if a base is within a previously defined critical region
        self.id = '' # string, indicates the identity of the base
    def __repr__(self):
        return(f"{self.gene}_{self.i}::{self.j}")
    
class structure:
    def __init__(self, genename):
        self.genename = '' # string, name of gene
        #self.bases = [] #list of objects of class base
        self.stems = {} # dictionary key is stem ID: [] list of 2, i bases, then j bases

    def __repr__(self):
        return(self.genename) # not super descriptive but it's there

class oligo:
    def __init__(self):
########
# i, j dictionary -> 2 contincous runs i and j = 1 ds, then sort into stems
# def stem as compeletewd set of brackets
# all combos of helixes wi a stem --> calling what a helix is will be complex
# limit n helicies per stem
######### -> I think this makes the most sense to do in R actually