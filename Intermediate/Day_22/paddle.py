from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle:
    def __init__(self):
        self.segments = []
        # self.head = self.segments[0]
        # self.create_paddle()

    def create_paddle(self, positions):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.goto(position)
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)




