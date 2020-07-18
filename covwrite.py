import os

print(os.getcwd())
os.chdir('C:/Users/prata/Desktop/')
print('after change: ', os.getcwd())

with open('cov19.txt','r') as cov19:
	cov19rd = cov19.readline()
	h1 = cov19rd.split('\t')
	d1 = {'Population\n':'Population', 'dummy': 'dummy1'}
	l2 = [d1.get(i, i) for i in h1]
	l3 = '\t\t | \t\t'.join(l2) + '\n'
	print(l3)
	break
	with open('cov19w.txt', 'w') as cov19w:
		hline = '=' * 550 + '\n'
		rline = '-' * 550 + '\n'
		cov19w.write(hline)
		cov19w.write(l3)
		cov19w.write(hline)

		for ln in cov19.readlines():
			v1 = ln.split('\t')
			v2 = '\t\t | \t\t'.join(v1)
			cov19w.write(v2)
			cov19w.write(rline)
