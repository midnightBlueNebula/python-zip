def zipper(*its):
	i = 0
	status = True
	
	while status:
		els = list()
		
		for it in its:
			if type(it) == type({}):
				it = list(it.keys())
				
			if i >= len(it):
				status = False
				break
        
			els.append(it[i])

		if status:
			yield(tuple(els))
			i += 1
