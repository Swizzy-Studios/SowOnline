import requests
import sys
import html
import re

def wikiscrape (inurl):
    numberwords = ['first','second','third','fourth','fifth','sixth','seventh','eighth','nineth','tenth',
        'eleventh','twelfth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth',
        'twentieth','thirtieth','fourtieth','fiftieth','sixtieth','seventieth','eightieth','ninetieth','hundredth','thousandth', 
        'one','two','three','four','five','six','seven','eight','nine','ten',
        'twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety',
        'hundred','thousand','million','billion','trillion','millionth','billionth','trillionth']
    wordnumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','30th','40th','50th','60th','70th','80th','90th','00th','000th','1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','00','000','000000','000000000','000000000000','000000th','000000000th','000000000000th']
    titleurl = ''
       
    try:
        page = requests.get(inurl)
    except:
        print("Error fetching article")
        exit(0)
    seeds =[]
    contentstr = []
    for line in page.iter_lines():
        contentstr.append(line.decode("utf-8"))
    titleurl = ''
    for line in contentstr:
        br = 0
        templine = line
        if '/wiki/Special:WhatLinksHere/' in line:
            hrefc = templine.index('href="') + 6
            i = 0
            href = ''
            presentation = ''
            c = ''
            while c != '"':
                href += c
                #print(title)
                c = line[hrefc + i]
                i+=1
            titleurl = href.replace('/wiki/Special:WhatLinksHere/','')
            
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
                # strsplit = html.unescape(title).split(' ')
                # spc = ' '
                
                # strsplitc = 0
                # for word in strsplit:
                    # nconvert = word.split('-')
                    # jnum = []
                    # numberword = 1
                    # for n in nconvert:
                        # if n.lower() in numberwords:
                            # i = numberwords.index(n.lower())
                            # jnum.append(wordnumbers[i])
                            # #print(nconvert)
                        # else:
                            # numberword = 0
                    # if numberword == 0:
                        # continue
                    # x = len(jnum)

                    # nobj = []
                    # if x > 1:
                        # c = 0
                        # nobji = 0
                        # for nw in jnum:
                            
                            # dc = 0
                            # for d in nw:
                                # try:
                                    # nobj[nobji + dc] = d
                                # except:
                                    # nobj.append(d)
                                # dc+=1
                         
                            # if c < (x -1):
                                # nl = len(nw)
                                
                                # nlx = len(jnum[c+1].replace('th','').replace('nd','').replace('rd',''))
                                
                                # if nl >= nlx:
                                    # nobji += (nl - nlx)
                                # else:
                                    # nobji += nl
                            # c+=1
                    # else:
                        # for d in jnum:
                            # nobj.append(d)
                                            
                                
                    # s = ''
                    # s = s.join(nobj)
                    # #print(s)
                    # strsplit[strsplitc] = s
                    # strsplitc+=1
                # seeds.append(spc.join(strsplit))
                


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
    
    
    linkshere = "https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/" + titleurl + "&namespace=0&limit=500"
    
    try:
        linksherer = requests.get(linkshere)
    except:
        print("Error fetching link pages for relevancy check")
        exit(0)
    linksherestr = []
    pc = pcn = 0
    for line in linksherer.iter_lines():
        linksherestr.append(line.decode("utf-8"))
    print(linkshere)
    for line in linksherestr:
        #print(line)
        if 'mw-pager-navigation-bar' in line:
            lineindex = pc
            break
        pc += 1
        
    lineindex +=1
    linksherearr = []
    offset = linksherestr[lineindex + pcn]
    while 'mw-pager-navigation-bar' not in offset: 
        titlec = offset.index('title="') + 7
        i = 0
        title = ''
        presentation = ''
        c = ''
        while c != '"':
            title += c
            #print(title)
            c = offset[titlec + i]
            i+=1
        linksherearr.append(title)
        pcn += 1
        offset = linksherestr[lineindex + pcn]
    print(linksherearr)
    return seeds


wikisearch = input("Please enter a search subject:")
wikisearch = wikisearch.replace(' ','+')
searchsafe = 'https://en.wikipedia.org/w/index.php?fulltext=Search&search='+ wikisearch + '&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1'
print('Search Query: ' + searchsafe)
searchreq = requests.get(searchsafe)
wfilter = ['list of','You are encouraged to create an account and log in','commons:Category','ctx_ver','template','wikipedia','user menu','Main menu','edit section','Visit the main page','Go to a page with this exact name if it exists','Download this page as a PDF file','More options','category','WebM','portal:','accesskey=','data-mwprovider=','data-shorttitle=','class=','Special:']
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
#for seed in seedsilo:
#    print(seed)
# i = 0
#print(contentstr)
#excelauto001@gmail.com