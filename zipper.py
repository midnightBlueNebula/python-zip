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

			
			
			
""" Examples 

>>> list(zipper([1,2,3],{"a":11,"b":22,"c":33},[100,200,300]))
[(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]
>>> list(zipper([1,2],{"a":11,"b":22,"c":33},[100,200,300]))
[(1, 'a', 100), (2, 'b', 200)]
>>> list(zipper([1,2,3],{"a":11,"b":22,"c":33},[100,200]))
[(1, 'a', 100), (2, 'b', 200)]
>>> list(zipper([1,2,3],{"a":11,"b":22},[100,200,300]))
[(1, 'a', 100), (2, 'b', 200)]

"""
