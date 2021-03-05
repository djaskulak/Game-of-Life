import random

class Person:
  def __init__ (self, name='', money=10000):
    self.name = name
    self.money = money
    self.home = ''
    self.job = ""

  def get_name (self):
    self.name = input("Welcome! What is your name? ")
    return self.name

  def add_kid (self, money):
    self.kids = random.randint(0, 4)
    self.money = money
    money -= (self.kids * 1000)
    print (f"You now have {self.kids} kids!")
    return money, self.kids

  def print_attributes (self):
    print (f"Hello! Your name is {self.name}")
    print (f"Your balance is {self.money}")
    # print (f"You are a {job} and make ${salary}")
    print (f"You have {self.kids} kids")
    print (f"You live in a {self.home}")