from Poem import Poem
from PoemsCrawler import PoemsCrawler
from DBAccessor import DBAccessor
import json

url = "http://www.chinapoesy.com/XianDaiList_{0}.html"

def run():
    all_poems = []
    for i in range(1, 3):
        pc = PoemsCrawler(url.format(str(i)))
        pc.generateUrls()
        pc.collectPoems()
        all_poems.extend(pc.poems_list)

    dba = DBAccessor("./static/poems.json")
    dba.write_json(all_poems)

run()
'''
def readJson():
    with open("./static/poems.json", "r") as fr:
        data = json.load(fr)
        print(data["1001"])

readJson()
'''