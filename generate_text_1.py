#!/usr/bin/env python3

#Student I: junli559 (Jun Li)
#Student II: vinda604 (Vinod Kumar Dasari)

import sys
import os
from collections import OrderedDict 
from operator import getitem
import numpy as np
from text_stats_1 import *


if __name__=="__main__":

    display_arg(False) ##display all arguments/input
    ok=check_arg(2)   ## check if arguments have correct form

    if ok:
        ## initialize variables
        sorted_words={}    ## sorted by sub-value 'Occurencies'
        new_words=""       ## new generated words
        num_generated_words=1			   ## number of generated words
        current_word=sys.argv[2] ## current word which will be followed by others

        ## operations inside file to generate dict "words" etc
        words=file_process(2)                           
        
        ## sort words   
        sorted_words=sort_words(words)
        #print(dict(list(sorted_words.items())[:])) 

        ## Generate words
        num_max=int(sys.argv[3])        

        while num_generated_words<num_max and len(words[current_word])>1:
            ind_pool=[ind for ind,_ in enumerate(words[current_word])]       ## index of nested dict of current word
            key_pool=[key for key,_ in words[current_word].items()]     ## key of ...
            val_pool=[val for _,val in words[current_word].items()]     ## value of ...
            
            weights=[x/sum(val_pool[1:len(ind_pool)]) for x in val_pool[1:len(ind_pool)]]
            random_ind=np.random.choice(ind_pool[1:len(ind_pool)],p=weights)
            next_word=key_pool[random_ind]
            new_words+=" "+next_word
            current_word=next_word
            num_generated_words+=1
            #print(current_word,words[current_word])
        print(new_words)
         

    


# Test
# python generate_text_1.py shakespeare.txt king 500
# python generate_text_1.py students.txt exam 10


# additional requirements
#[ ] The program should not take over roughly a minute on IDA computers to generate a 500 word text.
#[ ] Generating a 2000 word text should not take a lot longer than generating a 500 word text.
