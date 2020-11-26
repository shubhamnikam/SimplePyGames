import turtle
from components import paddle_a, paddle_b

# config var
window_width = 800
window_height = 600
player_a_move_up_key = "w"
player_a_move_down_key = "s"
player_b_move_up_key = "Up"
player_b_move_down_key = "Down"


def paddle_a_up():
    y = paddle_a.ycor()
    if y < 240:
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)


# perform action - key board binding
window = turtle.Screen()
window.title("pong by @SN")
window.bgcolor("black")
window.setup(width=window_width, height=window_height)
window.tracer(0)
window.listen()

# bind events
window.onkeypress(paddle_a_up, player_a_move_up_key)
window.onkeypress(paddle_a_down, player_a_move_down_key)
window.onkeypress(paddle_b_up, player_b_move_up_key)
window.onkeypress(paddle_b_down, player_b_move_down_key)
