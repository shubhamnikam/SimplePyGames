from components import ball, paddle_a, paddle_b, pen

# setup score var
score_a = 0
score_b = 0


# move ball
def move_ball():
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# boarder check for y
def boarder_check_y():
    # check boarder y top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # check boarder y down
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


# boarder check for x
def boarder_check_x():
    global score_a, score_b
    # check boarder x right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 12, "normal"))

    # check boarder x right
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 12, "normal"))


# collision detection
def collision_detection():
    # collision for paddle b
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    # collision for paddle a
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
