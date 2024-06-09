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

result = re.findall('\((.*)', verbs)

def get_verbs(result): 
    verbs = []
    for res in result: 

        res = res
            
        result_split = res.split(")")[0]
        word = list((result_split.split(" ")))
        trans = (res.split(")")[1]).replace(';', ',')
        trans = list(trans.split(","))

        verbs.append({
            "word": word,
            "trans": trans
        })
    return verbs

verb_list = get_verbs(result)

def create_verb_list(verb_list):
    verbs_vocab_list = []
    for verb in verb_list: 
        if len(verb["word"]) == 4: 
            get_rid_of = r'[\'\;\,\(\)]'
            verb_stem_act = re.sub("re$", '', re.sub(get_rid_of, '', verb["word"][1]))
            translations = []
            for transes in verb["trans"]:
                transes = transes.replace(' — ', '').strip().lower()
                translations.append(transes)
            verb_dict = ({
                "verb_stem_act": verb_stem_act,
                "transitive": False if re.sub(get_rid_of, '', verb["word"][0]).endswith('r') else True, 
                "pres_act_1st_sg": re.sub(get_rid_of, '', verb["word"][0]),
                "pres_act_inf": verb_stem_act + 're',
                "perf_act_inf": re.sub(get_rid_of, '', verb["word"][2]),
                "perf_pass_part": re.sub(get_rid_of, '', verb["word"][3]), 
                "translation": translations
            })
           
            verbs_vocab_list.append(verb_dict)
    print(verbs_vocab_list)
    return verbs_vocab_list

verbs_vocab_list = create_verb_list(verb_list)


def save_verbs(verbs_vocab_list): 
    with open('verbs.json', 'w') as fp:
        json.dump(verbs_vocab_list, fp)

save_verbs(verbs_vocab_list)
# after saving the verbs I manually changed ALL of the intransitive verbs to {verb["transitive"]: false}, so do not mess with this file - sorry but I have to :(