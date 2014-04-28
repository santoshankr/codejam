import sys

f = open(sys.argv[1])
for t in range(1, int(f.readline())+1):
	a = int(f.readline())
	print 'Case #%d: %d' % (t, a)
