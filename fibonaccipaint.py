# Programa que plota a proporção áurea em python usando turtle
# feito por Adriano Carvalho e João Eduardo
# bibliotecas que temos que incluir
import turtle
import math

def fiboPlot(n):
	# criar a tela
	tela = turtle.Screen()

	#fazer a tela aparecer no topo
	rootwindow = tela.getcanvas().winfo_toplevel()
	rootwindow.call('wm', 'attributes', '.', '-topmost', '1')

	#o começo de tudo
	a = 0
	b = 1
	sqa = a
	sqb = b

	# cor da caneta azul pra desenhar os quadrados
	x.pencolor("blue")

	# desenhando os quadrados
	x.forward(b * f)
	x.left(90)
	x.forward(b * f)
	x.left(90)
	x.forward(b * f)
	x.left(90)
	x.forward(b * f)

	# dando sequência em fibonacci
	temp = sqb
	sqb = sqb + sqa
	sqa = temp
	
	# desenhando os outros quadrados
	for i in range(1, n):
		x.backward(sqa * f)
		x.right(90)
		x.forward(sqb * f)
		x.left(90)
		x.forward(sqb * f)
		x.left(90)
		x.forward(sqb * f)

		# dando sequência de novo
		temp = sqb
		sqb = sqb + sqa
		sqa = temp

	# botando a caneta no ponto inicial da espiral
	x.penup()
	x.setposition(f, 0)
	x.seth(0)
	x.pendown()
	
	# mudando a cor da caneta de azul pra vermelho
	x.pencolor("red")

	# plotando a espiral
	x.left(90)
	for i in range(n):
		print(b)
		fdwd = math.pi * b * f / 2
		fdwd /= 90
		for j in range(90):
			x.forward(fdwd)
			x.left(1)
		temp = a
		a = b
		b = temp + b


# f é o que indica o tamanho da plotagem
# aumente no código pra ter um plot maior
f = 1

# input pra indicar o quão longo a pessoa gosta de sua proporção áurea
n = int(input("Quão longo você gosta? "))

# plotagem e contagem ao mesmo tempo
if n > 0:
	x = turtle.Turtle()
	x.speed(100)
	fiboPlot(n)
	turtle.done()
else:
	print("Se você botar 0 o bagulho não roda!")