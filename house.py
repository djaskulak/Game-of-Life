import random 

class House():
  def __init__(self):
    self.house = ['shack', 'ranch', 'duplex', 'mansion', 'beach house']
    self.cost = random.randint(100000, 1000000)


  def choose_house(self):
    house_q = input('Would you like to purchase a house? y/n ')

    if house_q == 'y':
      home = random.choice(self.house)
      
      print(f'You now live in a {home}! The cost of this is {self.cost}')
      return (self.cost, home)

    else:
      print('You chose not to buy a new house.')
