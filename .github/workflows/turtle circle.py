import turtle


spin = turtle.Turtle()
roller = turtle.Screen()
roller.bgcolor("Black")
spin.pensize(3)
spin.speed(300)
spin.pencolor("yellow")
def Spinner(spin,match):
  spin.fd(match)
  spin.rt(60)
  Spinner(spin,match - 4)

Spinner(spin,300)
mainloop()
