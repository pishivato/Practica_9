from robot import RobotPreparador, RobotCocinero, RobotMesero

robot_auxi = RobotMesero(None)
robot_Prep = RobotPreparador("PREPARADOR")
robot_Coci = RobotCocinero("COCINERO")
robot_Mese = RobotMesero("MESERO")

Robots = []
Robots.append(robot_auxi)
Robots.append(robot_Prep)
Robots.append(robot_Coci)
Robots.append(robot_Mese)

#variables de validacion
TODO_LISTO = False
step=1

class Menu:
	def Desayuno(self, pinche, platillo):
		Accion(pinche, platillo)

	def Comida(self, pinche, platillo):
		Accion(pinche, platillo)
	
	def Cena(self, pinche, platillo):
		Accion(pinche, platillo)

def Acciones(op, platillo):		
	op_robot = int(input("Que robot quiere usar, (1)->PREPARADOR, (2)->COCINERO, (3)->MESERO \n"))

	if op == 1:
		RoboMenu.Desayuno(Robots[op_robot], platillo)
	elif op == 2:
		RoboMenu.Comida(Robots[op_robot], platillo)
	elif op == 3:
		RoboMenu.Cena(Robots[op_robot], platillo)

def Accion(pinche, platillo):
		global step
		accion = int(input(f"Que deseas hacer con el robot->{(pinche.puesto).upper()}, para completar tu alimento | (1)->Preparar, (2)->Cocinar, (3)->Servir |?\n"))
		
		if accion == 1 and step == 1:
			pinche.PrepararIngredientes()
			if pinche.puesto == "PREPARADOR":
				pinche.FLAG = 1	
			step=2
			Acciones(op, platillo)

		elif accion == 2 and step == 2:
			pinche.Cocinar()
			if pinche.puesto == "COCINERO":
				pinche.FLAG = 1
			step=3
			Acciones(op, platillo)

		elif accion == 3 and step == 3:
			pinche.Servir(platillo)
			if pinche.puesto == "MESERO":
				pinche.FLAG = 1
			TODO_LISTO = Validacion()

			if TODO_LISTO == True:
				calificacion(respuesta = int(input("Califica el servicio de los Robots Cocineros (1)->Excelente, (2)->Regular, (3)->Mal servicio: \n")))
				return 0
			print("El platillo estuvo raro \n")
			calificacion(respuesta = int(input("Califica el servicio de los Robots Cocineros (1)->Excelente, (2)->Regular, (3)->Mal servicio: \n")))
			return 0


		else:
			print(f"Lo sentimos el robot->{pinche.puesto} no sabe como hacer eso !! \n") 
			Acciones(op, platillo)

def Validacion()->"FLAG":
	global TODO_LISTO
	suma = 0
	
	for i in Robots:
		suma+=i.FLAG

	if suma == 3:
		TODO_LISTO = True
	return TODO_LISTO

def calificacion(respuesta):
	if respuesta == 1:
		print("Los Robots estan contentos \n\n")
	elif respuesta == 2:
		print("Los Robots estan tristes \n\n")
	elif respuesta == 3:
		print("Los Robots piensan que eres tont@ para manejarlos\n\n")

RoboMenu = Menu()
if __name__ == '__main__':
	op = int(input("Que quiere hacer, (1)->DESAYUNAR, (2)->COMER, (3)->CENAR? \n"))
	platillo = input("Que deseas preparar? \n")
	Acciones(op, platillo)
	

