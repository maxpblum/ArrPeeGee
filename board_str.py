ROOM_SIDE = 7
JUT       = 1

OPEN_WALL   = (" " * (ROOM_SIDE - 2 - (2 * JUT))).join(["*" + ("*" * JUT)] * 2)
CLOSED_WALL = "*" * ROOM_SIDE

def init_st_arr(rooms):
  st = []
  for r in range((ROOM_SIDE - 1) * len(rooms) + 1):
    st.append([" "] * ((ROOM_SIDE - 1) * len(rooms[0]) + 1))
  return st

def draw_hor(left, st_arr, row, is_open):
  for i, ch in enumerate(OPEN_WALL if is_open else CLOSED_WALL):
    st_arr[row][left + i] = ch

def draw_ver(top, st_arr, col, is_open):
  for i, ch in enumerate(OPEN_WALL if is_open else CLOSED_WALL):
    st_arr[top + i][col] = ch

def draw_room(room, r, c, st_arr):
  top    = (ROOM_SIDE - 1) * r
  bottom = top + ROOM_SIDE - 1
  left   = (ROOM_SIDE - 1) * c
  right  = left + ROOM_SIDE - 1

  for draw_func, start, spot_pair, border_pair in \
    ((draw_hor, left, (top, bottom), (room.north, room.south)), \
     (draw_ver, top, (left, right), (room.west, room.east))):

    if spot_pair[0] == 0:
      draw_func(start, st_arr, spot_pair[0], border_pair[0])
    draw_func(start, st_arr, spot_pair[1], border_pair[1])

def draw_rooms(rooms, st_arr):
  for r in range(len(rooms)):
    for c in range(len(rooms[r])):
      draw_room(rooms[r][c], r, c, st_arr)

def get_center(room_row, room_col):
  return (room_row * (ROOM_SIDE - 1) + ROOM_SIDE / 2,
          room_col * (ROOM_SIDE - 1) + ROOM_SIDE / 2)

def draw_spot(ch, point, st_arr):
  row, col = point
  st_arr[row][col] = ch

def get_connector(p1, p2, p3):
  if p1[0] == p2[0] == p3[0]:
    return "-"
  if p1[1] == p2[1] == p3[1]:
    return "|"
  if (p3[0] - p1[0]) * (p3[1] - p1[1]) < 0:
    return "/"
  return "\\"

def excl_range(start_point, end_point):
  if end_point > start_point:
    return range(start_point + 1, end_point)
  return range(end_point + 1, start_point)

def draw_hor_seg(row, cols, st_arr):
  for c in cols:
    st_arr[row][c] = "-"

def draw_ver_seg(col, rows, st_arr):
  for r in rows:
    st_arr[r][col] = "|"

def draw_seg(p1, p2, st_arr):
  if p1[0] == p2[0]:
    seg_func = draw_hor_seg
    line     = p1[0]
    spots    = excl_range(p1[1], p2[1])
  else:
    seg_func = draw_ver_seg
    line     = p1[1]
    spots    = excl_range(p1[0], p2[0])
  seg_func(line, spots, st_arr)

def draw_path(path, st_arr):
  if len(path) > 0:
    draw_spot("O", get_center(path[-1][0], path[-1][1]), st_arr)
  if len(path) > 1:
    for i, spot in enumerate(path[:-1]):
      if i == 0:
        draw_spot("#", get_center(*spot), st_arr)
      else:
        check_r, check_c = get_center(*spot)
        if st_arr[check_r][check_c] not in "O#":
          draw_spot(get_connector(path[i - 1], spot, path[i + 1]), get_center(*spot), st_arr)
      draw_seg(get_center(*spot), get_center(*path[i + 1]), st_arr)


def make_str(st_arr):
  return "\n".join("".join(row) for row in st_arr)

def board_str(board):

  if len(board.rooms) == 0:
    return ""

  st_arr = init_st_arr(board.rooms)
  draw_rooms(board.rooms, st_arr)
  draw_path(board.path, st_arr)

  return make_str(st_arr)

