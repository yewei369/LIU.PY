#!/usr/bin/env/ python3

#Student I: junli559 (Jun Li)
#Student II: vinda604 (Vinod Kumar Dasari)


import sys
import os
from collections import OrderedDict 
from operator import getitem 

##### Pre-defined Functions ----BELOW  ######################
def display_arg(verb):   ## display all arguments/input
    ## verb, if True required to print arguments   
    position=1
    for argument in sys.argv:
        if verb:
            print("Argument %d: %s" % (position,argument))
        position+=1
    return position

def check_arg(mode=1):  ## check if arguments have correct form
    ## mode, 1 for text_stats_1.py; 2 for generate_text_1.py
    if sys.argv[0].lower().endswith("*.py"):  ## check if the script file is normal/missing
        raise NameError("The script file is missing or in a wrong format!")
        return False    
    if (len(sys.argv)-1)>0 and not os.path.isfile(sys.argv[1]): ## check if txt file existed
        raise NameError("The file %s does not exist!" % sys.argv[1])
        return False 
    elif (len(sys.argv)-1)>0 and os.path.isfile(sys.argv[1]) and mode==1:
        return True
    elif (len(sys.argv)-1)>1 and os.path.isfile(sys.argv[1]) and (len(sys.argv)-1)<3 and mode==1:
        raise NameError("Argument 2/3 is missing!")
        return False
    elif mode==2:
        return True

def file_process(mode=1):    ## operations inside file to generate dict "words"
    ## mode, 1 for text_stats_1.py; 2 for generate_text_1.py

    words={}
    words_in_file=[]
    if mode==1:
        letters={}
        num_words=0
        num_uni_words=0
      
    with open(sys.argv[1],"r+") as fo:     
        for line in fo: ## iterations by line

            if mode==1:    
                for digit in line: ## summarizing alphabetic letters
                    if digit.isalpha() and digit.lower() in letters.keys():  ## update occurencies for letters
                        letters[digit.lower()]+=1                    
                    elif digit.isalpha() and digit.lower() not in letters.keys(): ## add new letters to dict
                        letters[digit.lower()]=1

            words_in_line=line.split()        
            for ind,word in enumerate(words_in_line): ## cleaning words                
                while not word[-1].isalnum():    ## drop symbol digits 
                    word=word[:-1]
                    if len(word)==0:
                        break
                words_in_file.append(word) ## create a new list of all words
                    

    for ind,word in enumerate(words_in_file):       
        if mode==1:
            num_words+=1
        if word.lower() not in words.keys(): ## add new words to dict
            words[word.lower()]={}
            words[word.lower()]['Occurencies']=1
            if mode==1:
                num_uni_words+=1
        elif word.lower() in words.keys():   ## update occurencies for words
            words[word.lower()]['Occurencies']+=1
                    
        if ind!=len(words_in_file)-1:
            if words_in_file[ind+1].lower() not in words[word.lower()].keys():
                words[word.lower()][words_in_file[ind+1].lower()]=1
            elif words_in_file[ind+1].lower() in words[word.lower()].keys():
                words[word.lower()][words_in_file[ind+1].lower()]+=1
    
    if mode==1:
        return letters,words,num_words,num_uni_words
    else:
        return words

def sort_words(words):    ## sort dict "words"
    presorted_words={} ## sorted by value for every dictionary element
    for key in words.keys():
        presorted_words[key]={}
        presorted_words[key]={k:v for k,v in sorted(words[key].items(),key=lambda x:x[1],reverse=True)}            
    sorted_words=OrderedDict(sorted(presorted_words.items(),key=lambda x: getitem(x[1], 'Occurencies'),reverse=True)) 
    return sorted_words

##### Pre-defined Functions ----ABOVE  ######################


if __name__=="__main__":

    display_arg(False)  ## display all arguments/input
    ok=check_arg(1)     ## check if arguments have correct form

    if ok:
        ## initialize variables
        sorted_letters={}  ## sorted by value
        sorted_words={}    ## sorted by sub-value 'Occurencies'

        ## operations inside file to generate dict "words" etc
        letters,words,num_words,num_uni_words=file_process(1)                            
        
        ## sort lists
        sorted_letters={k:v for k,v in sorted(letters.items(),key=lambda x: x[1],reverse=True)}    
        sorted_words=sort_words(words)

        ## print results
        #print("Here come the frequencies of alphabetic letters:")
        #for key,val in sorted_letters.items():
            #print(f"Alphabet {key} ({val} occurencies)")
              
        #print(f"\nThere are {num_words} words in the file.\n")
        print(f"\nThere are {num_uni_words} unique words in the file.\n")

        #print("Here come the frequencies of unique words:")
        #for key in sorted_words.keys():
            #print(f"{key} : ({sorted_words[key]['Occurencies']} occurencies)")

        print("\nHere come the most popular followers for top 5 words:")
        for ind,key in enumerate(dict(list(sorted_words.items())[0:5])):
            print(f"{key} : ( {sorted_words[key]['Occurencies']} occurencies)")
            for sub_ind,sub_key in enumerate(dict(list(sorted_words[key].items())[1:4])):
                print(f"---: {sub_key},{sorted_words[key][sub_key]}")
              
              
            

# Additional questions
# split() method is used to divide text into words, and lower() is used in checking reoccurencies of words with different cases
# dictionary is used for summarizing letters and nested dictionary for words, since both numbers of words and the subsequent words have been investigated.
# since it is required to summarize the occurencies of unique words and their following words, where both character and intergal data type needed, but the
# structures including list and tuple do not allow different types. However array is possible for different data types but not easy to assign a name for elements.
# Therefore dictionay is adopted

# Test
# python text_stats_1.py shakespeare.txt
# python text_stats_1.py students.txt

