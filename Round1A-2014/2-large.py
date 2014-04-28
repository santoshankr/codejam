import sys
f = open(sys.argv[1])
for t in range(1, int(f.readline())+1):
			
	memo = {}
	N = int(f.readline())
	G = {}
	for i in range(N-1):
		src, dst = map(int, f.readline().split())
		if src not in G:
			G[src] = []
		if dst not in G:
			G[dst] = []
		G[src].append(dst)
		G[dst].append(src)
		
	def get_max_tree(root, prev):
		global memo
	
		if (root, prev) in memo:
			return memo[(root, prev)]
		
		children = filter(lambda x: x!= prev, G[root])
		lc = len(children)
		if lc == 0 or lc == 1:
			memo[(root, prev)] = 1
			return 1
			
		elif lc == 2:
			answer = get_max_tree(children[0], root) + get_max_tree(children[1], root) + 1
			memo[(root, prev)] = answer
			return answer
			
		else:
			children_max_trees = sorted([get_max_tree(child, root) for child in children], reverse=True)
			answer = children_max_trees[0] + children_max_trees[1] + 1
			memo[(root, prev)] = answer
			return answer
		
		print 'Huh?'
		return 0
		
	answer = min([N - get_max_tree(root, -1) for root in range(1, N+1)])	
	print 'Case #%d: %d' % (t, answer)
