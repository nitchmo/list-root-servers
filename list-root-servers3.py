import urllib.request
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
res = urllib.request.urlopen('https://www.internic.net/domain/named.root')

for rec in res:
    cols = rec.decode().split()

    if cols[0] == ';':
        continue

    if cols[0] == '.':
        continue

    if cols[2] != 'A':
        continue

    print(cols[3])
