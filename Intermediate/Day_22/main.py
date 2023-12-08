from turtle import Screen
from paddle import Paddle

STARTING_POSITIONS_PLAYER_1 = [(-300, -40), (-300, -20), (-300, 0), (-300, 20), (-300, 40)]
STARTING_POSITIONS_PLAYER_2 = [(300, -40), (300, -20), (300, 0), (300, 20), (300, 40)]


#TODO 1 Create the screen

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("black")
screen.title("Ping Pong")
# screen.tracer(0)

#TODO 2 Create and move a paddle

#TODO 3 Create another paddle
player_1 = Paddle()
player_1.create_paddle(positions=STARTING_POSITIONS_PLAYER_1)
player_2 = Paddle()
player_2.create_paddle(positions=STARTING_POSITIONS_PLAYER_2)
#TODO 4 Create the ball and make it move
#TODO 5 Detect collision with wall and bounce
#TODO 6 Detect collision with paddle
#TODO 7 Detect when paddle misses
#TODO 8 Keep score





screen.exitonclick()
