import random
import job from Job
import person from Person

class Board(): 
  def __init__(self, actions):
    self.actions = actions
  
  actions = [select_job, select_house, add_kid]

  def select_action(actions):
    random.choice(actions)