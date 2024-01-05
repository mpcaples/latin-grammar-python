import requests
from bs4 import BeautifulSoup
import re
import string
import json


## scrape Nouns 
URL ='http://latindictionary.wikidot.com/printer--friendly//portable:latin-nouns'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="page-content")

nouns = results.get_text()

result = re.findall('\((.*)', nouns)

def get_nouns(result): 
    nounsss = []
    for res in result: 
        options = ['(plural)', '(season)', '(divine)', '(Divine)', '(mail)', '(of a bow and arrow)', '(elected magistrate)', '(s.)', '(pl.)', '(fig)', '(Insect)', '(alphabet)', '(Unit of measure, lb.)', '(; Neuter)', '(; Masculine)', '(usually loud)', '(figurative)', '(of soldiers)']
        if res in options: 
            res = None 
        
        elif res.endswith('(-ium)'):
            res = None
        else: 
            res = res
            
            result_split = res.split(")")[0]
            word = list((result_split.split(" ")))
            trans = list((res.split(")")[1]).split(" "))

            nounsss.append({
                "word": word, 
                "trans": trans
            })
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
    get_rid_of = r'[\'\;\,\(\)\-]'
    pl_end = ["orum", "arum", "uum", "erum", "ium", "um"]
    
    for noun_dict in noun_list: 
        if len(noun_dict["word"]) == 3 and not re.sub(get_rid_of, '', noun_dict["word"][1]).endswith(tuple(pl_end)): # get rid of plural nouns and any noun that doesn't have nom, gen, and gender listed
            
            nom = re.sub(get_rid_of, '', noun_dict["word"][0])
            gen = re.sub(get_rid_of, '', noun_dict["word"][1])
            noun_base = find_noun_base(gen)
            decl = get_decl(gen)
            gender = re.sub(get_rid_of, '', noun_dict["word"][2])
            translations = []
            for transes in noun_dict["trans"]:
                if transes != '' and transes != '—' and transes != ';': 
                    transes = re.sub(get_rid_of, '', transes.lower())
                    translations.append(transes)
            noun_info = ({
                    "nom": nom,
                    "noun_base": noun_base,
                    "noun_decl": decl,
                    "gender": gender, 
                    "translation": translations
                })
             
            nouns_vocab_list.append(noun_info)
    print(nouns_vocab_list)
    return nouns_vocab_list

## add declension number and noun base to noun dictionary, instead of using regex in grammar.py

nouns_vocab_list = create_vocab_list(noun_list)


def save_nouns(nouns_vocab_list): 
    with open('nouns.json', 'w') as fp:
        json.dump(nouns_vocab_list, fp)

save_nouns(nouns_vocab_list)


