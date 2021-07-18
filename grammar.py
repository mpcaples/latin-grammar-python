import random 
import re

vocab = {
    "nouns": [
        {"nom": "puella", "gen": "puellae", "gender": "fem"}, 
        {"nom": "ager", "gen": "agris", "gender": "masc"},
        {"nom": "puer", "gen": "pueri", "gender": "masc"},
        {"nom": "fructus", "gen": "fructus", "gender": "masc"}, 
        {"nom": "dies", "gen": "diei", "gender": "masc"}
    ], 
    "verbs": ['amat', 'videt', 'vexat', 'verberat']}

def get_decl(noun): 

    '''
    Parameters: noun dict
    Returns: declension the noun is a part of 
    '''
    #first_decl_gen = "ae"
    str = noun["gen"]
    first_decl = re.search("ae$", str)
    second_decl = re.search("i$", str)
    third_decl = re.search("is$", str)
    fourth_decl = re.search("us$", str)
    fifth_decl = re.search("ei$", str)
    if (first_decl !=None): 
        return 1
    if (fifth_decl != None): 
        return 5
    if (second_decl != None) : 
        return 2
    if (third_decl != None): 
        return 3
    if (fourth_decl != None): 
        return 4

def find_noun_base (noun): 
    
    '''
    Parameters: dictionary that describes a noun in the nomanitive case, genitive case, and its gender
    Returns: the base of the noun
    '''
    
    gen = noun["gen"]
    decl = get_decl(noun)
    if decl == 1: 
        base = re.sub('ae$', "", gen)
    if decl == 5: 
        base = re.sub('ei$', "", gen)
    if decl == 2: 
        base = re.sub('i$', "", gen)
    if decl == 3: 
        base = re.sub('is$', "", gen)
    if decl == 4: 
        base = re.sub('us$', "", gen)
    
        
    return base


def make_subject (noun): 
    '''
    returns the nominative form of the noun
    '''
    return noun["nom"]

# e.g. a call to the following function: 
#       make_direct_object(find_noun_base(noun), get_decl(noun))
def make_DO_version2 (base, decl):
    ending = ""
    if decl == 1: 
        ending = "am"
    elif decl == 2: 
        ending = "um"
    elif decl == 3: 
        ending = "em"
    elif decl == 4: 
        ending = "um"
    elif decl == 5: 
        ending = "em"
    accusative = base + ending 
    return accusative


def generate_sentence (): 
    '''
    Trivial subset of the Latin language 
    '''

    subject = make_subject(random.choice(vocab["nouns"]))
    dir_obj = random.choice(vocab["nouns"])
    dir_obj = make_DO_version2(find_noun_base(dir_obj), get_decl(dir_obj))
    verb = random.choice(vocab["verbs"])

    sentence = subject + " " + dir_obj + " " + verb
    return sentence 



def main(): 
    print(generate_sentence())

if __name__ == '__main__': 

    main()