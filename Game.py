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

  def getComputerChoice(self):
