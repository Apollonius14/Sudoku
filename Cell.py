from collections import deque
from collections import Counter
from random import randint
import math


class cell(object):

    def __init__(self, x, y, w, h):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.state = 1
        self.num_val = deque([" ", 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.pad = self.w * 0.05
        self.active = False
        self.chosen = False

    def display(self):

        # A cell can be in one of X states:
        # 0 initialized by computer to a pre-set and unchangeable value between 1 and 9
        # 1 empty and unhighlighted
        # 2 empty and highlighted
        # 3 empty and clicked
        # 4 full with content being modified
        # 5 full with content final

        if self.chosen == True:
            self.state = 0

        if self.state == 0:
            strokeWeight(2)
            fill(150, 10)
            strokeJoin(ROUND)
            rect(self.x + self.pad, self.y + self.pad, self.w - self.pad * 2, self.h - self.pad * 2)

            noFill()
            textSize(self.w * 0.8)
            textAlign(CENTER)
            noStroke()
            fill(0)
            text(self.num_val[0], self.x + self.w * 0.5, self.y + self.h * 0.8)

        if self.state == 1:
            fill(255)
            strokeWeight(10)
            strokeJoin(ROUND)
            stroke(10, 10, 10, 10)
            rect(self.x, self.y, self.w, self.h)

        if self.state == 2:
            fill(0)
            strokeWeight(10)
            strokeJoin(ROUND)
            stroke(10, 10, 10, 10)
            rect(self.x, self.y, self.w, self.h)

        if self.state == 3:
            strokeWeight(15)
            fill(240, 120, 120)
            strokeJoin(ROUND)
            rect(self.x + self.pad, self.y + self.pad, self.w - self.pad * 2, self.h - self.pad * 2)

        if self.state == 4:
            strokeWeight(15)
            fill(240, 120, 120)
            strokeJoin(ROUND)
            rect(self.x + self.pad, self.y + self.pad, self.w - self.pad * 2, self.h - self.pad * 2)

            noFill()
            textSize(self.w * 0.8)
            textAlign(CENTER)
            noStroke()
            fill(255)
            text(self.num_val[0], self.x + self.w * 0.5, self.y + self.h * 0.8)

        if self.state == 5:
            strokeWeight(15)
            fill(120, 200, 200)
            strokeJoin(ROUND)
            rect(self.x + self.pad, self.y + self.pad, self.w - self.pad * 2, self.h - self.pad * 2)

            noFill()
            textSize(self.w * 0.8)
            textAlign(CENTER)
            noStroke()
            fill(150)
            text(self.num_val[0], self.x + self.w * 0.5, self.y + self.h * 0.8)

    def listen(self):

        if self.state == 1:

            if self.mouse_inside():
                self.state = 2

        if self.state == 2:

            if not self.mouse_inside():
                self.state = 1
            if mousePressed:
                self.state = 3

        if self.state == 3:

            if mousePressed and not self.mouse_inside():
                self.state = 1
                cell.moved = True
            if mousePressed and self.mouse_inside():
                self.state = 4

        if self.state == 4:

            if not mousePressed:
                self.active = True

            if self.active:

                if mousePressed and mouseButton == LEFT and self.mouse_inside():
                    self.num_val.rotate(1)

                if mousePressed and mouseButton == RIGHT and self.mouse_inside():
                    self.num_val.rotate(-1)

                if mousePressed and not self.mouse_inside():
                    self.active = False
                    self.state = 5

        if self.state == 5:

            self.active = False

            if self.num_val[0] == " ":
                self.state = 1
            if self.mouse_inside() and mousePressed:
                self.state = 4

    def mouse_inside(self):
        return ((self.x < mouseX < self.x + self.w) and (self.y < mouseY < self.y + self.h))