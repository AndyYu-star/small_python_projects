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

I noticed that, if for each bar state we make an array of 'dists' - distances between
the poisoned piece and each edge of the bar - then each move a player makes is
equivalent to decreasing exactly one of these dists to a lower dist (that's at least 0).
E.g. a 10x11 rectangle with (0,0) as the lower-left corner piece and the poisoned piece
being at (3,2), will have dists of 2, 3, 6 and 8.
The goal of the game then is to be the player to reduce the state of dists down to
[0, 0, 0, 0].
Notice that the order of the dists no longer matters - only their values.

If ... (to be written)
"""

win = []
loss = [] #this array first contains every possible non-obvious state

MAX_DIST = 20
for a in range(0, MAX_DIST):
    for b in range(a+1, MAX_DIST):
        for c in range(b+1, MAX_DIST):
            for d in range(c+1, MAX_DIST):
                loss.append([a, b, c, d]) #this array will always be sorted

#states in loss are checked and moved to win when they should be
i = 0
while i < len(loss):
    j = 0
    won = False
    while j < i and not won:
        #below if statement checks if exactly 3 of the dists match,
        #with the other dist in the substate being lower
        #than the corresponding dist in the original case
        if (int(loss[i][0] == loss[j][0]) + int(loss[i][1] == loss[j][1]) +
            int(loss[i][2] == loss[j][2]) + int(loss[i][3] == loss[j][3]) == 3 and
            loss[j][0]+loss[j][1]+loss[j][2]+loss[j][3] <
            loss[i][0]+loss[i][1]+loss[i][2]+loss[i][3]):
            
            win.append(loss[i]) #MAYBE REMOVE? since maybe no point to storing in win?
            won = True
            del loss[i]
        else:
            j += 1
    if not won:
        i += 1

for state in loss:
    print(state)

#TODO - use results to generalise to arbitrary MAX_DIST
#TODO - make perfect poisoned chocolate player
