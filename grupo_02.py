class Nodo():	
	nodos = []
	l_alcanzables = []

	contador = 0
	def __init__(self):
		Nodo.contador +=1
		self.nombre = str(Nodo.contador)
		self.aristas = []
		self.label = self.nombre
		self.nodos.append(self)
			
	def alcanzables(simbolo):
		for arist in self.aristas:
			if (simbolo == arist.simbolo):
				l_alcanzables.append(arist.origen)
		return l_alcanzables

class Arista():
	def __init__(self,simbolo,origen,destino):
		self.simbolo = simbolo
		self.origen = origen
		self.destino = destino	
		self.origen.aristas.append(self)

class Thompson():
	def __init__(self,simbolo):
		self.nodo_inicial = Nodo()
		self.nodo_aceptacion = Nodo()	
		Arista (simbolo, self.nodo_inicial,self.nodo_aceptacion)
		self.nodos_aceptacion.append(self.nodo_aceptacion)

	def concatena(self,otro_thompson):
		Arista(None,self.nodo_aceptacion,otro_thompson.nodo_inicial)
		self.nodo_aceptacion = otro_thompson.nodo_aceptacion
		self.nodos_aceptacion.remove(self.nodo_aceptacion)
		self.nodos_aceptacion.append(self.otro_thompson.nodo_aceptacion)
		
	def o(self,otro_thompson):
		Nodo_O_Inicial = Nodo()
		Nodo_O_Cierre = Nodo()		
		Arista(None,Nodo_O_Inicial,self.nodo_inicial) #arista que conecta el nuevo nodo con el nodo inicial del thompson que tengo
		Arista(None,Nodo_O_Inicial,otro_thompson.nodo_inicial) #arista que conecta el nuevo nodo con el nodo inicial del thompson que llega como parametro
		Arista(None,self.nodo_aceptacion,Nodo_O_Cierre) 
		Arista(None,otro_thompson.nodo_aceptacion,Nodo_O_Cierre)
		self.nodo_inicial = Nodo_O_Inicial
		self.nodo_aceptacion = Nodo_O_Cierre
		self.nodos_aceptacion.remove(self.nodo_aceptacion)
		self.nodos_aceptacion.remove(self.otro_thompson.nodo_aceptacion)
		self.nodos_aceptacion.append(Nodo_O_Cierre)			

	def mas(self):
		nuevoNodoMas = Nodo()
		Arista(None,self.nodo_aceptacion,nuevoNodoMas) #arista que se genera para volver al nodo inicial del thompson y asi poder pasar otra vez por el simbolo
		Arista(self.simbolo,nuevoNodoMas,self.nodo_aceptacion) #arista que va del nuevo nodo al nodo inicial del thompson
		self.nodo_aceptacion = nuevoNodoMas
		self.nodos_aceptacion.remove(self.nodo_aceptacion)
		self.nodos_aceptacion.append(nuevoNodoMas)

	def asterisco(self):
		Nodo_Ast_Inicio = Nodo()
		Nodo_Ast_Cierre = Nodo()
		Arista(None,self.nodo_aceptacion,self.nodo_inicial) #arista que se genera para volver al nodo inicial del thompson y asi poder pasar otra vez por el simbolo
		Arista(None,self.nodo_aceptacion,Nodo_Ast_Cierre) #arista que conecta el nodo aceptacion del thompson con el nuevo nodo aceptacion
		Arista(None,Nodo_Ast_Inicio,self.nodo_inicial) #arista que conecta el nuevo nodo de inicio con el nodo inicial del thompson que tengo
		Arista(None,Nodo_Ast_Inicio,Nodo_Ast_Cierre) #arista que conecta el nuevo nodo inicio con el nuevo nodo aceptacion
		self.nodo_inicial = Nodo_Ast_Inicio
		self.nodo_aceptacion = Nodo_Ast_Cierre 
		self.nodos_aceptacion.remove(self.nodo_aceptacion)
		self.nodos_aceptacion.append(Nodo_Ast_Cierre)

	def thompson_to_afd(thompson, callback):
		nuevoADF = AFD()


class AFD():
	def __init__(self):
		self.nodo_inicial = Nodo()
		self.nodos_aceptacion = []







			
