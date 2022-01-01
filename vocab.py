import json

with open('vocab_scraper/nouns.json', 'r') as fp:
    nouns = json.load(fp)
with open('vocab_scraper/verbs.json', 'r') as fp:
    verbs = json.load(fp)
with open('vocab_scraper/adjectives.json', 'r') as fp:
    adjectives = json.load(fp)



vocab = {
    "nouns": nouns, 
    "verbs": verbs, 
    "adjectives": adjectives}


