from turtle import Turtle
from random import choice

colors = ["#97BFB4", "#DD4A48", "#4F091D"]
angles = [-2, -3, 4, 2, -4, 5]
def player_pad():
    global  user_pad
    user_pad = Turtle()
    user_pad.speed(0)
    user_pad.color("#F5EEDC")
    user_pad.penup()
    user_pad.shape("square")
    user_pad.goto(x=0, y=-200)
    user_pad.shapesize(stretch_len=7)
    global movement
    movement = 0

    def pad_left():
        global movement
        movement += -20
        user_pad.setx(movement)

    def pad_right():
        global movement
        movement += 20
        user_pad.setx(movement)

    screen.onkey(pad_left, "Left")
    screen.onkey(pad_right, "Right")
    screen.listen()

def stone_wall():
    global wall
    wall = []
    y_position = 200
    x_position = -300
    for block in range(33):
        if block == 11:
            y_position = 150
            x_position = -300
        if block == 22:
            y_position = 100
            x_position = -300
        wall.append(Turtle())
        wall[block].speed(0)
        wall[block].shape("square")
        wall[block].color(choice(colors))
        wall[block].penup()
        wall[block].shapesize(stretch_len=2)
        wall[block].setposition(x=x_position, y=y_position)
        x_position += 50
        wall[block].setx(x_position)





def cannon_ball():
    global user_pad


    ball = Turtle()
    ball.shape("circle")
    ball.speed(0)
    ball.penup()
    ball.color("#5584AC")
    start_x = 1
    start_y = -6



    while True:
        ball.speed(0)
        new_y = ball.ycor() + start_y
        new_x = ball.xcor() + start_x
        ball.goto(new_x, new_y)


        # Detection of the player pad:
        if ball.distance(user_pad) < 70 and ball.ycor() <= -180:
            ball.speed(0)
            start_y *= -1
            start_x += choice(angles)

        # Detection of the walls:
        if ball.xcor() < -300 or ball.xcor() > 300:
            ball.speed(0)
            start_x *= -1
            start_y *= 1

        if ball.ycor() > 250:
            start_y *= -1
        elif ball.ycor() < -250:
            ball.goto(0, 0)
            t = Turtle()
            t.color("White")
            t.write("Game over !", font=("Courier", 30, "normal"), align="center")
            break

        screen.update()
        for block in wall:
            if block.distance(ball) < 25:
                start_x *= -1
                start_y *= 1
                wall.remove(block)
                block.hideturtle()

        if wall == []:
            t = Turtle()
            t.color("White")
            t.write("You win!", font=("Courier", 30, "normal"), align="center")













turtle = Turtle()
turtle.hideturtle()

screen = turtle.getscreen()
screen.bgcolor("Black")





player_pad()
stone_wall()
cannon_ball()


screen.mainloop()