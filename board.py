import random
from job import Job
from person import Person

class Board(Job, Person): 
  def __init__(self, actions):
    self.actions = actions
  
  actions = [select_job, select_house, add_kid]

  def select_action(self, actions):
    random.choice(actions)