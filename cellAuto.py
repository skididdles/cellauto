import math

def cellular_automaton(seed, rule, gen):
	runs = []
	for i in range(0,gen):
		seed = onegen(seed,rule)
		print seed
		runs.append(seed)
	return runs


def onegen(seed, rule):
	c = ""
	for e in sectiongrab(seed):	

		if e == '...':
			if (rule & 1):
				c += 'x'
			else:
				c += '.'

		if e == '..x':
			if rule & 2:
				c += 'x'
			else:
				c += '.'
        
		if e == '.x.':
			if rule & 4:
				c += 'x'
			else:
				c += '.'
    
		if e == '.xx':
			if rule & 8:
				c += 'x'
			else:
				c += '.'
        
		if e == 'x..':
			if rule & 16: 
				c += 'x'
			else:
				c += '.' 

		if e == 'x.x':
			if rule & 32:
				c += 'x'
			else:
				c += '.'
    
		if e == 'xx.':
			if rule & 64:
				c += 'x'
			else:
				c += '.'
    
		if e == 'xxx':
			if rule & 128:
				c += 'x'
			else:
				c += '.'
	return c

def sectiongrab(s):
	out = []
	chunk = ""
	for e in range(0,len(s)):
		chunk = ""
		for i in range(e,e+3):
			#print i
			if e + 3 > len(s):
				chunk += s[i - len(s)]
				#print chunk
			else:
				#print chunk
				#print s[i]
				chunk += s[i]
		out.append(chunk)
	return out	

def repfinder(r):
	reps = {}
	for i in range(0,len(r)):
		for j in range(0,len(r)):
			if i == j:
				continue
			if r[i] == r[j]:
				try:
					if j in reps[r[i]]:
						continue
					reps[r[i]].append(j)
				except:
					reps[r[i]] = [j]
	return reps

def classify(reps):
	notconstpatt = []
	for e in reps:
		temp = reps[e][1]
		tdiff = reps[e][1] - reps[e][0]
		diff = 0
		for ei in range(2,len(reps[e])):
			diff = temp - reps[e][ei]
			if math.fabs(tdiff) == math.fabs(diff):
				pass
			else:
				notconstpatt.append(e)
			tdiff = diff
			temp = reps[e][ei]
	return notconstpatt

def lotofrules(j):
	smallest= 100
	thing = ''
	for i in range(0,j):
		some = repfinder(cellular_automaton('x.xxx.x.',i,100))
		
		#print "%s repitions" % len(some)
		for e in some:
			some[e].sort()
		for e in some:
			if len(some[e]) < smallest:
				smallest = len(some[e])
				thing = i
	#print some	
	#return
	return smallest, thing
	#	it= []
	#	it = classify(some)
	#	if it:
	#		return it
		
#print '\n\n' ,lotofrules(256)

some = repfinder(cellular_automaton('xxx.....',9,100))
print "%s repitions" % len(some)
for e in some:
	some[e].sort()
print some
#print classify(some)

