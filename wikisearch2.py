import requests
wikisearch = input("Please enter a search subject:")
wikisearch = wikisearch.replace(' ','+')
searchsafe = 'https://en.wikipedia.org/w/index.php?fulltext=Search&search='+ wikisearch + '&title=Special%3ASearch&ns0=1'
print('Search Query: ' + searchsafe)
searchreq = requests.get(searchsafe)

contentstr = []


for line in searchreq.iter_lines():
    contentstr.append(line.decode("utf-8"))
article=[]
srcounter = linecounter = 0
for line in contentstr:
    if 'href="/wiki/' and 'mw-search-result' in line and '/w/index.php' not in line:
        if srcounter >= 10:
            break
        if 'mw-search-result-heading' in line:
            hrefi = line.index('href') + 6
            linkstr = 'https://en.wikipedia.com'
            cc = 0
   
            while (line[hrefi+cc] != '"'):
                linkstr = linkstr + line[hrefi+cc]
                cc+=1
            templine = line
            while '/wiki/' not in linkstr or 'Wikipedia:Article_wizard' in linkstr:
                templine = templine[line.index(linkstr.replace('https://en.wikipedia.com',''))+len(linkstr.replace('https://en.wikipedia.com','')):]
                hrefi = templine.index('href') + 6
                linkstr = 'https://en.wikipedia.com'
                cc = 0
                while (templine[hrefi+cc] != '"'):
                    linkstr = linkstr + templine[hrefi+cc]
                    cc+=1
            print('[' + str(srcounter) + '] Did you mean: ' + linkstr)
            article.append(linkstr)
            srcounter+=1
        linecounter+=1
wikitosearch = input("Please enter the article(s) you would like to search, separated by commas: ")
wikitosearch = wikitosearch.split(',')
for wiki in wikitosearch:
    wikiscrap(wiki)
    

# i = 0
#print(contentstr)
#excelauto001@gmail.com