import random

class JobList():
  def __init__ (self):
    i1 = {'job' : 'plumber', 'salary' : 56000}
    i2 = {'job' : 'bartender', 'salary' : 26000}
    i3 = {'job' : 'pilot', 'salary' : 175000}
    i4 = {'job' : 'store manager', 'salary' : 100000}

    e1 = {'job' : 'doctor', 'salary' : 500000}
    e2 = {'job' : 'software engineer', 'salary' : 200000}
    e3 = {'job' : 'CFO', 'salary' : 250000}
    e4 = {'job' : 'therapist', 'salary' : 100000}

    self.job_diploma = [i1, i2, i3, i4]
    self.job_degree = [e1, e2, e3, e4]
  
  def select_job (self):
    job_q = input("Would you like to go to college? y/n ")

    if job_q == 'y':
      job = random.choice(self.job_degree)
      print(f"You are now a {job}!")
      return job['salary']

    else:
      job = random.choice(self.job_diploma)
      print(f"You are now a {job}!")
      return job['salary']
