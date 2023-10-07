from flask import Flask , render_template
import json

app = Flask(__name__)

@app.route("/")
def index() : 
    with open('data.json', 'r', encoding="utf8") as f :
        data = json.loads(f.read())
    return render_template('index.html', data = data)

@app.route("/manga/<id>")
def manga(id) : 
    print(id)
    with open('data.json', 'r', encoding="utf8") as f :
        data = json.loads(f.read())
        title = data[int(id)]['title']
        price = data[int(id)]['price']
        description = data[int(id)]['description']
        image = data[int(id)]['image']
    return render_template("product.html", title=title, price=price,description=description, image=image, data = data[0:10])

@app.route("/search/<q>")
def search(q) : 
    match = []
    with open('data.json', 'r', encoding='utf8') as f :
        data = json.loads(f.read())
        for x in data :
            if q in x['title'] or q in x['description'] :
                match.append(x)
    print(match)
    return render_template('search.html', data=match)    


        

if __name__ == "__main__" :
    app.run()