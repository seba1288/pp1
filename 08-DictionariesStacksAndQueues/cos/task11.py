import json

movie = {
    "title":"mumdos",
    "year": 2032,
    "actor":{"leading":"uga","supporting":"buga"},
    "oscar":False,
    "awards": ['czaka','lorem','ipsum']    
}


x = json.dumps(movie)
f = open('favoritejson.json','w')
f.write(x)
f.close()