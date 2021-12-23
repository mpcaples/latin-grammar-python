import random 
import re
from vocab import vocab


def get_decl(noun): 

    '''
    Parameters: noun dict
    Returns: declension the noun is a part of 
    '''
    decl = noun["noun_decl"]
    return decl

def find_noun_base (noun): 
    
    '''
    Parameters: dictionary that describes a noun in the nomanitive case, genitive case, and its gender
    Returns: the base of the noun
    '''
    
    base = noun["noun_base"]   
    return base


def make_subject (noun): 
    '''
    returns the nominative form of the noun
    '''
    return noun["nom"]

# e.g. a call to the following function: 
#       make_direct_object(find_noun_base(noun), get_decl(noun))
def make_DO_version2 (base, decl):
    """
    Returns the accusative form of a noun based on its base and declension 
    
    """
    acc_endings = {
        1: "am",
        2: "um", 
        3: "em", 
        4: "em", 
        5: "em"
    }
   
    accusative = base + acc_endings[decl] 
    return accusative

def make_adjective_agree (subject, adjective):
    '''
    Returns an adjective that agrees in case, number, and gender with the noun which is in the parameter 
    NOTE: for now it will just modify the subject, but in future versions tweak so it can modify subject, DO, or both
    '''
    adj = adjective["fem"]
    adjective_base = re.sub('a$', "", adj)
    if subject['gender'] == 'Feminine': 
        return adjective_base + 'a'
    if subject['gender'] == 'Neuter': 
        return adjective_base + 'um'
    if subject['gender'] == 'Masculine': 
        return adjective_base + "us"

def get_verb_stem (verb): 
    return verb["verb_stem_act"]

def get_third_person_verb (verb_stem): 
    verb = verb_stem + 't'
    return verb


def generate_sentence (): 
    '''
    Generates a sentence randomly, from a trivial subset of the Latin language.  
    '''
    noun_dict = random.choice(vocab["nouns"])
    verb_dict = random.choice(vocab["verbs"])
    verb_stem = get_verb_stem(verb_dict)
    if verb_dict["transitive"] == True: 
        subject = make_subject(noun_dict).lower()
        
        dir_obj = random.choice(vocab["nouns"])
        dir_obj = make_DO_version2(find_noun_base(dir_obj), get_decl(dir_obj)).lower()
        verb = get_third_person_verb(verb_stem).lower()
        adjective = random.choice(vocab["adjectives"])
        adjective = make_adjective_agree(noun_dict, adjective).lower()
        sentence = f'{subject} {adjective} {dir_obj} {verb}'
    else: 
        subject = make_subject(noun_dict).lower()
        verb = get_third_person_verb(verb_stem).lower()
        adjective = random.choice(vocab["adjectives"])
        adjective = make_adjective_agree(noun_dict, adjective).lower()
        sentence = f'{subject} {adjective} {verb}' 
    return sentence 



def main(): 
    print(generate_sentence())

if __name__ == '__main__': 

    main()