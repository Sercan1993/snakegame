import turtle as tr
import time
import random
hiz = 0.15

pencere = tr.Screen()
pencere.title('yılan oyunu')
pencere.bgcolor('black')
pencere.setup(width=1200, height=1200)
pencere.tracer(0)

ti = tr.Turtle()
ti.speed(0)
ti.shape('turtle')
ti.color('red')
ti.penup()
ti.goto(0, 100)
ti.direction = 'stop'

cari = tr.Turtle()
cari.speed(0)
cari.shape('square')
cari.color('blue')
cari.penup()
cari.goto(0, 0)
cari.shapesize(1, 1)
cari.direction = 'stop'

kudelepe = []
puan = 0

ncari = tr.Turtle()
ncari.speed(0)
ncari.shape("square")
ncari.color("white")
ncari.penup()
ncari.hideturtle()
ncari.goto(0,130)
ncari.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

def move():
    if ti.direction == 'up':
         y = ti.ycor()
         ti.sety(y + 20)
    if ti.direction == 'down':
         y = ti.ycor()
         ti.sety(y - 20)
    if ti.direction == 'right':
         x = ti.xcor()
         ti.setx(x + 20)
    if ti.direction == 'left':
         x = ti.xcor()
         ti.setx(x - 20)
def go_up():
    if ti.direction != 'down':
        ti.direction = 'up'

def go_down():
    if ti.direction != 'up':
        ti.direction = 'down'
def go_right():
    if ti.direction != 'left':
        ti.direction = 'right'
def go_left():
    if ti.direction != 'right':
        ti.direction = 'left'

pencere.listen()
pencere.onkey(go_up, "Up")
pencere.onkey(go_down, "Down")
pencere.onkey(go_left, "Left")
pencere.onkey(go_right, "Right")

while True:
    pencere.update()


    if ti.xcor() > 600 or ti.xcor() < -600 or ti.ycor() > 600 or ti.ycor() < -600:
       time.sleep(1)
       ti.goto(0, 0)
       ti.direction = 'stop'

       for kudeli in kudelepe:
           kudeli.goto(1000, 1000)
           hiz = 0.15

    if ti.distance(cari) < 20:
        x = random.randint(-450, 450)
        y = random.randint(-450, 450)
        cari.goto(x, y)

    if ti.distance(kudelepe) <1 :
        time.sleep(1)
        ti.goto(0, 0)
        ti.direction = 'stop'


        agnekudeli = tr.Turtle()
        agnekudeli.speed(0)
        agnekudeli.shape('turtle')
        agnekudeli.color('yellow')
        agnekudeli.penup()
        kudelepe.append(agnekudeli)

        hiz = hiz - 0.001

        puan = puan + 10
        ncari.clear()
        ncari.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
    for i in range(len(kudelepe) - 1, 0, -1):

       x = kudelepe[i - 1].xcor()
       y= kudelepe[i - 1].ycor()
       kudelepe[i].goto(x, y)

    if len(kudelepe) > 0:

       x = ti.xcor()
       y = ti.ycor()
       kudelepe[0].goto(x, y)
    move()
    time.sleep(hiz)