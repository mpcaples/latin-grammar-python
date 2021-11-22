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

def create_vocab_list(noun_list):
    nouns_vocab_list = []
    for noun in noun_list: 
        if len(noun) == 3: 
            get_rid_of = r'[\'\;\,\(\)]'
            noun_dict = ({"nom": re.sub(get_rid_of, '', noun[0]),
                "gen": re.sub(get_rid_of, '', noun[1]),
                "gender": re.sub(get_rid_of, '', noun[2])})
            #noun = noun_dict
            nouns_vocab_list.append(noun_dict)
    return nouns_vocab_list

nouns_vocab_list = create_vocab_list(noun_list)

def save_nouns(nouns_vocab_list): 
    with open('nouns.json', 'w') as fp:
        json.dump(nouns_vocab_list, fp)

save_nouns(nouns_vocab_list)


