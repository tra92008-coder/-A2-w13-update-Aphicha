import random
# lightout game 

ROWS = 5
COLS = 5
grid = [
    [0] * COLS,
    [0] * COLS,
    [0] * COLS,
    [0] * COLS,
    [0] * COLS
]
game_over = False
moves = 0
OFFSET_X = 150
OFFSET_Y = 150
SPACING = 100


def setup():
    size(700, 700)
    reset_game()


def reset_game():
    global grid, moves, game_over
    moves = 0
    game_over = False


def check_win():
    if not any(1 in row for row in grid):
        return True
    else:
        return False


def draw_bulb(cx, cy, is_on):
    if is_on:
        fill(255, 200, 0)
        noStroke()
        ellipse(cx, cy, 60, 60)
    else:
        fill(100, 100, 100)
        stroke(50)
        ellipse(cx, cy, 60, 60)


def draw_grid_recursive(r, c):
    if r >= ROWS:
        return
    else:
        cx = OFFSET_X + c * SPACING
        cy = OFFSET_Y + r * SPACING
        draw_bulb(cx, cy, grid[r][c] == 1)
        if c + 1 >= COLS:
            draw_grid_recursive(r + 1, 0)
        else:
            draw_grid_recursive(r, c + 1)


def draw():
    background(30)
    draw_grid_recursive(0, 0)


def flip(r, c):
    if 0 <= r < ROWS and 0 <= c < COLS:
        grid[r][c] = 1 - grid[r][c]


def toggle(r, c):
    global grid
    flip(r, c)
    flip(r - 1, c)
    flip(r + 1, c)
    flip(r, c - 1)
    flip(r, c + 1)


def mousePressed():
    global moves, game_over
    if game_over:
        return
    c = int(round((mouseX - OFFSET_X) / float(SPACING)))
    r = int(round((mouseY - OFFSET_Y) / float(SPACING)))
    if 0 <= r < ROWS and 0 <= c < COLS:
        moves += 1
        toggle(r, c)
        if check_win():
            game_over = True


def keyPressed():
    if key == 'r' or key == 'R':
        reset_game()