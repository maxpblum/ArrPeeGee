class Board(object):
  def __init__(self, rooms, path):
    self.rooms, self.path = rooms, path

class Room(object):
  def __init__(self, borders):
    self.north, self.east, self.south, self.west = borders

def make_free_room():
  return Room([True, True, True, True])

from random import choice
def rand_rooms(w, h):
  rooms = []
  for ri in range(h):
    rooms.append([])
    for ci in range(w):
      true_or_false = lambda: choice( (True, False) )
      north = False if ri == 0 else rooms[ri - 1][ci].south
      west  = False if ci == 0 else rooms[ri][ci - 1].east
      east  = False if ci == (w - 1) else true_or_false()
      south = False if ri == (h - 1) else true_or_false()
      rooms[ri].append( Room( (north, east, south, west) ) )
  print ["North: {0}, East: {1}, South: {2}, West: {3}".format(room.north, room.east, room.south, room.west) \
         for row in rooms for room in row]
  return rooms

def random_board():
  return Board( rand_rooms(choice(range(1, 6)), choice(range(1, 9))), [[0, 0]] )

def check_path(rooms, p1, p2):
  already_checked = [[False for _ in row] for row in rooms]
  current_spots   = [p1]
  while len(current_spots > 0):
    row, col = current_spots.pop()
    if (row, col) == p2:
      return True
    already_checked[row][col] = True
    if row > 0 and not already_checked[row - 1][col]:
      current_spots.append( (row - 1, col) )
    if col > 0 and not already_checked[row][col - 1]:
      current_spots.append( (row, col - 1) )
    if row < len(rooms) and col < len(rooms[row + 1]) and not already_checked[row + 1][col]:
      current_spots.append( (row + 1, col) )
    if col < len(rooms[row]) and not already_checked[row][col + 1]:
      current_spots.append( (row, col + 1) )
  return False
