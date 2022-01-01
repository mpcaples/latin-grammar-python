import requests
from bs4 import BeautifulSoup
import re
import json

## Scrape Verbs 

URL ='http://latindictionary.wikidot.com/printer--friendly/portable:latin-adjectives'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="page-content")

adjectives = results.get_text()

result = re.findall('\(.*?\)', adjectives)

def get_adjectives(result): 
    adjectives = []
    for res in result: 
        res = list(res.split(" "))
        adjectives.append(res)
    return adjectives

adjective_list = get_adjectives(result)

def create_adjective_list(adjective_list):
    adjectives_vocab_list = []
    for adj in adjective_list: 
        if len(adj) == 3: 
            get_rid_of = r'[\'\;\,\(\)]'
            adj_dict = ({"masc": re.sub(get_rid_of, '', adj[0]),
                "fem": re.sub(get_rid_of, '', adj[1]),
                "neut": re.sub(get_rid_of, '', adj[2])})
           
            adjectives_vocab_list.append(adj_dict)
    return adjectives_vocab_list

adj_vocab_list = create_adjective_list(adjective_list)


def save_adjectives(adj_vocab_list): 
    with open('adjectives.json', 'w') as fp:
        json.dump(adj_vocab_list, fp)

save_adjectives(adj_vocab_list)

