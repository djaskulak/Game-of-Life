import random
from job import JobList
from house import House
from person import Person

class Board(): 
  def __init__(self, player, joblist, house):
    self.actions = ["job", "home", "kid"]
    self.player = player
    self.joblist = joblist
    self.house = house

  def select_action(self):
    return random.choice(self.actions)

  def begin_game(self):
    play = True

    while play is True:
      like = input("Would you like to play a turn? y/n ")
      if like == 'y':
        action = self.select_action()
        print(action)
        if action == "home":
          house.choose_house()
        elif action == "job":
          self.player.money += self.joblist.select_job()
        else:
          self.player.add_kid(1000)
      else:
        print("It was nice playing with you!")
        self.player.print_attributes()



if __name__ == "__main__":
  player1 = Person()
  player1.get_name()

  house = House()
  job_list = JobList()

  game_board = Board(player1, job_list, house)
  game_board.begin_game()