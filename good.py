



from random import randint as ri

def gen_random():
	s = range(1, 1001)
	for i in range(1000):
		r = ri(i, 999)
		s[i], s[r] = s[r], s[i]
	return s
	
def gen_bad_random():
	s = range(1, 1001)
	for i in range(1000):
		r = ri(0, 999)
		s[i], s[r] = s[r], s[i]
	return s
	
def get_too_close(s):
	too_close = 0
	for index, i in enumerate(s):
		diff = i - index
		if diff <= 200 and diff >= 0:
			too_close += 1
	return too_close
		
	
from pylab import *	
t = [get_too_close(gen_random()) for i in range(500)]
u = [get_too_close(gen_bad_random()) for i in range(500)]
plot(t, 'r-', u, 'b-')
plt.show()


	
