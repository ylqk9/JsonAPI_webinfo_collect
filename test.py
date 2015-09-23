from html.parser import HTMLParser
import urllib.request

class MyParser(HTMLParser):
    """
    The class is used to find the text body and title
    """
    # content storage
    content = []
    contenttitle = ""
    contentattrib = []
    contenttag = ""
    # start capture after the title is seen
    titleseen = False
    # redefine the member function of HTMLParser. The function is called by feed
    def handle_starttag(self, tag, attrs):
        self.contenttag = tag
        self.contentattrib = attrs
    def  handle_data(self, data):
        # drop everything before title
        if(not self.titleseen):
            if(self.lasttag.lower() == "title"):
                self.titleseen = True
                self.contenttitle = data
                return
        # drop short lines since they are unlikely be a paragraph
        if(len(data) < 20):
            return
        # drop these
        if(self.lasttag.lower() in ["script", "span", "time"]):
            return
        if(self.titleseen):
            # drop the lines with h1, h2, h3 (could be titles)
            if(self.lasttag.lower() not in ["h1", "h2", "h3"]):
                self.content.append(data)
                print(data)
        return

website = urllib.request.Request("http://www.foxnews.com/politics/2015/09/23/iran-deal-open-for-debate-tehran-presses-new-ayatollah-demand", headers={'User-Agent' : "Magic Browser"})
sitecontent = urllib.request.urlopen(website).read().decode("utf-8")

parser = MyParser()
parser.feed(sitecontent)
d1 = parser.content
