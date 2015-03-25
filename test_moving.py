from board import random_board
from board_str import board_str
from go import go, BoundaryError
from game import Game
from character import Character
from tick import tick

b = random_board()
g = Game(b, [Character(100, 200)])

actions = {
  'q': exit,
  'u': lambda: go('north', g.board),
  'd': lambda: go('south', g.board),
  'l': lambda: go('west', g.board),
  'r': lambda: go('east', g.board)
}

class CommandError(Exception):
  def __str__(self):
    return "Invalid command!"

def do_thing(command, *args):
  try:
    actions[command](*args)
    tick(g)
  except KeyError:
    raise CommandError()

while True:
  print(chr(27) + "[2J")
  print board_str(g.board)
  print g.party[0].hp
  while True:
    command = raw_input()
    try:
      do_thing(command)
      break
    except Exception as e:
      print e
