import turtle

w=turtle.Screen()
w.title('spiral')
w.bgcolor('black')

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'brown', 'gray']

t=turtle.Pen()
t.speed(700)


for i in range(360):
    color = colors[i % len(colors)]
    t.pencolor(color)
    t.width(i/100 + 1)
    t.circle(i)
    t.circle(-i)
    t.left(i)

     
    
    

turtle.done()