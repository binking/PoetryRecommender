from bs4 import BeautifulSoup
from urllib import request
import time
from Poem import Poem

class PoemsCrawler():

    def __init__(self, url):
        self.url = url
        self.poem_urls = []
        self.poems_list = []

    def generateUrls(self):
        while (True):
            with request.urlopen(self.url) as response:
                pageSoup = BeautifulSoup(response.read(), 'html.parser')
                table_of_poems = pageSoup.find('table', attrs={'class': 'List'})  # Now I found the aimed table
                for tr in table_of_poems.find_all('tr'):  # Now I should extract all urls pointed to peoms
                    for td in tr.findAll('td'):
                        self.poem_urls.append('http://www.chinapoesy.com/' + td.find('a').get('href')) # save all urls
                break
            print("Connection error came again, maybe you need to wait for 15s ")
            time.sleep(15) # if error merges, sleep, and access again

    def collectPoems(self):
        self.poem_urls.reverse()
        while(len(self.poem_urls) > 0):
            url = self.poem_urls.pop()
            with request.urlopen(url) as response:
                pageSoup = BeautifulSoup(response.read(), 'html.parser')

                # Extract poem's title
                head = pageSoup.find('title')
                head = head.text.strip().split('_')
                title = re.sub(r"\r\n", "", head[0]) # newline char may embed in title
                author = head[1][:-2] # exclude last two words
                # Extract poem's body
                script_tags = pageSoup.findAll('script', {'type': 'text/javascript'})
                body = script_tags[9].find_next('p')
                if len(body.text) < 20:
                    body = script_tags[9].find_next('div')
                body = body.text # you shuld remove title and author
                self.poems_list.append(Poem(title, author, body))
                print(title, author)
                continue
            print("Connection error came again, maybe you need to wait for 15s ")
            time.sleep(15)
            self.poem_urls.append(url)
'''
def test():
    pc = PoemsCrawler('http://www.chinapoesy.com/XianDaiList_1.html');
    pc.generateUrls()
    pc.collectPoems()
    for poem in pc.poems_list:
        print(poem.author)

test()
'''