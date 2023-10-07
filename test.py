import json 
with open('data.json', 'r', encoding='utf8') as f :
    data = json.loads(f.read())
    for x in data : 
        data.append('h')

print(match)  
