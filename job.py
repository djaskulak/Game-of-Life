import random
import person from Person

class Job(self, job, money):
  def __init__ (self, job, salary):
    self.job = job
    self.salary = salary
  
  i1 = {'job' : 'plumber', 'salary' : 56000}
  i1 = {'job' : 'bartender', 'salary' : 26000}
  i3 = {'job' : 'pilot', 'salary' : 175000}
  i4 = {'job' : 'store manager', 'salary' : 100000}

  e1 = {'job' : 'doctor', 'salary' : 500000}
  e2 = {'job' : 'software engineer', 'salary' : 200000}
  e3 = {'job' : 'CFO', 'salary' : 250000}
  e4 = {'job' : 'therapist', 'salary' : 100000}

  diploma = [i1, i2, i3, i4]
  degree = [e1, e2, e3, e4]

  def select_job (job, diploma, degree):
    job_q = input("Would you like to go to college? y/n")

    if job_q == 'y':
      job = random.choice(degree)
      money += job['salary']

    else:
      job = random.choice(diploma)
      money += job['salary']
