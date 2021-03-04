import random
import job from Job

class Person:
  def __init__ (self, name, money=10000):
    self.name = name
    self.money = money

  def add_kid (self, kids):
    kids = random.randint(0, 4)
    return ("You now have {kids} kids")
