def takeDiff(num):
	if num=="1":
		return 5
	elif num=="2":
		return 7
	elif num=="3":
		return 9
	elif num=="4":
		return 10
	elif num=="5":
		return 15
	elif num=="10000":
		return 3
	else:
		print("Thanks for not playing. Lil' baby")
		return exit()
	
	
def makeMtrx(num): #Hacer 1/3 del total de cuadros, Minas
    map=[]
    for i in range(num):
        map.append([])
        for j in range(num):
            map[i].append(0)
    return map
    
def showMap(map):
    for r in map:
        print(r)
    return ""
