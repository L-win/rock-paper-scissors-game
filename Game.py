import random

class Game:
  computerChoice = None
  playerChoice = None
  computerPoints = 0
  playerPoints = 0
  choices = ['rock', 'paper', 'scissors']
  rules = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
  
  def __init__(self, playerPoints, computerPoints):
    self.playerPoints = playerPoints
    self.computerPoints = computerPoints
    # self.getPlayerChoice()
    # self.getComputerChoice()
    # self.round()
  
  def getPlayerChoice(self):
    print('== Make your choice ==\n1 - rock\n2 - paper\n3 - scissors\n4 - exit game')
    choice = input('Enter number: ')
    try:
      int(choice)
    except ValueError:
      print('\n== Wrong value!')
      exit()
    if int(choice) == 4:
      print()
      print('='*10, 'FINISH', '='*10)
      exit()
    elif int(choice) > 4:
      print('\n== Wrong value!')
      exit()
    self.playerChoice = self.choices[int(choice)-1]

  def getComputerChoice(self):
    choice = random.randint(0,2)
    self.computerChoice = self.choices[choice]
