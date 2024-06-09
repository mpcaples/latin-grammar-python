import requests
from bs4 import BeautifulSoup
import re
import json


URL ='http://latindictionary.wikidot.com/printer--friendly/portable:latin-adjectives'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="page-content")

adjectives = results.get_text()

result = re.findall('\((.*)', adjectives)

def get_adjectives(result): 
    adjectives = []
    for res in result: 
        res = res
            
        result_split = res.split(")")[0]
        word = list((result_split.split(" ")))
        trans = (res.split(")")[1]).replace(';', ',')
        trans = list(trans.split(","))
        adjectives.append({
            "word": word,
            "trans": trans
        })
    return adjectives

adjective_list = get_adjectives(result)

def create_adjective_list(adjective_list):
    adjectives_vocab_list = []
    for adj in adjective_list: 
        if len(adj["word"]) == 3: 
            get_rid_of = r'[\'\;\,\(\)]'
            translations = []
            for transes in adj["trans"]:
                transes = transes.replace(' — ', '').strip().lower()
                translations.append(transes)
            adj_dict = ({
                "masc": re.sub(get_rid_of, '', adj["word"][0]),
                "fem": re.sub(get_rid_of, '', adj["word"][1]),
                "neut": re.sub(get_rid_of, '', adj["word"][2]), 
                "translation": translations
            })
           
            adjectives_vocab_list.append(adj_dict)
    print(adjectives_vocab_list)
    return adjectives_vocab_list

adj_vocab_list = create_adjective_list(adjective_list)


def save_adjectives(adj_vocab_list): 
    with open('adjectives.json', 'w') as fp:
        json.dump(adj_vocab_list, fp)

save_adjectives(adj_vocab_list)

