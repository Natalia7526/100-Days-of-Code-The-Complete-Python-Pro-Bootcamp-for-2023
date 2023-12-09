import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

# TODO 1 Create the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

# TODO 2 Create and move a paddle
player_1 = Paddle(starting_position=(350, 0))
screen.listen()
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")

# TODO 3 Create another paddle
player_2 = Paddle(starting_position=(-350, 0))
screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")

# TODO 4 Create the ball and make it move
ball = Ball()

# definition of scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
# TODO 5 Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs bounce
        ball.bounce_y()

# TODO 6 Detect collision with paddle
    # collision with paddle
    if (ball.distance(player_1) < 50 and ball.xcor() > 320) or (ball.distance(player_2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

# TODO 7 Detect when paddle misses
    # detect player_1 paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect player_2 paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
# TODO 8 Keep score


screen.exitonclick()
