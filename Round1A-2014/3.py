import sys
f = open(sys.argv[1])
for t in range(1, int(f.readline())+1):
	N = int(f.readline())
	s = map(int, f.readline().split())
	too_close = len(filter(lambda x: x <= 200 and x >= 0, [i-index for index, i in enumerate(s)]))
	print 'Case #%d: %s' % (t, 'BAD' if too_close >= 200 else 'GOOD')
