import random
from job import Job
from house import House
from board import Board

class Person:
  def __init__ (self, name, money=10000):
    self.name = name
    self.money = money

  def get_name (self, name):
    name = input("Welcome! What is your name? ")
    return name

  def add_kid (self, kids=0, money):
    self.kids = kids
    kids = random.randint(0, 4)
    self.money = money
    money -= (kids * 1000)
    print ("You now have {kids} kids!")
    return money, kids

  def print_attributes (self, name, money, job, salary, kids, home):
    print ("Hello! Your name is {name}")
    print ("Your balance is {money}")
    print ("You are a {job} and make ${salary}")
    print ("You have {kids} kids")
    print ("You live in a {home}")


if __name__ == "__main__":
  name = get_name(name)

  play = True

  while play is True:
    like = input("Would you like to play a turn? y/n")
    if like == 'y':
      board.select_action
    else:
      print("It was nice playing with you!")