import requests
import sys
import getopt
import re
import html
import os
args = sys.argv[1:]
options = "s:hbtalvL:cC:f:e:d:o:A:P:i:d:"
loptions = ["search=","help","bypass","disable-transm","all","all-title","dense","lucky=","caps","caps-limit","filter=","extra=","depth=","output=","append=","preappend=","integers=","dates="]
h = 0
global bypass
global transm
global alltitle
global atoz
global density
global extra
global caps
bypass = transm = alltitle = atoz = density = extra = caps = append = preappend = integers = dates = lucky = 0
appendfilter = preappendfilter = integerspath = datespath = ''
global depth
depth = 3
global path 
search = "wikipedia"
path = "wordlist_sow_" + search + ".txt"
global splitfilter
splitfilter = ["the","and","a","or","do","of","list","it"]
global wfilter
wfilter = ['category:','w:c:','version history','wikia help','template:','wiki:','special:','wikia:','blog:','list','wikipedia','template','dark theme','light theme','table of contents']
afilter = []
global carray
carray = ['-','_',':',' ',]
global capslimit 
capslimit = 0


def transmutemech(seed):

    wordarray = []
    wordarray.append(seed)
    for c in carray:
        temptt = seed.replace(c,'')
        wordarray.append(temptt)
        if density == 1:
            for ccc in carray:
                temptt2 = temptt.replace(ccc,c)
                wordarray.append(temptt2)
        for cc in carray:
            tempttR = seed.replace(c,cc)
            wordarray.append(tempttR)
            if density == 1:
                for c4 in carray:
                    temptt3 = tempttR.replace(c4,cc)
                    wordarray.append(temptt3)
                temptt4 = tempttR
                for c5 in carray:
                    temptt4 = temptt4.replace(c5,'')
                wordarray.append(temptt4)
        temptt5 = tempttR
        for c6 in carray:
            temptt5 = temptt5.replace(c6,'')
            wordarray.append(temptt5)
        if density == 1:
            #Half-Life 2: Episode One
            temptt6 = seed
            temptt6 = temptt6.replace(c,'')
            temptt9 = temptt6
            for c9 in carray:
                for c10 in carray:
                    temptt8 = temptt6.replace(c10,c9)
                    temptt9 = temptt9.replace(c10,c9)
                    wordarray.append(temptt8)
                wordarray.append(temptt9)
            for c7 in carray:
                temptt6 = temptt6.replace(c7,c)
            wordarray.append(temptt6)
            temptt7 = seed
            for c8 in carray:
                temptt7 = temptt7.replace(c8,c)
            wordarray.append(temptt7)
        temptt10 = seed
        for c11 in carray:
            temptt10 = temptt10.replace(c11,c)
        wordarray.append(temptt10)
    return wordarray  
            
def transmute(seed):
    seed = html.unescape(seed)
    seed = seed.replace(' Wiki','').replace('Wiki ','').replace('Wiki','')  
    wordarray = []
    if transm == 1:
        return seed
    else:
        collection = transmutemech(seed)
        for word in collection:
            wordarray.append(word)
            
        rparr = re.sub(r'\s\(.*?\)','',seed)
        rparr = re.sub(r'\(.*?\)[ \t]','',rparr)
        rparr = re.sub(r'\s\(.*?\)[ \t]','',rparr)
        collection = transmutemech(rparr)
        for word in collection:
            wordarray.append(word)
            
        rcoll = re.findall(r'\(.*?\)',seed)
        if len(rcoll) > 0:
            for rword in rcoll:
                rword = rword.replace('(','').replace(')','')
                collection = transmutemech(rword)
                for word in collection:
                    wordarray.append(word)
                rcollA = rword.split(' ')
                if len(rcollA) > 1:
                    for sword in rcollA:
                        if sword.lower() not in splitfilter:
                            collection = transmutemech(sword)
                            for word in collection:
                                wordarray.append(word)
                rcollA = rword.split('-')
                if len(rcollA) > 1:
                    for sword in rcollA:
                        if sword.lower() not in splitfilter:
                            collection = transmutemech(sword)
                            for word in collection:
                                wordarray.append(word)
                rcollA = rword.split('_')
                if len(rcollA) > 1:
                    for sword in rcollA:
                        if sword.lower() not in splitfilter:
                            collection = transmutemech(sword)
                            for word in collection:
                                wordarray.append(word)
                rcollA = rword.split(':')
                if len(rcollA) > 1:
                    for sword in rcollA:
                        if sword.lower() not in splitfilter:
                            collection = transmutemech(sword)
                            for word in collection:
                                wordarray.append(word)
                rcollA = rword.split('/')
                if len(rcollA) > 1:
                    for sword in rcollA:
                        if sword.lower() not in splitfilter:
                            collection = transmutemech(sword)
                            for word in collection:
                                wordarray.append(word)
                    
        splitwordsSP = rparr.split(' ')
        if len(splitwordsSP) > 1:
            for sword in splitwordsSP:
                if sword.lower() not in splitfilter:
                    collection = transmutemech(sword)
                    for word in collection:
                        wordarray.append(word)
        splitwordsD = rparr.split('-')
        if len(splitwordsD) > 1:
            for sword in splitwordsD:
                if sword.lower() not in splitfilter:
                    collection = transmutemech(sword)
                    for word in collection:
                        wordarray.append(word)
        splitwordsUS = rparr.split('_')
        if len(splitwordsUS) > 1:
            for sword in splitwordsUS:
                if sword.lower() not in splitfilter:
                    collection = transmutemech(sword)
                    for word in collection:
                        wordarray.append(word)
        splitwordsC = rparr.split(':')
        if len(splitwordsC) > 1:
            for sword in splitwordsC:
                if sword.lower() not in splitfilter:
                    collection = transmutemech(sword)
                    for word in collection:
                        wordarray.append(word)
        splitwordsFS = rparr.split('/')
        if len(splitwordsFS) > 1:
            for sword in splitwordsFS:
                if sword.lower() not in splitfilter:
                    collection = transmutemech(sword)
                    for word in collection:
                        wordarray.append(word)
            
        if density == 1:    
            rown = seed.replace("'s",'s')
            collection = transmutemech(rown)
            for word in collection:
                wordarray.append(word)
                
            rparrrown = rparr.replace("'s",'s')
            collection = transmutemech(rparrrown)
            for word in collection:
                wordarray.append(word)
            
            rquo = seed.replace("'",'')
            collection = transmutemech(rquo)
            for word in collection:
                wordarray.append(word)
            
            rparrrquo = rparr.replace("'",'')
            collection = transmutemech(rparrrquo)
            for word in collection:
                wordarray.append(word)
                
            rquospace = seed.replace("'",' ')
            collection = transmutemech(rquospace)
            for word in collection:
                wordarray.append(word)
            
            rparrrquospace = rparr.replace("'",' ')
            collection = transmutemech(rparrrquospace)
            for word in collection:
                wordarray.append(word)
    wordarray = list(set(wordarray))
    return(wordarray)

def transmutecaps(inseed):
    wordarray = []
    upperarr = []
    seed = html.unescape(inseed)
    upperarr = []
    i = 0
    for c in seed:
        if c.isupper():
            upperarr.append(i)
        i+=1
    if capslimit == 0 and len(upperarr) > 0:
        collection = transmutecapsmech(seed,upperarr)
        for word in collection:
            wordarray.append(word)
    elif capslimit > 1 and len(upperarr) > 0 and len(upperarr) <= capslimit:
        collection = transmutecapsmech(seed,upperarr)
        for word in collection:
            wordarray.append(word)
    return(wordarray)
    
        
def transmutecapsmech(inseed,inarr):
    wordarray = []
    upperarr = inarr
    btotal = len(upperarr) * '1'
    dec = 0
    for d in btotal:
        dec = dec*2 + int(d)
    dec+=1
    for i in range(dec):
        ta = list(inseed)
        binary = bin(i)
        sbinary = '0' * (len(upperarr)- (len(binary.replace('0b','')))) + binary.replace('0b','')

        bc = 0
        for b in sbinary:
            if b == '1':
                ta[upperarr[bc]] = ta[upperarr[bc]].lower()                 
            bc+=1
        collection = transmute("".join(ta))
        for word in collection:
            wordarray.append(word)
    return(wordarray)
        
def transmuterouter(inseed):
    wordarray = []
    if caps == 1:
        collection = transmutecaps(inseed)
    else:
        collection = transmute(inseed)
    for word in collection:
        wordarray.append(word)
    return wordarray
    
def writefile(inrparr):
    with open(path,"a", encoding="utf-8") as f:
        if type(inrparr) != list:
            f.write(inrparr + '\n')
        else:
            for line in inrparr:
                f.write(line  + '\n')
    f.close()
def fandomscrapealltitle(inurl):
    try:
        allarticles = requests.get(inurl + '/wiki/Special:AllPages')
        allarticles = requests.get(allarticles.url)
    except:
        sys.exit("Error fetching URL: " + inurl + '/wiki/Special:AllPages')
    contentstr = []
    nextpage = ''
    seeds = []
    for line in allarticles.iter_lines():
        contentstr.append(line.decode("utf-8"))
    for line in contentstr:
        if 'href' and (inurl + '/wiki/') and 'title="' in line:
            titlec = line.index('title="') + 7
            i = 0
            title = ''
            c = ''
            while c != '"':
                title += c
                c = line[titlec + i]
                i+=1
            wfcheck = 0
            for wf in wfilter:
                if wf in title.lower():
                    wfcheck = 1
            if wfcheck == 0:  
                collection = transmuterouter(title)
                for word in collection:
                    seeds.append(word)
                    
                   
            if 'Next page' in line:
                    npindex = line.index('href=') + 6
                    i = 0
                    c = ''
                    while c != '"':
                        nextpage += c
                        c = line[npindex + i]
                        i+=1
    
    while nextpage != '':
        print(nextpage)
        try:
            allarticles = requests.get(inurl + nextpage)
            allarticles = requests.get(allarticles.url)
        except:
            sys.exit("Error fetching URL: " + inurl + nextpage)
        contentstr = []
        nextpage = ""
        for line in allarticles.iter_lines():
            contentstr.append(line.decode("utf-8"))
        for line in contentstr:
            if 'href' and '/wiki/' and 'title="' in line:
                titlec = line.index('title="') + 7
                i = 0
                title = ''
                c = ''
                while c != '"':
                    title += c
                    c = line[titlec + i]
                    i+=1
                wfcheck = 0
                for wf in wfilter:
                    if wf in title.lower():
                        wfcheck = 1
                if wfcheck == 0:  
                    collection = transmuterouter(title)
                    for word in collection:
                        seeds.append(word)
                        
                       
                if 'Next page' in line:
                    prevnext = line.split('|')
                    if len(prevnext) == 2:
                        nextline = prevnext[1]
                        npindex = nextline.index('href=') + 6
                        i = 0
                        c = ''
                        while c != '"':
                            nextpage += c
                            c = nextline[npindex + i]
                            i+=1
    return seeds
       
def fandomscrape(inurl,indepth):
    #Special:AllPages
    print(wfilter)
    links = []
    seeds = []
    try:
        homepage = requests.get(inurl)
        nurl = homepage.url
        homepage = requests.get(nurl)
    except:
        sys.exit("Error fetching URL: " + inurl)
    contentstr = []
    for line in homepage.iter_lines():
        contentstr.append(line.decode("utf-8"))
    for line in contentstr:
        br = 0
        if 'href' and (nurl + '/wiki/') and 'title="' in line:
            titlec = line.index('title="') + 7
            i = 0
            title = ''
            c = ''
            while c != '"':
                title += c
                c = line[titlec + i]
                i+=1
            wfcheck = 0
            for wf in wfilter:
                if wf in title.lower():
                    wfcheck = 1
            if wfcheck == 0:        
                collection = transmuterouter(title)
                for word in collection:
                    seeds.append(word)
    return seeds
    

try:
    arguments, values = getopt.getopt(args, options, loptions)
    for carg, cval in arguments:
        if carg in ("-h", "--help"):
            h=1
            print("sowonline.py usage:")
            print("Create password rparr wordlist by searching various wikis for specified topic")
            print("sowonline will pull potential password candidates by scraping wiki's for relevant strings")
            print("Password candidates are taken from href values, categorical lists, and in-article content links")
            print("sowonline will follow the href links to other linked articles and check for relevancy by searching for the parent article (default) or the previously linked article (verbose)")
            print("sowonline.py <OPTIONS>")
            print("  -h, --help:               This menu")
            print("  -s, --search:             Search term, separated by commas")
            print("  -d, --depth <int>:        level of interlinked articles sowonline will search. Default=3, Relevance only check=0")
            print("  -b, --bypass:             Bypass relevancy check. sowonline will follow -d level only")
            print("  -t, --disable-transm:     Disable transmutation of password rparrs.")
            print("  -o, --output <path>:      Output wordlist to specific file")      
            print("  -a, --all:                Uses Fandom A-Z article navigation to pull all articles for subject. Will pull ALOT of content")
            print("  -l, --all-title:          Uses Fandom A-Z article navigation but will only pull the href value rather than follow all links")
            print("  -v, --dense:              Uses multiple iterations of transmutation. Adds exponentially more seeds")
            print("  -e, --extra <chars>:      Add extra characters to transmutation routine separated by comma. Default: '-','_',':',' '")
            print("  -f, --filter <words>:     Add additional words to filter out separated by comma")
            print("  -c, --caps:               Find all possible combination of capital letters for a given seed, replacing the positions where capital letters are found")
            print("  -C, --caps-limit <int>:   Used with -c, --caps. Limit the words provided to caps by max <int> number of total capital letters")
            print("  -A, --append <filter>:    Append words to words with a variety of filters. Filters are separated by commas and their values are indicated by '='")
            print("                            MLR=<int>: Max Length Right. Only append words that are equal to or less than the provided value")
            print("                            MLL=<int>: Max Length Left. Only append words to words that are equal to or less than provided value")
            print("                            MLT=<int>: Max Length Total. Only append words to words if the resulting number of characters is less than provided value")
            print("                            IO: Integer Only. Append words that contain only numbers")
            print("                            D: Dates. Append words that contain only numbers, and are 4-6 characters long")
            print("                            S=<@$&!>: Separating characters. Append word with a preappended list of provided characters. No separation of provided characters needed.")
            print("                            SCL=<int>: Special Character Limiter Left. Only Append to words that contain provided number of special characters or less")
            print("                            SCR=<int>: Special Character Limiter Right. Only Append words that contain provided number of special characters or less")
            print("                            AP=<path>: Append Path. Save appended result to a separate file. Helpful if you run into memory issues while processing a large amount of data")
            print("                            AP creates 2 temporary files, appenderTMP.txt and appendeeTMP.txt which are deleted at the end of sowonline's run")
            print("                            APW: Append Path Write. Keeps Append Path file, but adds results to end of the normal output's file")
            print("  -P, --preappend <filter>: Same filters as append, only (MLR and MLL) and (SCL and SCR) are switched when referencing the 'appender' and 'appendee'")
            print("  -i, --integers <path>:    Save words containing only numbers to a separate file")
            print("  -d, --dates <path>:       Save words containing only numbers between 4-6 characters to a separate file")
            print("  -L, --lucky <path>        Print seeds that are 7-12 characters, contain 1-3 upper case characters, 1-4 numbers, and contain 1-3 special characters")
            print("                            Enter path to save Lucky results to file or leave blank to print to terminal")
            
        elif carg in ("-b", "--bypass"):
            bypass = 1
        elif carg in ("-t", "--disable-transm"):
            transm = 1
        elif carg in ("-d", "--depth"):
            depth = int(cval)
        elif carg in ("-o", "--output"):
            path = cval
        elif carg in ("-s", "--search"):
            search = cval
            path = "wordlist_sow_" + search + ".txt"
        elif carg in ("-a", "--all"):
            atoz = 1
        elif carg in ("-l", "--all-title"):
            alltitle = 1
        elif carg in ("-v", "--dense"):
            density = 1
        elif carg in ("-e", "--extra"):
            extra = 1
            echars = cval.split(',')
            carray += echars
        elif carg in ("-f", "--filter"):
            afilter = cval.split(',')
            wfilter+=afilter
        elif carg in ("-c", "--caps"):
            caps = 1
        elif carg in ("-C", "--caps-limit"):
            capslimit = int(cval)
        elif carg in ("-A", "--append"):
            append = 1
            appendfilter = cval
        elif carg in ("-P", "--preappend"):
            preappend = 1
            preappendfilter = cval
        elif carg in ("-i", "--integers"):
            integers = 1
            integerspath = cval
        elif carg in ("-d", "--dates"):
            dates = 1
            datespath = cval
        elif carg in ("-L", "--lucky"):
            lucky = 1
            luckypath = cval
    
finally:
    if h==1:
        exit()


searchsafe = 'https://www.fandom.com/?s='
searchsafe = searchsafe + search.replace(' ','+')

print('Search Query: ' + searchsafe)
searchreq = requests.get(searchsafe)
contentstr = []

for line in searchreq.iter_lines():
    contentstr.append(line.decode("utf-8"))
i = 0
morecommunities = []
for line in contentstr:    
    
    if 'Top Wiki Community' in line:
        tsr = contentstr[i + 1]
        tsr = tsr.replace('<a href="','').replace('"','').strip()
    elif 'a class="other-communities-content-details"' in line:
        morecommunities.append(line.replace('<a class="other-communities-content-details" href="','').replace('"','').strip())
        #print(line.replace('<a class="other-communities-content-details" href="','').replace('"','').strip())
    i+=1
    
print('[0] Top Wiki: ' + tsr)
cc = 1
for c in morecommunities:
    print('[' + str(cc) + '] Additional Wikis: ' + c)
    cc+=1
fandomtosearch = input("Please select which Wikis you would like to harvest separated by commas: ")
fandomtosearch = fandomtosearch.split(',')
seedsilo = []
for f in fandomtosearch:
    if int(f) == 0:
        seeds = fandomscrape(tsr,0)
        for seed in seeds:
            seedsilo.append(seed)
        if alltitle == 1:
            seeds = fandomscrapealltitle(tsr)
            for seed in seeds:
                seedsilo.append(seed)
    else:
        seeds = fandomscrape(morecommunities[(int(f)-1)],0)
        for seed in seeds:
            seedsilo.append(seed)
        if alltitle == 1:
            seeds = fandomscrapealltitle(morecommunities[(int(f)-1)])
            for seed in seeds:
                seedsilo.append(seed)
#print(seedsilo)
seedsilo = list(set(seedsilo))
seedsilo = sorted(seedsilo)
ap = apw = 0
if (append ==1):
    seedsilo2 = []
    goodappendee = []
    goodappender = []
    afl = appendfilter.split(',')
    integersonly = MLL = MLR = MLT = SCL = SCR = separator = 0
    sepchar = []
    specchararr = "[@_!#$%^&*()<>?/|}{~:]-+= " 
    for fl in afl:
        if fl == 'IO':
            integersonly = 1
        elif fl == 'D':
            integersonly = 2
        elif 'MLL' in fl:
            MLLA = fl.split('=')
            MLL = int(MLLA[1])
        elif 'MLR' in fl:
            MLRA = fl.split('=')
            MLR = int(MLRA[1])
        elif 'MLT' in fl:
            MLLT = fl.split('=')
            MLT = int(MLLT[1])
        elif 'SCL' in fl:
            SCLA = fl.split('=')
            SCL = int(SCLA[1])
        elif 'SCR' in fl:
            SCRA = fl.split('=')
            SCR = int(SCRA[1])
        elif 'S' in fl:
            separator = 1
            SA = fl.split('=')
            for c in SA[1]:
                sepchar.append(c)
        elif 'AP' in fl:
            ap = 1
            APA = fl.split('=')
            print(APA[1])
            appendpath = APA[1]
        elif 'APW' in fl:
            apw = 1
            

    i = 0
    for appendee in seedsilo:
        notqualified = 0
        if MLL > 0:
            if len(appendee) > MLL:
                notqualified = 1
        if SCL > 0:
            speccharcounter = 0
            for c in appendee:
                if c in specchararr:
                    speccharrcounter  += 1
            if speccharcounter > SCL:
                notqualified = 1
        if notqualified == 0:
            goodappendee.append(i)
        i+=1
    if ap == 1:
        fp = open('appendeeTMP.txt',"w",encoding="utf-8")
        for r in goodappendee:
            fp.write(str(r) + '\n')
        fp.close()
        goodappendee = []
    i = 0
    for appender in seedsilo:
        notqualified = 0
        if integersonly > 0:
            integer = []
            for c in appender:
                if c.isnumeric():
                    integer.append(c)
                else:
                    notqualified = 1
                    break

            if notqualified == 0:
                
                if integersonly == 2:
                    if len(integer) > 6 or len(integer) < 4:
                        notqualified = 1

            
        if MLR > 0:
            if len(appender) > MLR:
                notqualified = 1
        if SCR > 0:
            speccharcounter = 0
            for c in appender:
                if c in specchararr:
                    speccharrcounter  += 1
            if speccharcounter > SCR:
                notqualified = 1
        if notqualified == 0:
            goodappender.append(i)
        i+=1
    
    if (ap == 1):
        fp = open('appenderTMP.txt',"w",encoding="utf-8")
        for r in goodappender:
            fp.write(str(r) + '\n')
        fp.close()
        goodappender = []
        ff = open(appendpath,"a",encoding="utf-8")
        fr = open('appenderTMP.txt',"r",encoding="utf-8")
        fe = open('appendeeTMP.txt',"r",encoding="utf-8")
        appendeecontent = fe.readlines()
        appendercontent = fr.readlines()
        for lineE in appendeecontent:
            for lineR in appendercontent:

                notqualified = 0
                if MLT > 0:
                    if separator == 1:
                        if len(seedsilo[int(lineE)]) + len(seedsilo[int(lineR)]) + 1 > MLT:
                            notqualified = 1
                    else:
                        if len(seedsilo[int(lineE)]) + len(seedsilo[int(lineR)]) > MLT:
                            notqualified = 1
                if notqualified == 0:
                    ff.write(seedsilo[int(lineE)] + seedsilo[int(lineR)] + '\n')
                    if separator == 1:
                        for s in sepchar:
                            ff.write(seedsilo[int(lineE)] + s + seedsilo[int(lineR)] + '\n')
        ff.close()
        fe.close()
        fr.close()
        appendeecontent = ''
        appendercontent = ''
        os.remove('appenderTMP.txt')
        os.remove('appendeeTMP.txt')
    else:                       
        for l in goodappendee:
            for r in goodappender:
                notqualified = 0
                if MLT > 0:
                    if separator == 1:
                        if len(seedsilo[l]) + len(seedsilo[r]) + 1 > MLT:
                            notqualified = 1
                    else:
                        if len(seedsilo[l]) + len(seedsilo[r]) > MLT:
                            notqualified = 1
                if notqualified == 0:
                    seedsilo2.append(seedsilo[l] + seedsilo[r])
                    if separator == 1:
                        for s in sepchar:
                            seedsilo2.append(seedsilo[l] + s + seedsilo[r])
                        
        seedsilo = seedsilo + seedsilo2
        seedsilo = list(set(seedsilo))
        seedsilo = sorted(seedsilo)
    
if (preappend ==1):
    seedsilo2 = []
    afl = appendfilter.split(',')
    integersonly = MLL = MLR = MLT = SCL = SCR = separator = 0
    sepchar = []
    specchararr = "[@_!#$%^&*()<>?/|}{~:]-+= " 
    for fl in afl:
        if fl == 'IO':
            integersonly = 1
        elif fl == 'D':
            integersonly = 2
        elif 'MLL' in fl:
            MLLA = fl.split('=')
            MLL = int(MLLA[1])
        elif 'MLR' in fl:
            MLRA = fl.split('=')
            MLR = int(MLRA[1])
        elif 'MLT' in fl:
            MLLT = fl.split('=')
            MLT = int(MLLT[1])
        elif 'SCL' in fl:
            SCLA = fl.split('=')
            SCL = int(SCLA[1])
        elif 'SCR' in fl:
            SCRA = fl.split('=')
            SCR = int(SCRA[1])
        elif 'S' in fl:
            separator = 1
            SA = fl.split('=')
            for c in SA[1]:
                sepchar.append(c)
    
    i = 0
    for appendee in seedsilo:
        notqualified = 0
        if MLR > 0:
            if len(appendee) > MLR:
                notqualified = 1
        if SCR > 0:
            speccharcounter = 0
            for c in appendee:
                if c in specchararr:
                    speccharrcounter  += 1
            if speccharcounter > SCR:
                notqualified = 1
        if notqualified == 0:
            goodappendee.append(i)
        i+=1
    i = 0
    for appender in seedsilo:
        notqualified = 0
        if integersonly > 0:
            integer = []
            for c in appender:
                if c.isnumeric():
                    integer.append(c)
                else:
                    notqualified = 1
                    break

            if notqualified == 0:
                
                if integersonly == 2:
                    if len(integer) > 6 or len(integer) < 4:
                        notqualified = 1

            
        if MLL > 0:
            if len(appender) > MLL:
                notqualified = 1
        if MLT > 0:
            if separator == 1:
                if len(appendee) + len(appender) + 1 > MLT:
                    notqualified = 1
            else:
                if len(appendee) + len(appender) > MLT:
                    notqualified = 1
        if SCL > 0:
            speccharcounter = 0
            for c in appender:
                if c in specchararr:
                    speccharrcounter  += 1
            if speccharcounter > SCL:
                notqualified = 1
        if notqualified == 0:
            goodappender.append(i)
        i+=1
        
    for r in goodappendee:
        for l in goodappender:
            if MLT > 0:
                if separator == 1:
                    if len(seedsilo[l]) + len(seedsilo[r]) + 1 > MLT:
                        notqualified = 1
                else:
                    if len(seedsilo[l]) + len(seedsilo[r]) > MLT:
                        notqualified = 1
            if notqualified == 0:
                seedsilo2.append(seedsilo[l] + seedsilo[r])
                if separator == 1:
                    for s in sepchar:
                        seedsilo2.append(seedsilo[l] + s + seedsilo[r])
                    
    seedsilo = seedsilo + seedsilo2
    seedsilo = list(set(seedsilo))
    seedsilo = sorted(seedsilo)
    
writefile(seedsilo)
if ap == 1 and apw == 1:
    appendarray = []
    fa = open(appendpath,"r",ecoding="utf-8")
    for line in fa.readlines():
        appendarray.append(line)
    writefile(appendarray)
    fa.close()
    
if (lucky == 1):
    if (luckypath != ''):
        fl = open(luckypath,"a", encoding="utf-8")
    else:
        print("Possible password candidates:")
    specchararr = "[@_!#$%^&*()<>?/|}{~:]-+= "
    for seed in seedsilo:
        specialchars = 0
        numbers = 0
        uppercase = 0
        if len(seed) >= 7 and len(seed) <=10:
            for c in seed:
                if c.isnumeric():
                    numbers+=1
                elif c.isupper():
                    uppercase+=1
                elif c in specchararr:
                    specialchars+=1
            if numbers > 0 and numbers <=4 and uppercase > 0 and uppercase <=3 and specialchars > 0 and specialchars <= 3:
                if (luckypath == ''):  
                    print(seed)
                else:
                    fl.write(seed + '\n')
    if ap == 1:
        with open(appendpath,"r",encoding="utf-8") as fa:
            for seed in fa:
                specialchars = 0
                numbers = 0
                uppercase = 0
                if len(seed) >= 7 and len(seed) <=12:
                    for c in seed:
                        if c.isnumeric():
                            numbers+=1
                        elif c.isupper():
                            uppercase+=1
                        elif c in specchararr:
                            specialchars+=1
                    if numbers > 0 and numbers <=4 and uppercase > 0 and uppercase <=3 and specialchars > 0 and specialchars <= 3:
                        if (luckypath == ''):  
                            print(seed)
                        else:
                            fl.write(seed + '\n')
        fa.close()
    if (luckypath != ''):
        fl.close()

