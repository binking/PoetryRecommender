from urllib import request
import re, json

def getImage(kw):
    urlExp = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={0}&ct=201326592&v=flip"
    reExp = r'"thumbURL":"(http://.*?\.jpg)"'
    # transfer keyword to unicode
    kw_bytes = kw.encode("utf-8")
    kw_unicode = str(kw_bytes).replace(r"\x", "%").replace("'", "") # remove ' and replace \x with %
    kw_unicode = re.sub(r"^b", "", kw_unicode) # remove b char
    search_url = urlExp.format(kw_unicode)
    with request.urlopen(search_url) as rq:
        pageCode = rq.read()
        pageCode = str(pageCode, encoding="utf-8", errors="ignore")
        img_url = re.search(reExp, pageCode).group(1)
        return img_url

def crawlImages():
    with open("../static/poet2image.json", "w") as fw, open("../static/poems.json", "r") as fr:
        data = json.load(fr)
        poet2image = {}
        for key in data.keys():
            author = data[key]['author']
            print(author)
            if author not in poet2image:
                poet2image[author] = getImage(author)
        json.dump(poet2image, fw)
crawlImages()
'''
def test():
    keyword = u"余光中"
    getImage(keyword)
test()'''