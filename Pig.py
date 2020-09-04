#https://www.codesdope.com/python-subclass-of-a-class/


class Pig:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Player:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Human(Player):
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Computer(Player):
  def __init__(self, name, age):
    self.name = name
    self.age = age