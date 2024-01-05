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

def make_ablative (base, decl): 
    '''
    Returns the ablative form of a noun based on its base and declension
    '''
    abl_sg_endings = {
        1: "a", 
        2: "o", 
        3: "e", 
        4: "u", 
        5: "e"
    }
    ablative = base + abl_sg_endings[decl]
    return ablative
make_ablative('domin-', 2)

def make_abl_agent (ablative): 
    '''Returns ablative of agent prepositional phrase, given an ablative form of a noun
    '''

    # if ablative starts with a, return "ab" else return "a"
    vowels = ['a', 'i', 'e', 'o', 'u']
    for vowel in vowels: 
        if ablative.lower().startswith(vowel): 
            return f'ab {ablative}'
    else: 
        return f'a {ablative}'
#noun_test = random.choice(vocab["nouns"])
#print(make_abl_agent(make_ablative(find_noun_base(noun_test), get_decl(noun_test))))
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

def get_third_person_passive_verb (verb_stem): 
    verb = verb_stem + 'tur'
    return verb

def choose_sentence_type(): 
    sentence_types = ["active", "passive"]
    return random.choice(sentence_types)

def generate_sentence (): 

    '''
    Generates a sentence randomly, from a trivial subset of the Latin language.  
    '''

    #choose whether sentence is active or passive 
    sentence_type = choose_sentence_type()
    if sentence_type == "active": 
    
        noun_dict = random.choice(vocab["nouns"])
        verb_dict = random.choice(vocab["verbs"])
        verb_stem = get_verb_stem(verb_dict)
        if verb_dict["transitive"] == True: 
            subject = make_subject(noun_dict).lower()
            
            dir_obj_raw = random.choice(vocab["nouns"])
            dir_obj = make_DO_version2(find_noun_base(dir_obj_raw), get_decl(dir_obj_raw)).lower()
            verb = get_third_person_verb(verb_stem).lower()
            adjective_raw = random.choice(vocab["adjectives"])
            adjective = make_adjective_agree(noun_dict, adjective_raw).lower()
            sentence = f'{subject} {adjective} {dir_obj} {verb}'
            sentence_info_dict = {"subject": noun_dict, 
                           "verb": verb_dict, 
                           "dir_obj": dir_obj_raw, 
                           "adjective": adjective_raw}
        else: 
            subject = make_subject(noun_dict).lower()
            verb = get_third_person_verb(verb_stem).lower()
            adjective_raw = random.choice(vocab["adjectives"])
            adjective = make_adjective_agree(noun_dict, adjective_raw).lower()
            sentence = f'{subject} {adjective} {verb}' 
            sentence_info_dict = {"subject": noun_dict, 
                                  "adjective": adjective_raw, 
                                  "verb": verb_dict}
        return {"sentence": sentence, "sentence_info_dict": sentence_info_dict}

    elif sentence_type == "passive": 
        noun_dict = random.choice(vocab["nouns"])
        verb_dict = random.choice(vocab["verbs"])
        if verb_dict["transitive"] == False: 
            verb_dict = random.choice(vocab["verbs"])
            verb_stem = get_verb_stem(verb_dict)
        else: 
            verb_stem = get_verb_stem(verb_dict)

        subject = make_subject(noun_dict).lower()
        ablative_dict = random.choice(vocab['nouns'])
        abl_agent = make_abl_agent(make_ablative(find_noun_base(ablative_dict), get_decl(ablative_dict)))
        verb = get_third_person_passive_verb(verb_stem).lower()
        sentence = f'{subject} {abl_agent} {verb}'
        sentence_info_dict = {"subject": noun_dict, 
                              "verb": verb_dict, 
                              "abl_agent": ablative_dict}
        return {"sentence": sentence, "sentence_info_dict": sentence_info_dict}




def main(): 
    print(generate_sentence())

if __name__ == '__main__': 

    main()