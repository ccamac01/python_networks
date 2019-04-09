import sys, urllib.request

try: 
	comp_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply the COMP course number as a first arg')
    sys.exit(2)

template = 'http://www.cs.tufts.edu/comp/{}/index.html'
url = template.format(comp_number)
comp_raw = urllib.request.urlopen(url).read()
comp = comp_raw.decode()
print(comp)
