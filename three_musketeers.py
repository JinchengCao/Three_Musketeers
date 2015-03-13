# The Three Musketeers Game
# by <Jincheng Cao and Siyang Shu>.

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

import random
def create_board():
    global board
    """Creates the initial Three Musketeers board. 'M' represents
    a Musketeer, 'R' represents one of Cardinal Richleau's men,
    and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board
 
def string_to_location(s):
    """Given a two-character string (such as 'A5') return the designated
       location as a 2-tuple (such as (0, 4))."""
    assert s[0] >= 'A' and s[0] <= 'E'
    assert s[1] >= '1' and s[1] <= '5'
    #Return an integer representing the Unicode code of the character s[0]-65.
    #Return an integer which is int(s[1]) - 1 to fit the coordinate on the board.
    location = (ord(s[0]) - 65, int(s[1]) - 1) 
    return location

def location_to_string(location):
    """Return the string representation of a location."""
    assert location[0] >= 0 and location[0] <= 4
    assert location[1] >= 0 and location[1] <= 4
    #Return a string representing the coordinate on the board.
    s = chr(location[0]+65)+ str(location[1]+1)
    return s

def at(location):
    """Returns the contents of the board at the given location."""
    #Return either 'M', 'R' or '-'
    return board[location[0]][location[1]]

def all_locations():
    loc = []
    for i in range(0, 5):
        for j in range(0, 5):
            #Concatenate the list with each location on the board to generate all locations on the board.
            loc = loc + [(i, j), ]
    return loc
    """Returns a list of all 25 locations on the board."""

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board."""
    (row, column) = location
    assert row >= 0 and row <= 4
    assert column >= 0 and column <=4
    #Return the new location based on given direction.
    if direction == 'up':
        row = row - 1
    if direction == 'down':
        row = row + 1
    if direction == 'left':
        column = column - 1
    if direction == 'right':
        column = column + 1
    return (row, column)

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction."""
    assert at(location) == 'M'
    #'M' can only move to 'R', and the new location should be on 5x5 board.
    return at(adjacent_location(location, direction)) == 'R' and is_legal_location(adjacent_location(location, direction))

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction."""
    assert at(location) == 'R'
    #'R' can only move to '-', and the new location should be on 5x5 board.
    return at(adjacent_location(location, direction)) == '-' and is_legal_location(adjacent_location(location, direction))

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction."""
    #To make sure the new location is on 5x5 board.
    if(is_legal_location(adjacent_location(location, direction)) == False):
        return False
    if at(location) == 'R':
        return at(adjacent_location(location, direction)) == '-'    # 'R' can only move to '-', 
    if at(location) == 'M':
        return at(adjacent_location(location, direction)) == 'R'    # 'M' can only move to 'R'
    if at(location) == '-':
        return False

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is."""
    #At each location, try every potential direction for "who" to see if there is a legal move
    for i in range(0, 5):
        for j in range(0, 5):
            if at((i, j)) != who:
                # If content at given location is not "who", just skip the following part.
                continue
            #The content at given location is "who"
            for direction in ['up', 'down', 'left', 'right']:
                if is_legal_move((i, j), direction):
                    return True
    return False

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, []."""
    if at(location) == '-':
        return[]
    #The content at given location is either 'M' or 'R'
    else:
        possible_directions = []
        for direction in ['up', 'down', 'left', 'right']:
            if is_legal_move(location,direction):
                #Concatenate all possible directions and put them into a list for content at certain location
                possible_directions = possible_directions + [direction]
        return possible_directions 

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available."""
    #If there are still possible moves at given location, the player can move
    return (possible_moves_from(location) != [])

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board."""
    return (location[0] >= 0 and location[0] <= 4 and location[1] >=0 and location[1] <= 4)

   
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board."""
    return is_legal_location(adjacent_location(location, direction))
  
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples."""
    #At each location, try every potential direction for player to form a tuple for all possible moves.
    every_possible_move = []
    for i in range(0, 5):
        for j in range(0, 5):
            if at((i,j)) == player:
                #Collect all possible moves from the possible_moves_from(location)
                for direction in possible_moves_from((i,j)):
                    every_possible_move.append(((i,j),direction))
    return every_possible_move                               

def make_move(location, direction):
    """Moves the piece in location in the indicated direction."""
    assert is_legal_move(location, direction)
    (row, column) = location    # move from
    (row_next, column_next) = adjacent_location(location, direction)   # move to
    b = get_board()
    #Cover the next location with the content from the old location.
    b[row_next][column_next] = b[row][column]
    #Empty the old location on the board.
    b[row][column] = '-'

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual."""
    moves = all_possible_moves_for(who)
    if moves != []:
    #Randomize a move from all possible moves for player
        i = random.randint(0,len(moves)-1)
        return moves[i]
    else:
        return ()

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    for i in range(0, 5):
        count_by_column = 0
        count_by_row = 0
        for j in range(0, 5):
            if at((i, j)) == 'M':
                count_by_column = count_by_column + 1    # find a Musketeer on the column
            if at((j, i)) == 'M':
                count_by_row = count_by_row + 1    # find a Musketeer on the row
        if count_by_column == 3 or count_by_row == 3:    # exactly find 3 Musketeers on one column/row
            return True
    return False

#---------- Communicating with the user ----------

def print_board():
    print "    1  2  3  4  5"
    print "  ---------------"
    ch = "A"
    for i in range(0, 5):
        print ch, "|",
        for j in range(0, 5):
            print board[i][j] + " ",
        print
        ch = chr(ord(ch) + 1)
    print

def print_instructions():
    print
    print """To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).

For convenience in typing, you may use lowercase letters."""
    print

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = raw_input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    

    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = raw_input("Your move? ").upper().replace(' ', '')
    if len(move) >= 3 and move[0] in 'ABCDE' and move[1] in '12345' and move[2] in 'LRUD':
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
        
    print "Illegal move--'" + move + "'"
    print_instructions()
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M' and is_legal_move(location, direction):
            make_move(location, direction)
            describe_move("Musketeer", location, direction)
        else:
            print "You can't move there!"
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R' and is_legal_move(location, direction):
            make_move(location, direction)
            describe_move("Enemy", location, direction)
        else:
            print "You can't move there!"
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n"

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print "Cardinal Richleau's men win!"
                break
        else:
            print "The Musketeers win!"
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print "The Musketeers win!"
            break
