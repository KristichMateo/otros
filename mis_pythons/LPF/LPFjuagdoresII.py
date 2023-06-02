import random



class Equipo:
	def __init__(self, pdg , nombre, pdd, pdc, jugadores):
		self.nombre = nombre
		self.pdg = pdg
		self.puntos = 0
		self.pdd = pdd
		self.pdc = pdc
        self.jugadores = []
Talleres = Equipo(75,"Talleres de Cordoba",8,5,)
River = Equipo(80,"River Plate",8 ,5,[["J.Alvarez", [0,1,2,3]],["B.Romero", [4,5,6]],["M.Suarez", [7,8,9]]])
Estudiantes = Equipo(75,"Estudiantes de la Plata",9,5)
Lanus = Equipo(73,"Lanus",14,5,[["Sand", [0,1,2,3,4]],["J.M.Lopez", [5,6,7]]])
Independiente = Equipo(81,"Independiente",9,5,[["S.romero", [0,1,2,3,4]],["A.Roa", [5,6,7]],["Palacios", [8,9]]])
Tomba = Equipo(73,"Godoy Cruz",14,5,[["Ojeda", [1,2,3,4,5,6]],["Bullaude", [7,8,9]],["Badaloni", [0]]])
Boca = Equipo(78,"Boca Juniors",7,5,[["Vazquez", [1,2,3]],["Pavon", [4,5]],["Cardona", [6,7,8,9]]])
Velez = Equipo(77,"Velez Sarfield",8,5,[["TAlmada", [1,2,3,4]],["Lucero", [5,6,7]],["Orellano", [8,9]]]) 
Colon = Equipo(76,"Colon",12,5,[["Farias", [1,2,3]],["Ferreira", [4,5,6]],["Beltran", [7,8,9]]])
Racing = Equipo(78,"Racing",5,5,[["Copeti", [1,2,3,4]],["Chancalay", [5,6,7]],["Dominguez", [8,9]]])
Gimnasia = Equipo(68,"Gimnasia y Esgrima de la Plata",11,4,[["Pulga Rodriguez", [1,2,3,4]],["Contin", [5,6]],["Torres",[7,8,9]]])
Rosario_Central = Equipo(72,"Rosario Central",14,4,[["Vechio", [1,2,3,4]],["Marco Ruben", [5,6,7]],["LGamba", [8,9]]])
Defensa = Equipo(73,"Defensa y Justicia",9,4,[["Bou", [1,2,3,4]],["Pizzini", [5,6,7]],["Merentiel", [8,9]]])
Argentinos = Equipo(74,"Argentinos Juniors",6,5,[["Reniero", [2,3]],["Avalos", [5,6,7,8]],["Mcallister", [8,1]]])
Newells = Equipo(73,"Newell's Old Boys",15,4,[["Castro", [1,2,3,4]],["Scoco", [5,6,7]],["MRodriguez", [8,9]]])
Atletico = Equipo(70,"Atletico Tucuman",13,4,[["Puch", [1,2,3,4]],["Heredia", [5,6,7]],["Coman", [8,9]]])
Patronato = Equipo(65,"Patronato",10,4,[["Sosa", [1,2,3,4]],["Comas", [5,6,7]],["Leys", [8,9]]])
Huracan = Equipo(67,"Huracan",6,5,[["Cocaro", [1,2,3,4]],["Cristaldo", [5,6,7]],["Rincon", [8,9]]])
San_Lorenzo = Equipo(72,"San Lorenzo",11,4),[["Uvita", [1,2,3,4]],["Di Santo", [5,6,7]],["Ortigoza", [8,9]]]
Sarmiento = Equipo(63,"Sarmiento de Junin",11,4,[["Gondou", [1,2,3,4]],["Salinas", [5,6,7]],["Vismara", [8,9]]])
Aldosivi = Equipo(63,"Aldosivi",19,4,[["Carteruccio", [1,2,3,4,5]],["Hauche", [8,6,7]],["Rinaldi", [9]]])
Platense = Equipo(62,"Platense",13,4,[["Curuchet", [1,2,3,4]],["Mansilla", [5,6,7]],["Tijanovich", [8,9]]])
Union = Equipo(63,"Union de Santafe",13,4,[["Blandi", [1,2,3,4]],["Marquez", [5,6,7]],["Cordero", [8,9]]])
Central_Cordoba = Equipo(62,"Central Cordoba",14,4,[["Riano", [1,2,3,4]],["Melano", [5,6,7]],["Sequiera", [8,9]]])
Banfield = Equipo(65,"Banfield",10,4,[["Pons", [1,2,3,4]],["Datolo", [5,6,7]],["Sonora", [8,9]]])
Arsenal = Equipo(61,"Arsenal de Sarandi",14,4,[["Mazzola", [1,2,3,4]],["Albertengo", [5,6,7]],["Sepulveda", [8,9]]])

E= [Tomba,Boca,Talleres,River,Estudiantes,Lanus,Independiente,Velez,Colon,Racing,Gimnasia,Rosario_Central,
Defensa,Argentinos,Newells,Atletico,Patronato,Huracan,San_Lorenzo,Sarmiento,Aldosivi,Platense,Union,Central_Cordoba,
Banfield,Arsenal]
Puntos = []
GF = []
GC = []
DG = []
for j in range (26):
	Puntos += [0]
	GF += [0]
	GC += [0]
	DG += [0]

def gol_local (pdg,pdd,pdc):
	global golL
	golL = 0
	for k in range (pdc):
		p=random.randint(0,100)
		b=random.randint(0,25)
		if p < pdg and b < pdd:
			golL = golL+1
		if k == 4:
			return golL
	return golL
def gol_visita (pdg,pdd,pdc):
	global golV
	golV = 0
	for k in range (pdc):
		p=random.randint(0,100)
		b=random.randint(0,25)
		if p < pdg and b < pdd:
			golV = golV+1
		if k == 4:
			return golV
	return golV
for i in range (26):
	print(E[i].nombre,"en casa:")
	for c in range (26):
		l = 0
		v = 0
		if E[c].nombre != E[i].nombre:
			l = gol_local(E[i].pdg,E[c].pdd,E[i].pdc)
			print("_____",E[c].pdd)
			v = gol_visita(E[c].pdg,E[i].pdd,E[c].pdc)
			print(E[i].nombre,l,":",v, E[c].nombre)
			print(E[i].pdd)
			if v < l:
				Puntos[i] = Puntos[i]+3
			elif v == l:
				Puntos[i] = Puntos[i]+1
				Puntos[c] = Puntos[c]+1
			elif v > l:
				Puntos[c] = Puntos[c]+3
	
Q = []
for i in range(26):
	E[i].puntos = Puntos[i]
	Q.append(Puntos[i])
	
S = sorted(E, key=lambda t: t.puntos, reverse=True)


print("El campeon es:", S[0])
for E in S:
    print("|",E.nombre," |  ",E.puntos,)
