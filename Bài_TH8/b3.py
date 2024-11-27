print ( "SV: Luu Duc Loc , msv: 205751030110045 ")
print (" ###############")
#################
import turtle, random
colors =["red", "green", "blue"]
painter = turtle.Turtle()
painter.pensize (3)
for i in range(15):
    color = color = colors[i % 3]
    painter.speed(100)
    painter.pencolor (color)
    painter.circle (100)
    painter.right (30)
    painter.left (60)
    painter.setposition (0,0)
