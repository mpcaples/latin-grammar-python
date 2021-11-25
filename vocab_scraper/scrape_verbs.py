import requests
from bs4 import BeautifulSoup
import re
import json

## Scrape Verbs 

URL ='http://latindictionary.wikidot.com/printer--friendly//portable:latin-verbs'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="page-content")

verbs = results.get_text()

result = re.findall('\(.*?\)', verbs)

def get_verbs(result): 
    verbs = []
    for res in result: 
        res = list(res.split(" "))
        verbs.append(res)
    return verbs

verb_list = get_verbs(result)

def create_verb_list(verb_list):
    verbs_vocab_list = []
    for verb in verb_list: 
        if len(verb) == 4: 
            get_rid_of = r'[\'\;\,\(\)]'
            verb_stem_act = re.sub("re$", '', re.sub(get_rid_of, '', verb[1]))
            verb_dict = ({
                "verb_stem_act": verb_stem_act,
                "pres_act_1st_sg": re.sub(get_rid_of, '', verb[0]),
                "pres_act_inf": verb_stem_act + 're',
                "perf_act_inf": re.sub(get_rid_of, '', verb[2]),
                "perf_pass_part": re.sub(get_rid_of, '', verb[3])})
           
            verbs_vocab_list.append(verb_dict)
    return verbs_vocab_list

verbs_vocab_list = create_verb_list(verb_list)


def save_verbs(verbs_vocab_list): 
    with open('verbs.json', 'w') as fp:
        json.dump(verbs_vocab_list, fp)

save_verbs(verbs_vocab_list)