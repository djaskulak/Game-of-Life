import random
import job from Job
import house from house
import board from Board

class Person:
  def __init__ (self, name, money=10000):
    self.name = name
    self.money = money

  def get_name (self, name):
    name = input("Welcome! What is your name? ")
    return name

  def add_kid (self, kids=0):
    kids = random.randint(0, 4)
    money = money - (kids * 1000)
    print ("You now have {kids} kids!")
    return money, kids

  def print_attributes (self, name, money, job, salary, kids, home):
    print ("Hello! Your name is {name}")
    print ("Your balance is {money}")
    print ("You are a {job} and make ${salary}")
    print ("You have {kids} kids")
    print ("You live in a {home}")

person.get_name(name)

play = True

while play is True:
  like = input("Would you like to play a turn? y/n")
  if like == 'y':
    board.select_action
  else:
    print("It was nice playing with you!")