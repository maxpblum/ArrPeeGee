class BoundaryError(Exception):
  def __init__(self, cardinal):
    self.cardinal = cardinal
  def __str__(self):
    return repr('Path {0} is blocked!'.format(self.cardinal))

cardinal_funcs = {
  'north': (lambda room: room.north, lambda r, c: (r - 1, c) ),
  'south': (lambda room: room.south, lambda r, c: (r + 1, c) ),
  'east':  (lambda room: room.east, lambda r, c: (r, c + 1) ),
  'west':  (lambda room: room.west, lambda r, c: (r, c - 1) )
}

def go(cardinal, b):

  cur_row, cur_col = b.path[-1]
  check_wall, get_new_point = cardinal_funcs[cardinal]

  if check_wall( b.rooms[cur_row][cur_col] ) == False:
    raise BoundaryError(cardinal)

  b.path.append( get_new_point( cur_row, cur_col ) )
