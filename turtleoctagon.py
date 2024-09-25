import turtle

screen = turtle.Screen()
screen.bgcolor("white")

octagon = turtle.Turtle()
octagon.speed(3)

colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan"]

def draw_multicolored_octagon():
    for color in colors:
        octagon.color(color)
        octagon.forward(100)
        octagon.left(45)

draw_multicolored_octagon()

turtle.done()
