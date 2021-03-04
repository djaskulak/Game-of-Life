import random
import job from Job
import house from house
import board from Board

class Person:
  def __init__ (self, name, money=10000):
    self.name = name
    self.money = money

  def add_kid (self, kids):
    kids = random.randint(0, 4)
    money = money - (kids * 1000)
    print ("You now have {kids} kids!")
    return money, kids

