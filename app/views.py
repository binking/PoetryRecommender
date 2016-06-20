from app import app
from flask import render_template
import json

@app.route('/')
@app.route('/index')
def index():
    with open("app/static/poems.json", "r") as fr1:
        poems = json.load(fr1)
        # list_of_poems = [poems[key]["title"] for key in poems.keys()]
        poem2order = {} # hyper link to poem page
        for key in poems.keys():
            poem2order[poems[key]["title"]] = key
        return render_template("home.html", p2o = poem2order)

@app.route('/poem/<index>.html')
def showPoem(index):
    with open("app/static/poems.json", "r") as fr1, \
        open("app/static/poet2poems.json", "r") as fr2, \
        open("app/static/poet2image.json", "r") as fr3:
        all_poems = json.load(fr1)
        poems_of_poets = json.load(fr2)
        image_of_poets = json.load(fr3)
        specified_poem = all_poems[index]["text"]
        author = all_poems[index]['author']
        return render_template("poems.html",
                               author=author,
                               title = all_poems[index]['title'],
                               img_url = image_of_poets.get(author, ""),
                               list_of_poems=poems_of_poets.get(author, []),
                               sen_list=[seg.split("\r\n") for seg in specified_poem.split("\n\r\n")][1:])