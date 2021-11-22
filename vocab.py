import json

with open(r'C:\Users\Owner\Documents\python\latin-grammar\latin-grammar-python\vocab_scraper\nouns.json', 'r') as fp:
    nouns = json.load(fp)
with open(r'C:\Users\Owner\Documents\python\latin-grammar\latin-grammar-python\vocab_scraper\verbs.json', 'r') as fp:
    verbs = json.load(fp)


vocab = {
    "nouns": nouns, 
    "verbs": verbs, 
    "adjectives": ['laeta', 'fessa', 'magna']}


