import json

class DBAccessor():
    def __init__(self, name):
        self.name = name

    def write_json(self, elements):
        id2ele = {}
        with open(self.name, 'w') as fw:
            for i, ele in enumerate(elements):
                id2ele[str(1001+i)] = {'title': ele.title, 'author': ele.author, 'text': ele.text, 'click': ele.click}
            json.dump(id2ele, fw, indent=4)

    def read_json(self):
        with open(self.name, 'r') as fr:
            data = json.load(fr)
            for key in data.keys():
                print(key, data.get(key, ""))
'''
def test():
   test_dict = {
    "1001": {'name': "Jiang", 'author': "dsfdsewef", 'text': "sdfsdfdsf", 'click': 200},
    "1002": {'name': "Xujie", 'author': "sdfdsdsfw", 'text': "sdfdsfdsfds", 'click': 100},
    "1003": {'name': "Zhang", 'author': "sdsdgsd", 'text': "sddsfsfwef", 'click': 1000}
   }
   with open("poems.json", "r") as fr:
       data = json.load(fr)
       for key in data.keys():
           print(data[key])
test()
'''