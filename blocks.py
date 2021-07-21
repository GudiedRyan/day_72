from turtle import Turtle

class Block(Turtle):
    
    def __init__(self, coordinate):
        super().__init__()
        self.index = coordinate
        self.active = True
    
    def change_color(self):
        self.color("black")
        self.active = False
    

class BlockRow:

    def __init__(self, color, yval):
        self.color = color
        self.yval = yval
        self.xvals = [-210,-140,-70,0,70,140,210]
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        for coordinate in self.xvals:
            block = Block(coordinate)
            block.penup()
            block.shape("square")
            block.shapesize(stretch_wid=1.5, stretch_len=3)
            block.color("black", self.color)
            block.goto(coordinate, self.yval)
            self.blocks.append(block)