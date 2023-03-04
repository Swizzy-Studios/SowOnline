numberwords = ['first','second','third','fourth','fifth','sixth','seventh','eighth','nineth','tenth',
        'eleventh','twelfth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth',
        'twentieth','thirtieth','fourtieth','fiftieth','sixtieth','seventieth','eightieth','ninetieth','hundredth','thousandth', 
        'one','two','three','four','five','six','seven','eight','nine','ten',
        'twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety',
        'hundred','thousand','million','billion','trillion','millionth','billionth','trillionth']
wordnumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','30th','40th','50th','60th','70th','80th','90th','00th','000th','1','2','3','4','5','6','7','8','9','10','20','30','40','50','60','70','80','90','00','000','000000','000000000','000000000000','000000th','000000000th','000000000000th']
word = 'one-trillion-fifty-two'
word = word.split('-')
jnum = []
for n in word:
	if n in numberwords:
		i = numberwords.index(n)
		jnum.append(wordnumbers[i])
        
x = len(jnum)

nobj = []
if x > 1:
    c = 0
    nobji = 0
    for nw in jnum:
        
        dc = 0
        for d in nw:
            try:
                nobj[nobji + dc] = d
            except:
                nobj.append(d)
            dc+=1
     
        if c < (x -1):
            nl = len(nw)
            
            nlx = len(jnum[c+1].replace('th','').replace('nd','').replace('rd',''))
            
            if nl >= nlx:
                nobji += (nl - nlx)
            else:
                nobji += nl
        c+=1
else:
    for d in jnum:
        nobj.append(d)
                        
            
s = ''
s = s.join(nobj)
print(s)
