from turtle import Turtle


START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SPEED = 20


class Snake :

    def __init__(self) :
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) :
        for positions in START_POS :
            self.add_segment(positions)

    def extend(self) :
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position) :
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def change_colour(self, position):
        self.segments[position].color("red")

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def destroy_tail(self, position):
        delete_seg = self.segments[position]
        delete_seg.goto(2000, 2000)
        delete_seg.reset()
        self.segments.remove(self.segments[position])


    def move(self) :

        for seg_num in range(len(self.segments) - 1, 0, -1) :
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(SPEED)

    def up(self) :
        if self.head.heading() != DOWN :
            self.head.setheading(UP)


    def down(self) :
        if self.head.heading() != UP :
            self.head.setheading(DOWN)


    def left(self) :
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)


    def right(self) :
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)

