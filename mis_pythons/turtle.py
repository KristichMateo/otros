import turtle as t 
ang=10

t.speed(700)
t.setup(500,500)
t.shape("turtle")
t.color("green","blue")

def rec (b,c):
	
	t.penup()
	
	t.pendown()
	t.forward(b)
	t.seth(90)
	t.forward(c)
	t.seth(180)
	t.forward(b)
	t.seth(270)
	t.forward(c)

def rectangulo (a,h):
	
	t.penup()
	t.goto(100,100)
	t.pendown()
	t.forward(a)
	t.seth(90)
	t.forward(h)
	t.seth(180)
	t.forward(a)
	t.seth(270)
	t.forward(h)

def Nlin():
		t.penup()
def Slin():
		t.pendown()
def derecha():
		t.seth(360)
		t.forward(10)
def izquierda():
		t.seth(180)
		t.forward(10)
def arriba():
		t.seth(90)
		t.forward(10)
def abajo():
		t.seth(270)
		t.forward(10)
def pos():
		print(t.pos() )
		print("esta es su posicion" )
	
	
contra=str(input("la contraseña"))
if contra=="hola":
	for c in range(500):
		ang=ang+5
		t.seth(ang)
		t.forward(200)
		t.left(225)
		t.forward(200)
		t.goto(0,0)
		if c==100:
			t.goto(300,300)
			for f in range(100):
				t.goto(300,300)
				ang=ang+5
				t.seth(ang)
				t.forward(200)
				t.left(225)
				t.forward(200)
				t.goto(0,0)
		elif c==200:
			t.goto(-300,-300)
			for f in range(100):
				t.goto(-300,-300)
				ang=ang+5
				t.seth(ang)
				t.forward(200)
				t.left(225)
				t.forward(200)
				t.goto(0,0)
		elif c==300:
			t.goto(300,-300)
			for f in range(100):
				t.goto(300,-300)
				ang=ang+5
				t.seth(ang)
				t.forward(200)
				t.left(225)
				t.forward(200)
				t.goto(0,0)
		elif c==400:
			t.goto(-300,300)
			for f in range(100):
				t.goto(-300,300)
				ang=ang+5
				t.seth(ang)
				t.forward(200)
				t.left(225)
				t.forward(200)
				t.goto(0,0)
elif contra=="chau":
	
	j=int(input("ingrese el valor de la base su rectangulo"))
	h=int(input("ingrese el valor de la altura  su rectangulo"))
	rec(b=h,c=j)
	t.onkey(derecha,"d")
	t.onkey(izquierda,"a")
	t.onkey(arriba,"w")
	t.onkey(abajo,"s")
	t.onkey(Nlin,"y")
	t.onkey(Slin,"t")
	t.onkey(pos,"p")
	t.onkey(rec,"r")
	t.listen()
else:
	
	rectangulo(150,90)
	
t.done()
