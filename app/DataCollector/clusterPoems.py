import json, re

def clusterPoemsByPoets():
    with open("../static/poems.json", "r")as fr, \
        open("../static/poet2poems.json", "w") as fw:
        data = json.load(fr)
        poet2poems = {}  # {key:value} , {author: list_of_poems}
        for key in data.keys():
            author = data[key]["author"]
            title = data[key]["title"]
            print(author, title)
            if author not in poet2poems.keys():
                poet2poems[author] = [title]
            else:
                poet2poems[author].append(title)
            #print(poet2poems)
        json.dump(poet2poems, fw)

clusterPoemsByPoets()