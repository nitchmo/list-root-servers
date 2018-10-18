import urllib2

res = urllib2.urlopen('https://www.internic.net/domain/named.root')

rec = res.readline()
while rec:
    cols = rec.split()
    rec = res.readline()

    if cols[0][0] == ';':
        continue

    if cols[0][0] == '.':
        continue

    if cols[2] != 'A':
        continue

    print( cols[3] )
