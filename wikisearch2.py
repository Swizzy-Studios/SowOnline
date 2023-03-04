import requests
import sys
import html
import re

def wikiscrape (inurl):
    numberwords = ['first','second','third','fourth','fifth','sixth','seventh','eighth','nineth','tenth','eleventh','twelfth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth','twentieth','thertieth','fourtieth','fiftieth','sixtieth','seventieth','eightieth','ninetieth','hundredth','thousandth','one','two','three','four','five','six','seven','eight','nine','ten']
    wordnumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',
    try:
        page = requests.get(inurl)
    except:
        print("Error fetching article")
        exit(0)
    seeds =[]
    contentstr = []
    for line in page.iter_lines():
        contentstr.append(line.decode("utf-8"))
    for line in contentstr:
        br = 0
        templine = line
        while 'href' in templine and "/wiki/" in templine and 'title="' in templine:
            #if 'href' and "/wiki/" and 'title="' in templine:
            titlec = templine.index('title="') + 7
            i = 0
            title = ''
            presentation = ''
            c = ''
            while c != '"':
                title += c
                #print(title)
                c = templine[titlec + i]
                i+=1
            c = ''
            i+=1
            while c!= '<':
                presentation += c
                #print(templine)
                #print(presentation)
                c = templine[titlec + i]
                i+=1
                
            wfcheck = 0
            for wf in wfilter:
                if wf.lower() in title.lower():
                    wfcheck = 1
            if wfcheck == 0:        
                seeds.append(html.unescape(title))
                
            if title != presentation:    
                for wf in wfilter:
                    if wf.lower() in presentation.lower():
                        wfcheck = 1
                if wfcheck == 0:
                    #print(presentation)
                    seeds.append(html.unescape(presentation))
            if titlec + i < len(templine):
                templine = templine[titlec + i:]
            else:
                continue
        
        rcoll = re.findall(r' \d+ ',line)
        for word in rcoll:
            seeds.append(word.replace(' ',''))
    return seeds


wikisearch = input("Please enter a search subject:")
wikisearch = wikisearch.replace(' ','+')
searchsafe = 'https://en.wikipedia.org/w/index.php?fulltext=Search&search='+ wikisearch + '&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1'
print('Search Query: ' + searchsafe)
searchreq = requests.get(searchsafe)
wfilter = ['prollynotgonnabeinhere','list of','You are encouraged to create an account and log in','commons:Category','ctx_ver','template','wikipedia','user menu','Main menu','edit section','Visit the main page','Go to a page with this exact name if it exists','Download this page as a PDF file','More options','category','WebM','portal:','accesskey=','data-mwprovider=','data-shorttitle=','class=','Special:']
contentstr = []

    
for line in searchreq.iter_lines():
    contentstr.append(line.decode("utf-8"))
article=[]
srcounter = linecounter = 0
for line in contentstr:
    if srcounter >= 10:
        break
    #if 'mw-search-result-heading' in line:
    if 'mw-search-result mw-search-result-ns-0' in line:
        hrefi = line.index('href') + 6
        linkstr = 'https://en.wikipedia.org'
        cc = 0

        while (line[hrefi+cc] != '"'):
            linkstr = linkstr + line[hrefi+cc]
            cc+=1
        templine = line
        while '/wiki/' not in linkstr or 'Wikipedia:Article_wizard' in linkstr:
            templine = templine[line.index(linkstr.replace('https://en.wikipedia.org',''))+len(linkstr.replace('https://en.wikipedia.org','')):]
            hrefi = templine.index('href') + 6
            linkstr = 'https://en.wikipedia.org'
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
seedsilo = []
for wiki in wikitosearch:
    collection = wikiscrape(article[int(wiki)])
    for word in collection:
        seedsilo.append(word)
seedsilo = list(set(seedsilo))
seedsilo = sorted(seedsilo)
for seed in seedsilo:
    print(seed)
# i = 0
#print(contentstr)
#excelauto001@gmail.com