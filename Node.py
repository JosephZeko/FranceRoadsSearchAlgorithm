#!/usr/bin/python3

#Class node
#used for representing the nodes on the france map
class Node:
    def __init__(self, name, parent=None, f=0, g=0, h=0):
        self.name = name.capitalize()
        self.parent = parent
        self.f = f
        self.g = g
        self.h = h