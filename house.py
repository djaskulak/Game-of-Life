import random 
import person from person

class House():
  def __init__(self, house, cost):
    self.house = list['shack', 'ranch', 'duplex', 'mansion', 'beach house']
    self.cost = random.randint(100000, 1000000)

  def choose_house(home, cost):
    house_q = input('Would you like to purchase a house? y/n')

    if house_q == 'y':
      home = random.choice(house)
      money = money - cost
      print('You now live in a {home}!')
      print('You now have {money} dollars.')

    else:
      print('You chose not to buy a new house.')
