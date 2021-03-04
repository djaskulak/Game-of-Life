import random
from job import Job
from person import Person

class Board(Job, Person): 
  def __init__(self, actions):
    self.actions = actions
  
  select_j = select_job()
  select_h = select_house()
  select_k = add_kid()

  actions = [select_j, select_h, select_k]

  def select_action(self, actions):
    random.choice(actions)