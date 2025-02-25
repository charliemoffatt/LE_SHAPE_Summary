'''
GOAL: Design oligos based on dot bracket structure derived from SHAPE data
1. Parse dot bracket structure into a more useful format
2. Annotate base pairs based on what double-stranded region they are found in and what stem they are part of
--> ds region will just be coninous runs of bases
--> stem is where all brakets in the strucutre so far are closed
'''

class base:
    def __init__(self, genename):
        self.gene = genename # string
        self.i = 0 # integer, must be overwritten, index of base within structure, between 1 and 260
        self.j = 0 # integer, may be overwritten with the index of the base this one pairs to
        self.helix = 0 # integer, may be overwritten with the index of the double stranded region/ helix base is involved in
        self.stem = 0 # integer, may be overwritten with the index of the stem a base is found in, does not have to be paired!
        self.cr = False # logical, indicates if a base is within a previously defined critical region
        self.id = '' # string, indicates the identity of the base
    def __repr__(self):
        return(f"{self.gene}_{self.i}::{self.j}")