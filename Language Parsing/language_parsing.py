import re
from nltk import pos_tag
from nltk import word_tokenize
from nltk import RegexpParser
from nltk import Tree

'''
.compile(): create a regular expression object which can be used to match text
            the match object lets you know what piece of text the regular expression matched, and at what index the match begins and ends
.match():   look for a "single" match to the regular expression that starts at the "beginning" of the string
            if no match is found .match() will return None, otherwise, returns matched object
            * will only return one piece of matching text
.group():   access the matched text
'''
regular_expression_object = re.compile("[A-Za-z]{4}")
result = regular_expression_object.match("Totoro")
#print(result.group(0))

# OR in one line
result = re.match("[A-Za-z]{4}", "Totoro")
#print(result.group(0))


'''
.search():  look through an entire piece of text and return a match object for the first match to the regular expression given 
            if no match is found .search() will return None
            * will only return one piece of matching text
'''
result = re.search("\w{8}","Are you a Munchkin?")   # same arguments with .match() would return None!
#print(result.group(0))


'''
.findall(): returns a list of non-overlapping matches of the regular expression in the string 
            * will return all occurrences of matching text
'''
text = open("text_for_findall.txt",encoding="utf-8").read().lower()
list_of_matches = re.findall("\w{8}", text)
#print(list_of_matches)

# finding all the occurrences of a word
num_munchkins = len(re.findall("munchkins", text))
#print("number of munchkins in the text: {}".format(num_munchkins))


'''
from nltk import pos_tag
pos_tag():  gets a list as input and returns list of (word, pos_abbreviations) tuples
            list of all pos abbreviations available in part_of_speech_abbreviations.txt
'''
text = open("text_for_pos.txt",encoding="utf-8").read().lower()
tokenized_text = word_tokenize(text)
pos_tagged_text = pos_tag(tokenized_text)
#print(pos_tagged_text)


'''
from nltk import RegexpParser
chunk_grammar:  regular expression you build to find chunks

Example grammars:   "AN: {<JJ><NN>}"                        adjective noun              e.g. wicked witch
                    "NP: {<DT>?<JJ>*<NN>}"                  noun phrases                e.g. the wicked witch
                    "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"     verb phrases version 1      e.g. said the cowardly lion
                    "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"     verb phrases version 2      e.g. the cowardly lion said
                    
                    """NP:  {<.*>+}                         <.*>+ matches every pos in sentence
                            }<VB.?|IN>+{"""                 filter out any verbs or prepositions 

from nltk import Tree: pretty print the the chunked text
'''
# first example: AN chunking
text = open("text_for_AN_chunking.txt",encoding="utf-8").read().lower()
tokenized_text = word_tokenize(text)
pos_tagged_text = pos_tag(tokenized_text)

chunk_grammar = "AN: {<JJ><NN>}"
chunk_parser = RegexpParser(chunk_grammar)
chunked_text = chunk_parser.parse(pos_tagged_text)
Tree.fromstring(str(chunked_text)).pretty_print()

# second example: NP chunking
text = open("text_for_NP_chunking.txt", encoding='utf-8').read().lower()
tokenized_text = word_tokenize(text)
pos_tagged_text = pos_tag(tokenized_text)

chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(chunk_grammar)
chunked_text = chunk_parser.parse(pos_tagged_text)
Tree.fromstring(str(chunked_text)).pretty_print()

# third example: chunk filtering
text = open("text_for_filtering_chunks.txt", encoding='utf-8').read().lower()
tokenized_text = word_tokenize(text)
pos_tagged_text = pos_tag(tokenized_text)

chunk_grammar = "Chunk: {<.*>+}"    # whole sentence as a chunk
chunk_parser = RegexpParser(chunk_grammar)
chunked_text = chunk_parser.parse(pos_tagged_text)
Tree.fromstring(str(chunked_text)).pretty_print()

chunk_grammar = """NP: {<.*>+}
                        }<VB.?|IN>+{"""   # whole sentence as a chunk
chunk_parser = RegexpParser(chunk_grammar)
chunked_text = chunk_parser.parse(pos_tagged_text)
Tree.fromstring(str(chunked_text)).pretty_print()



















