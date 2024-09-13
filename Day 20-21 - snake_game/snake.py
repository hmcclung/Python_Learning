from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction_change = 0

    def create_snake(self):
        """Creates three segments to form the initial snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the existing snake body"""
        new_segment = Turtle(shape="square")
        new_segment.color("#9ce383")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a single snake segment to the back of the current snake body"""
        self.add_segment(self.segments[-1].position())
        # add a new segment to the snake

    def reset(self):
        """Resets the snake to the original 3 segment body"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Moves the snake forward by the specified MOVE DISTANCE"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.direction_change = 0

    def up(self):
        """Changes the snake heading to up unless the current heading is down"""
        if self.head.heading() != DOWN and self.direction_change < 1:
            self.head.setheading(UP)
            self.direction_change += 1

    def down(self):
        """Changes the snake heading to down unless the current heading is up"""
        if self.head.heading() != UP and self.direction_change < 1:
            self.head.setheading(DOWN)
            self.direction_change += 1

    def left(self):
        """Changes the snake heading to left unless the current heading is right"""
        if self.head.heading() != RIGHT and self.direction_change < 1:
            self.head.setheading(LEFT)
            self.direction_change += 1

    def right(self):
        """Changes the snake heading to down unless the current heading is left"""
        if self.head.heading() != LEFT and self.direction_change < 1:
            self.head.setheading(RIGHT)
            self.direction_change += 1
