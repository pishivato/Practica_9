from abc import abstractmethod
from abc import ABCMeta

class Interfaz(metaclass=ABCMeta):
	
	@abstractmethod
	def Cocinar(self):
		pass
	@abstractmethod
	def PrepararIngredientes(self):
		pass
	@abstractmethod
	def Servir(self, comida):
		pass

class RobotPreparador(Interfaz):

	def __init__(self, puesto):
		self.puesto = puesto
		self.FLAG = 0
	
	def Cocinar(self):
		print("La comida no esta tan bien cocinada -.- \n")
	
	def PrepararIngredientes(self):
		print("Los ingredientes estan preparados correctamente!! \n")
	
	def Servir(self, comida):
		self.comida = comida
		print(f"El Robot->{self.puesto} tiro el plato de {self.comida} para el cliente !! \n")

class RobotCocinero(Interfaz):

	def __init__(self, puesto):
		self.puesto = puesto
		self.FLAG = 0

	def Cocinar(self):
		print("La comida esta Perfectamente cocinada!! \n")
	
	def PrepararIngredientes(self):
		print(f"El robot->{self.puesto} no preparo muy bien los ingredientes -.- !! \n")
	
	def Servir(self, comida):
		self.comida = comida
		print(f"El robot->{self.puesto} no llevo toda la comida a la mesa -.- !! \n")

class RobotMesero(Interfaz):

	def __init__(self, puesto):
		self.puesto = puesto
		self.FLAG = 0

	def Cocinar(self):
		print(f"El robot-> {self.puesto} no sabe cocinar muy bien -.- !! \n")
	
	def PrepararIngredientes(self):
		print(f"El robot-> {self.puesto} no sabe donde estan los ingredientes -.- !! \n")
	
	def Servir(self, comida):
		self.comida = comida
		print(f"El platillo de {self.comida} esta Servido!! \n")


