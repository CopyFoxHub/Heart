from turtle import *

# You can change this
speeeeed = 2

# Setings
speed(100)
hideturtle()
pencolor("red")
pensize(5)
up()
goto(-200, 0)
down()

# 1
speed(speeeeed)

forward(50)
goto( pos() + (15, 40) )
goto( pos() + (15,-40) )
forward(10)
goto( pos() + (5,-15) )
goto( pos() + (5,15) )
forward(5)
goto( pos() + (10, 75) )
goto( pos() + (10,-150) )
goto( pos() + (10, 100) )
goto( pos() + (5, -50))
forward(10)
goto( pos() + (5, 25) )
forward(25)

# 2
forward(50)
goto( pos() + (15, 40) )
goto( pos() + (15,-40) )
forward(10)
goto( pos() + (5,-15) )
goto( pos() + (5,15) )
forward(5)
goto( pos() + (10, 75) )
goto( pos() + (10,-150) )
goto( pos() + (10, 100) )
goto( pos() + (5, -25))
forward(60)
for_me = pos()

# heart
pencolor("red")
speed(3.5)
goto(-10, -300)
goto(-200, 0)
left(120)
forward(100)
x = xcor()
rad = (-10 - x) // 2
right(30)
speed(5.5)
circle(-rad, 180)
circle(rad, -180)
speed(3.5)
goto(for_me)

# End
done()
