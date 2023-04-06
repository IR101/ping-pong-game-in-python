import turtle
import winsound

window = turtle.Screen()        # intializing Screen

window.title("GAME DEVELOPMENT 1 ATTEMPT :)")  # Title
window.bgcolor("white")                        # Background Color
window.setup(width=800, height=600)            # Dimensions
window.tracer(0)                               # Stop auto screen refresh rate so we can update Screen manually



# Paddle A
paddle_a = turtle.Turtle() 
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()                               #penup() used to remove the residue lines while moving objects
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle() 
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score variables
score_a = 0
score_b = 0


# FUNCTION
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y<=265:
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y>=-265:
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y<=265:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y>=-265:
        paddle_b.sety(y)

# Pen
pen =turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  |  Player B: 0" , align="center", font=("Courier", 20, "normal"))

# Keyboard Binding
window.listen()                   # to listen keyboard
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")



# FOR UPDATING SCREEN MANUALLY

while True:

    window.update() 

    # Moving the Ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  |  Player B: {score_b}" , align="center", font=("Courier", 20, "normal"))


    if ball.xcor() < -390:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  |  Player B: {score_b}" , align="center", font=("Courier", 20, "normal"))


    # Paddle and Ball Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    