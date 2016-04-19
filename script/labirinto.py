import random

def porta(i,t):
	"""data la porta e una tulpa con in numeri della stanza restituisce quelli della nuova stanza"""
	if i==1:
		return __controllo((t[1],t[0],t[3],t[2]))
	elif i==2:
		return __controllo((t[0],t[1]+2,t[2]+2,t[3]))
	elif i==3:
		return __controllo((t[2],t[3],t[0],t[1]))
	elif i==4:
		return __controllo((t[0]-2,t[1],t[2],t[3]-3))
	else:
		print('error')
		return t

def __controllo(t):
	return(t[0]%10,t[1]%10,t[2]%10,t[3]%10)


if __name__ == '__main__':
	partenza = (0,0,0,0)
	arrivo   = (9,9,9,9)
	#numero massimo di porte che può avere il percorso
	porteMax = 50
	#numero di tentativi di percorso che esegue il PC
	tentativiMax=100000
	path=[]
	steps=[]
	
	for n in range(1,tentativiMax):
		room=partenza
		
		doors=[]
		
		for i in range(1,porteMax):
			x= random.randrange(1,5)
			
			room=porta(x,room)
			
			doors.append(x)
	
			if (room==arrivo):
				path.append(doors)
				steps.append(i)
				break
	
	if len(path) == 0:
		print('hai perso')
	else:
		print('hai vinto')
		print('partenza', partenza)
		room = partenza
		for x in path[steps.index(min(steps))]:
			room = porta(x,room)
			print('scegliamo la porta',x,'ed entrimao nella stanza',room)
		print('a destinazione')