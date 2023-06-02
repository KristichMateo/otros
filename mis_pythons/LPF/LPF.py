import random


class Equipo:
    def __init__(self, pdg , nombre ):
        self.nombre = nombre
        self.pdg = pdg
        self.puntos = 0

Talleres = Equipo(75,"Talleres de Cordoba")
River = Equipo(80,"River Plate")
Estudiantes = Equipo(75,"Estudiantes de la Plata")
Lanus = Equipo(73,"Lanus")
Independiente = Equipo(81,"Independiente")
Tomba = Equipo(73,"Godoy Cruz")
Boca = Equipo(78,"Boca Juniors")
Velez = Equipo(77,"Velez Sarfield") 
Colon = Equipo(76,"Colon")
Racing = Equipo(78,"Racing")
Gimnasia = Equipo(68,"Gimnasia y Esgrima de la Plata")
Rosario_Central = Equipo(72,"Rosario Central")
Defensa = Equipo(73,"Defensa y Justicia")
Argentinos = Equipo(74,"Argentinos Juniors")
Newells = Equipo(73,"Newell's Old Boys")
Atletico = Equipo(70,"Atletico Tucuman")
Patronato = Equipo(65,"Patronato")
Huracan = Equipo(67,"Huracan")
San_Lorenzo = Equipo(72,"San Lorenzo")
Sarmiento = Equipo(63,"Sarmiento de Junin")
Aldosivi = Equipo(63,"Aldosivi")
Platense = Equipo(62,"Platense")
Union = Equipo(63,"Union de Santafe")
Central_Cordoba = Equipo(62,"Central Cordoba")
Banfield = Equipo(65,"Banfield")
Arsenal = Equipo(61,"Arsenal de Sarandi")

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
def gol_local (pdg):
	golL=0
	for k in range(3):
		p=random.randint(0,100)
		if p < pdg:
			golL = golL+1
		if k==2:
			return golL
	
	
def gol_visita (pdg):
	golV=0
	for k in range (3):
		p=random.randint(0,100)
		if p < pdg:
			golV = golV+1
		if k == 2:
			return golV

for i in range (26):
	print(E[i].nombre,"en casa:")
	for c in range (26):
		if E[c].nombre != E[i].nombre:
			L = gol_local(E[i].pdg)
			V = gol_visita(E[c].pdg)
			print(E[i].nombre,L,":",V, E[c].nombre)
			GF[i] += L
			GF[c] += V
			GC[c] += V 
			GC[i] += L
			if V < L:
				Puntos[i] = Puntos[i]+3
			elif V == L:
				Puntos[i] = Puntos[i]+1
				Puntos[c] = Puntos[c]+1
			elif V > L:
				Puntos[c] = Puntos[c]+3
Q = []
for i in range(26):
	E[i].puntos = Puntos[i]
	Q.append(Puntos[i])
	
S = sorted(E, key=lambda t: t.puntos, reverse=True)



for E in S:
    print("|",E.nombre," |  ",E.puntos,)
    
    
print(S[0],"Campeon!!!!!!!!!!!!!!")
