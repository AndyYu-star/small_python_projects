import random
import math

"""
Puzzle prompt:
This is a game where two players share a bar of chocolate. But there's a twist – one
of the pieces of chocolate is poisoned!
The chocolate bar is a rectangle (or a square) with m rows and n columns of chocolate
squares and both players know where the poisoned piece is when the game starts.
The players take it in turns to break the chocolate either vertically or horizontally
into two pieces and eat the safe side, until the only piece left is the poisoned square.
The loser is the player whose turn it is to go when there's only the poisoned square
left.

The question is: a chocolate bar with certain dimensions and a certain poisoned piece
is chosen. You are given the option to decide whether to play first or second. How
do you decide? (assuming you want to win)

I noticed that, if for each bar state we make an array of 'dists' - distances between
the poisoned piece and each edge of the bar - then each move a player makes is
equivalent to decreasing exactly one of these dists to a lower dist (that's at least 0).
E.g. a 10x11 rectangle with (0,0) as the lower-left corner piece and the poisoned piece
being at (3,2), will have dists of 2, 3, 6 and 8.
The goal of the game then is to be the player to reduce the state of dists down to
[0, 0, 0, 0].
Notice that the order of the dists no longer matters - only their values.

Of course, we're assuming both playes play optimally.
If there are an even, non-zero number of pairs of equal dists, then the second player
can always win, as whichever dist the first player reduces, the second player can reduce
the other dist in the pair by the same amount to arrive at a similar position.
E.g. if player 1 makes a move from [2, 2, 5, 5] to [2, 2, 3, 5], player 2 should make
the move to obtain [2, 2, 3, 3].
E.g. if player 1 makes a move from [4, 4, 4, 4] to [1, 4, 4, 4], player 2 should make
the move to obtain [1, 1, 4, 4].
As at every turn some dist is being reduced, eventually this must end in the second
player reducing the dists down to [0, 0, 0, 0], and winning.

If there are an odd number of pairs of equal dists, then the first player can win by
reducing a dist that isn't in a pair in order to reach a state where there are an even
number of pairs of equal dists.
E.g. if the bar state is [2, 5, 5, 6], player 1 should make the move to reach
[2, 2, 5, 5]. Then, by the earlier explanation, player 2 must now lose.
E.g. if the bar state is [3, 3, 3, 7], player 1 should make the move to reach
[3, 3, 3, 3], making player 2 lose.

If there are no pairs of equal dists however, then this question becomes very
complicated, which is what this code is written for.
"""

"""
loss = [] #this array first contains every possible non-obvious state

MAX_DIST = 32
for a in range(0, MAX_DIST):
    for b in range(a+1, MAX_DIST):
        for c in range(b+1, MAX_DIST):
            for d in range(c+1, MAX_DIST):
                loss.append([a, b, c, d]) #this array will always be sorted

#states in loss are checked and removed when they should be
i = 0
while i < len(loss):
    j = 0
    won = False
    while j < i and not won:
        #below if statement checks if only 1 of the dists is different, with the other
        #dist in the substate being lower than the dist in the original case
        if (len(set(loss[i]) - set(loss[j])) == 1 and
            list(set(loss[i]) - set(loss[j]))[0] >
            list(set(loss[j]) - set(loss[i]))[0]):
            
            won = True
            del loss[i]
        else:
            j += 1
    if not won:
        i += 1

for state in loss:
    print(state)
"""

"""
By examining the outputs of the above (commented out) code very closely, I figured out a
strategy!
Simply take all of the dists and bitwise XOR them all together. If the result is 0, the
player will lose. Otherwise the first player will win.
Call the result of bitwise XOR'ing all the dists in a certain bar state the 'value' of
the state. If a state has value 0, then whatever move the next player makes, it will
change the state's
value to something greater than 0, since a player can only change one dist in a single
turn. If the current bar state is not 0, then the next player can make a move that
forces the value to become 0 again. This player should bitwise XOR the value of the
current state with one of its dists. If the result is less than the dist, that is the
new dist of the new state.
E.g. the bar state with dists [2, 6, 7, 9] has value 10. 2 XOR 10, 6 XOR 10 and 7 XOR 10
are greater than 2, 6 and 7 respectively, but 9 XOR 10 is 3 which is less than 9.
Therefore the next player should make the move obtaining dists of [2, 3, 6, 7], which
indeed has a value of 0.
This works because XOR is commutative, associative and has the property that any number
XOR'ed with itself outputs 0. So (2 XOR 6 XOR 7 XOR 9) XOR 10 = 0, and since
9 XOR 10 = 3, 2 XOR 6 XOR 7 XOR 3 = 0.
It is guaranteed that one of the dists, when XOR'ed with the value, will output a
smaller number (if the value is non-zero). Whatever the most significant bit of the
value is, it will be present in at least 1 of the dists since otherwise that bit would
be a 0 after the XOR operations. XOR'ing the value with a dist that includes that bit
will turn the bit into a 0, so the result would have to be less than that dist.

"""


#a 'move' is written as a char corresponding to the direction of the move, followed
#by the number of squares cut off in that direction
#(e.g. 'd8' means 8 rows are chopped off from the bottom (down) of the chocolate bar)

def draw_bar(w, h, coords):
    if type(coords[0]) is list:
        choco_array = []
        for i in range(h):
            choco_row = [" "]*w
            choco_array.append(choco_row)
        for coord in coords:
            if h-1-coord[1] >= 0 and 1+coord[1] > 0 and coord[0] >= 0 and coord[0] < w:
                choco_array[h-1-coord[1]][coord[0]] = "x"
        print()
        for choco_row in choco_array:
            print((2*w+1)*"-")
            for choco_square in choco_row:
                print("|"+choco_square,end="")
            print("|")
        print((2*w+1)*"-")
        print("The bar is "+str(w)+"x"+str(h)+" and the pieces are at positions", *coords, "(0-indexed).")
    else:
        print()
        for i in range(h):
            print((2*w+1)*"-")
            if h-i == coords[1]:
                print("| "*(coords[0]-1)+"|X"+"| "*(w-coords[0])+"|")
            else:
                print("| "*w+"|")
        print((2*w+1)*"-")
        print("The bar is "+str(dims[0])+"x"+str(dims[1])+" and the piece is at position ("+str(coords[0]-1)+","+str(coords[1]-1)+"). (0-indexed)")

def validate_move(move):
    if len(move) >= 2:
        if (move[0] == 'r' or move[0] == 'u' or move[0] == 't' or
            move[0] == 'l' or move[0] == 'd' or move[0] == 'b'):
            return move[1:].isnumeric()
    return False

def make_move(dims, ppiece, move):
    if move[0] == 'r':
        dims[0] -= int(move[1:])
    elif move[0] == 'u' or move[0] == 't':
        dims[1] -= int(move[1:])
    elif move[0] == 'l':
        dims[0] -= int(move[1:])
        if type(ppiece[0]) is list:
            for coords in ppiece:
                coords[0] -= int(move[1:])
        else:
            ppiece[0] -= int(move[1:])
    elif move[0] == 'd' or move[0] == 'b':
        dims[1] -= int(move[1:])
        if type(ppiece[0]) is list:
            for coords in ppiece:
                coords[1] -= int(move[1:])
        else:
            ppiece[1] -= int(move[1:])
    else:
        assert False #this should never be reached

def make_turn(dims, coords):
    if type(coords[0]) is list:
        leftest = dims[0]-1
        rightest = 0
        highest = 0
        lowest = dims[0]-1

        for ppiece in coords: #finds the bounding box of all the poisoned squares
            if ppiece[0] < leftest:
                leftest = ppiece[0]
            if ppiece[0] > rightest:
                rightest = ppiece[0]
            if ppiece[1] > highest:
                highest = ppiece[1]
            if ppiece[1] < lowest:
                lowest = ppiece[1]
        move = decide_move(dims[0]-1-rightest, dims[1]-1-highest, leftest, lowest)
    else:
        move = decide_move(dims[0]-ppiece[0], dims[1]-ppiece[1], ppiece[0]-1, ppiece[1]-1)
        
    make_move(dims, coords, move)

def decide_move(rdist, udist, ldist, ddist):
    dists = [rdist, udist, ldist, ddist]
    value = dists[0] ^ dists[1] ^ dists[2] ^ dists[3]
    dirs = ['r', 'u', 'l', 'd']
    
    if value == 0:
        for i in range(3, -1, -1):
            #deletes all dists equal to 0
            if dists[i] == 0:
                del dists[i]
                del dirs[i]
        #makes a random move in a random direction
        rn_dir = random.randint(0,len(dirs)-1)
        return dirs[rn_dir] + str(random.randint(1,dists[rn_dir]))
    else:
        i = 0
        while i < len(dists):
            #for the new dist to be smaller than the old dist, the old dist has
            #to include the most significant bit of 'value'
            if dists[i] & (2**int(math.log(value, 2))) != 0:
                return dirs[i] + str(dists[i] - (value ^ dists[i]))
            i += 1
        assert False #this should never be reached
        
def is_win(dims, coords):
    if type(coords[0]) is list:
        leftest = dims[0]-1
        rightest = 0
        highest = 0
        lowest = dims[0]-1

        for ppiece in coords: #checks if the bounding box of the poisoned squares takes up the whole bar
            if ppiece[0] < leftest:
                leftest = ppiece[0]
            if ppiece[0] > rightest:
                rightest = ppiece[0]
            if ppiece[1] > highest:
                highest = ppiece[1]
            if ppiece[1] < lowest:
                lowest = ppiece[1]
        return (leftest == 0 and rightest == dims[0]-1 and highest == dims[1]-1 and lowest == 0)
    else:
        return (dims[0] == 1 and dims[1] == 1)

MAX_DIST = 10

num_poison = input("Enter the number of poisoned squares you want the chocolate bar to have. (a standard game has just 1.)")
if num_poison.isnumeric(): #TODO test properly
    num_poison = int(num_poison)
    if num_poison == 0:
        print("Nice try. I'll make 1 square poisoned.")
else:
    print("That is not a positive integer, so I'll just assume you want 1.")
    num_poison = 1

dims = [random.randint(1,MAX_DIST), random.randint(1,MAX_DIST)]

if num_poison == 1:
    ppiece = [random.randint(1,dims[0]), random.randint(1,dims[1])]
else:
    ppiece = []
    if dims[0]*dims[1] <= num_poison:
        dims[0] = MAX_DIST
        dims[1] = num_poison // MAX_DIST + 1
        
    temp_list = random.sample(range(dims[0]*dims[1]), num_poison)
    for item in temp_list:
        coords = [item // dims[1], item % dims[1]]
        ppiece.append(coords)
    
draw_bar(dims[0], dims[1], ppiece)

game_over = False


turn_order = input("Do you want to be the 1st or 2nd player? (Enter '1' for 1st, anything else for 2nd.)")
if turn_order != "1":
    turn_order = "2"

    if is_win(dims, ppiece):
        game_over = True
        print("You won!... without doing anything. *slow clap*")

    if not game_over:
        print("My turn! The chocolate bar now looks like this:")

        make_turn(dims, ppiece)

        draw_bar(dims[0], dims[1], ppiece)

    
while not game_over:

    if is_win(dims, ppiece):
        game_over = True
        print("I won!")
        
    if not game_over:
        move = input("""Your turn! Type in a move, which is a single char followed by the number of squares in that direction you want to cut the bar by.
E.g. 'r6' would remove 6 columns from the right, while 'd2'/'b2' would remove 2 rows from the bottom (down).\n""").lower()
        while not validate_move(move):
            move = input("Invalid move! Enter a valid move. \n")

        make_move(dims, ppiece, move)
        print("The chocolate bar now looks like this:")

        draw_bar(dims[0], dims[1], ppiece)

        if is_win(dims, ppiece):
            game_over = True
            print("You won!")
        elif type(ppiece[0]) is list:
            poison_ate = False
            i = 0
            while i < len(ppiece) and not poison_ate:
                if (ppiece[i][0] < 0 or ppiece[i][0] >= dims[0] or
                    ppiece[i][1] < 0 or ppiece[i][1] >= dims[1]):
                    poison_ate = True
                    game_over = True
                    print("""Uhh, you just ate a poisoned piece. I mean I'll take the win, but you could've tried to keep going until the end.
If you did that you wouldn't even have to eat the poisoned chocolate - I would've just said I won and that's it. Now you're probably gonna die a painful death just because you gave up early to a game of chocolate.""")
            
                i += 1
        else:
            if (ppiece[0] < 0 or ppiece[0] >= dims[0] or
                ppiece[1] < 0 or ppiece[1] >= dims[1]):
                game_over = True
                print("""Uhh, you just ate the poisoned piece. I mean I'll take the win, but you could've tried to keep going until the end.
If you did that you wouldn't even have to eat the poisoned chocolate - I would've just said I won and that's it. Now you're probably gonna die a painful death just because you gave up early to a game of chocolate.""")

        if not game_over:
            print("My turn! The chocolate bar now looks like this:")
    
            make_turn(dims, ppiece)

            draw_bar(dims[0], dims[1], ppiece)

#TODO - make imperfect player, then allow user to input a bar size & poison position
