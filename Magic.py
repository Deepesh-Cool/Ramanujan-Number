limit = int(input("Enter The Limit\n"))
import turtle
wn = turtle.Screen()
wn.bgcolor("Pink")
Point = turtle.Turtle()
Point.up()
Point.speed(0)
Point.setpos(-300,50)
Point.begin_fill()
Point.fillcolor("Black")
Point.circle(250)
Point.end_fill()
Point1 = turtle.Turtle()
Point1.color("Pink")
Point1.up()
Point1.setpos(-450,175)
Point1.write("RAMANUJAN MAGIC NO.",font = ("Times New Roman",30,"normal"))
Magic = turtle.Turtle()
Magic.color("Black")
Magic.up()
x=0
y=200
Magic.setpos(x,y)
count = 0
i = 0
while i<limit:
	j = 1
	while j**3<i:
		k = j+1
		while j**3+k**3<=i:
			if j**3+k**3==i:
				count += 1
			k += 1
		j += 1
	if count == 2:
		y = y-50
		Magic.write("{}".format(i),font = ("Times New Roman",50,"normal"))
		Magic.goto(x,y)
	count = 0
	i += 1
wn.exitonclick()
