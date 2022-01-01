import requests
from bs4 import BeautifulSoup
import re
import json


## scrape Nouns 
URL ='http://latindictionary.wikidot.com/printer--friendly//portable:latin-nouns'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="page-content")

nouns = results.get_text()

result = re.findall('\(.*?\)', nouns)

def get_nouns(result): 
    nounsss = []
    for res in result: 
        options = ['(plural)', '(season)', '(divine)', '(Divine)', '(mail)', '(of a bow and arrow)', '(elected magistrate)', '(s.)', '(pl.)', '(fig)', '(Insect)', '(alphabet)', '(Unit of measure, lb.)', '(; Neuter)', '(; Masculine)', '(usually loud)', '(figurative)', '(of soldiers)']
        if res in options: 
            res = None 
        
        elif res.endswith('(-ium)'):
            res = None
        else: 
            res = list(res.split(" "))
            nounsss.append(res)
    return nounsss

noun_list = get_nouns(result)

def get_decl(noun): 

    '''
    Parameters: genitive noun
    Returns: declension the noun is a part of 
    '''
   
    if noun.endswith('ae'): 
        return 1
    if noun.endswith('ei'): 
        return 5
    if noun.endswith('i'): 
        return 2
    if noun.endswith('is'): 
        return 3
    if noun.endswith('us'): 
        return 4


def find_noun_base (noun): 
    
    
    endings = ['ae', 'ei', 'i', 'is', 'us']
    for ending in endings: 
        if noun.endswith(ending): 
            base = noun[:-len(ending)]
            return base 

def create_vocab_list(noun_list):
    nouns_vocab_list = []
    get_rid_of = r'[\'\;\,\(\)]'
    pl_end = ["orum", "arum", "uum", "erum", "ium", "um"]
    
    for noun in noun_list: 
        if len(noun) == 3 and not re.sub(get_rid_of, '', noun[1]).endswith(tuple(pl_end)): # get rid of plural nouns and any noun that doesn't have nom, gen, and gender listed
            
            nom = re.sub(get_rid_of, '', noun[0])
            gen = re.sub(get_rid_of, '', noun[1])
            noun_base = find_noun_base(gen)
            decl = get_decl(gen)
            gender = re.sub(get_rid_of, '', noun[2])
            noun_dict = ({"nom": nom,
                "noun_base": noun_base,
                "noun_decl": decl,
                "gender": gender})
            #noun = noun_dict
             
            nouns_vocab_list.append(noun_dict)
    return nouns_vocab_list

## add declension number and noun base to noun dictionary, instead of using regex in grammar.py

nouns_vocab_list = create_vocab_list(noun_list)


def save_nouns(nouns_vocab_list): 
    with open('nouns.json', 'w') as fp:
        json.dump(nouns_vocab_list, fp)

save_nouns(nouns_vocab_list)


