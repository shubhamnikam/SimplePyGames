from events import window
from actions import move_ball, boarder_check_y, boarder_check_x, collision_detection

# main loop of game
while True:
    window.update()
    move_ball()
    boarder_check_y()
    boarder_check_x()
    collision_detection()
