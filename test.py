import turtle

def draw_shapes():
    turtle.bgcolor("darkblue")
    draw = turtle.Turtle()
    draw.shape("turtle")
    draw.color("yellow")
    draw.speed(2)

    rotate = 0
    while rotate <= 40:
        draw.right(10)
        rotate += 1
        steps = 0
        while steps <= 3:
            draw.forward(100)
            draw.left(90)
            steps += 1

draw_shapes()
