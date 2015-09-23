import requests

keys = ["iowa", "republican", "visit"]
sitesource = "https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q="
for keyword in keys:
    sitesource += keyword + "%20"
print("download content from:\n", sitesource, "\n")
resp = requests.get(sitesource, headers={'User-Agent' : "Magic Browser"})
if(not resp.ok):
    print("download failure")
    SystemExit(1)
content = resp.json()
resp.close()
entry = content.get('responseData').get('results')
if(len(entry) == 0):
    print("downloaded successfully. But there is no matched result")
    SystemExit(1)

# get title
alltitle = []
allurl = []
for item in entry:
    alltitle.append(item.get('titleNoFormatting'))
    allurl.append(item.get('unescapedUrl'))

ReplaceName = ("Trump", "Picachu")

f = open('result.txt', 'w')
for title in alltitle:
    title = title.replace(ReplaceName[0], ReplaceName[1])
    f.write(title)
    f.write("\n")
f.close()
