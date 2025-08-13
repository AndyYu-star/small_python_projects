import tkinter as tk

#speffz lettering scheme
edge_speffz = [["A","Q"],["B","M"],["C","I"],["D","E"],["L","F"],["J","P"],["T","N"],["R","H"],["U","K"],["V","O"],["W","S"],["X","G"]]
corner_speffz = [["A","R","E"],["B","N","Q"],["C","J","M"],["D","F","I"],["U","L","G"],["V","P","K"],["W","T","O"],["X","H","S"]]

#define moves, all of these involve shifting pieces to other pieces' positions
#and changing their orientation if needed
def r(number):
    for i in range(number):
        temp1 = edges[1]
        edges[1] = edges[5]
        edges[5] = edges[9]
        edges[9] = edges[6]
        edges[6] = temp1
        temp2 = corners[1]
        corners[1] = [corners[2][0],(corners[2][1]+1)%3]
        corners[2] = [corners[5][0],(corners[5][1]+2)%3]
        corners[5] = [corners[6][0],(corners[6][1]+1)%3]
        corners[6] = [temp2[0],(temp2[1]+2)%3]
def u(number):
    for i in range(number):
        temp1 = edges[1]
        edges[1] = edges[0]
        edges[0] = edges[3]
        edges[3] = edges[2]
        edges[2] = temp1
        temp2 = corners[1]
        corners[1] = corners[0]
        corners[0] = corners[3]
        corners[3] = corners[2]
        corners[2] = temp2
def f(number):
    for i in range(number):
        temp1 = edges[2]
        edges[2] = [edges[4][0],(edges[4][1]+1)%2]
        edges[4] = [edges[8][0],(edges[8][1]+1)%2]
        edges[8] = [edges[5][0],(edges[5][1]+1)%2]
        edges[5] = [temp1[0],(temp1[1]+1)%2]
        temp2 = corners[2]
        corners[2] = [corners[3][0],(corners[3][1]+1)%3]
        corners[3] = [corners[4][0],(corners[4][1]+2)%3]
        corners[4] = [corners[5][0],(corners[5][1]+1)%3]
        corners[5] = [temp2[0],(temp2[1]+2)%3]
def l(number):
    for i in range(number):
        temp1 = edges[3]
        edges[3] = edges[7]
        edges[7] = edges[11]
        edges[11] = edges[4]
        edges[4] = temp1
        temp2 = corners[0]
        corners[0] = [corners[7][0],(corners[7][1]+2)%3]
        corners[7] = [corners[4][0],(corners[4][1]+1)%3]
        corners[4] = [corners[3][0],(corners[3][1]+2)%3]
        corners[3] = [temp2[0],(temp2[1]+1)%3]
def d(number):
    for i in range(number):
        temp1 = edges[8]
        edges[8] = edges[11]
        edges[11] = edges[10]
        edges[10] = edges[9]
        edges[9] = temp1
        temp2 = corners[4]
        corners[4] = corners[7]
        corners[7] = corners[6]
        corners[6] = corners[5]
        corners[5] = temp2
def b(number):
    for i in range(number):
        temp1 = edges[0]
        edges[0] = [edges[6][0],(edges[6][1]+1)%2]
        edges[6] = [edges[10][0],(edges[10][1]+1)%2]
        edges[10] = [edges[7][0],(edges[7][1]+1)%2]
        edges[7] = [temp1[0],(temp1[1]+1)%2]
        temp2 = corners[0]
        corners[0] = [corners[1][0],(corners[1][1]+1)%3]
        corners[1] = [corners[6][0],(corners[6][1]+2)%3]
        corners[6] = [corners[7][0],(corners[7][1]+1)%3]
        corners[7] = [temp2[0],(temp2[1]+2)%3]
#regular moves are done according to the absolute positions of the pieces
#rotations, wide and slice moves are done according to the relative position of the cube, using orientation
def x(number):
    global orientation
    for i in range(number):
        temp = orientation["u"]
        orientation["u"] = orientation["f"]
        orientation["f"] = orientation["d"]
        orientation["d"] = orientation["b"]
        orientation["b"] = temp
def y(number):
    global orientation
    for i in range(number):
        temp = orientation["r"]
        orientation["r"] = orientation["b"]
        orientation["b"] = orientation["l"]
        orientation["l"] = orientation["f"]
        orientation["f"] = temp
def z(number):
    global orientation
    for i in range(number):
        temp = orientation["r"]
        orientation["r"] = orientation["u"]
        orientation["u"] = orientation["l"]
        orientation["l"] = orientation["d"]
        orientation["d"] = temp
def rw(number):
    global orientation
    eval(orientation["l"] + "(number)")
    x(number)
def uw(number):
    global orientation
    eval(orientation["d"] + "(number)")
    y(number)
def fw(number):
    global orientation
    eval(orientation["b"] + "(number)")
    z(number)
def lw(number):
    global orientation
    eval(orientation["r"] + "(number)")
    x(4-(number%4))
def dw(number):
    global orientation
    eval(orientation["u"] + "(number)")
    y(4-(number%4))
def bw(number):
    global orientation
    eval(orientation["f"] + "(number)")
    z(4-(number%4))
def m(number):
    global orientation
    rw(4-(number%4))
    eval(orientation["r"] + "(number)")
def e(number):
    global orientation
    uw(4-(number%4))
    eval(orientation["u"] + "(number)")
def s(number):
    global orientation
    bw(4-(number%4))
    eval(orientation["b"] + "(number)")

#functions for getting the bld memo letter sequences for a given scramble
def edge_memo(buffer, flip):
    result = ""
    cycle_done = False
    solved = []
    global edges
    global eo
    global edge_speffz
    piece = edges[buffer]
    eo = flip
    for edge in edges:
        #checks if there are already any solved edges
        if edge[0] == edges.index(edge) and edge[1] == 0:
            solved.append(edge[0])
    while not cycle_done:
        #orients the edge if needed
        eo = (eo + piece[1]) % 2
        #doesn't do this if the buffer is already in place
        if piece[0] != edges.index(piece):
            #adds the letter corresponding to the edge + orientation to 'result'
            result = result + edge_speffz[piece[0]][eo]
            #the piece the current one points to is set to be the next piece
            solved.append(piece[0])
            piece = edges[piece[0]]
        if piece[0] == buffer:
            solved.append(buffer)
            cycle_done = True
    #checks if all pieces are solved
    if set(solved) == set(range(12)):
        return result
    cycle_done = False
    while True:
        eo = 0
        for i in range(12):
            #picks a new piece to start the new cycle
            if i not in solved:
                new_buffer = i
                result = result + edge_speffz[new_buffer][0]
                piece = edges[new_buffer]
                break
        while not cycle_done:
            #does the same tracing thing as before
            eo = (eo + piece[1]) % 2
            if piece[0] != edges.index(piece):
                result = result + edge_speffz[piece[0]][eo]
                solved.append(piece[0])
                piece = edges[piece[0]]
            #checks if the piece returns to the original,
            #but now it factors in eo and actually writes it in result
            if piece[0] == new_buffer:
                solved.append(new_buffer)
                if new_buffer != edges.index(piece):
                    eo = (eo + piece[1]) % 2
                result = result + edge_speffz[new_buffer][eo]
                cycle_done = True
        #checks if it's solved, restarts if not
        if set(solved) == set(range(12)):
            return result
        cycle_done = False
        
def corner_memo(buffer, twist):
    result = ""
    cycle_done = False
    solved = []
    global corners
    global co
    global corner_speffz
    piece = corners[buffer]
    co = twist
    for corner in corners:
        if corner[0] == corners.index(corner) and corner[1] == 0:
            solved.append(corner[0])
    while not cycle_done:
        co = (co + piece[1]) % 3
        if piece[0] != corners.index(piece):
            result = result + corner_speffz[piece[0]][co]
            solved.append(piece[0])
            piece = corners[piece[0]]
        if piece[0] == buffer:
            solved.append(buffer)
            cycle_done = True
    if set(solved) == set(range(8)):
        return result
    cycle_done = False
    while True:
        co = 0
        for i in range(8):
            if i not in solved:
                new_buffer = i
                result = result + corner_speffz[new_buffer][0]
                piece = corners[new_buffer]
                break
        while not cycle_done:
            co = (co + piece[1]) % 3
            if piece[0] != corners.index(piece):
                result = result + corner_speffz[piece[0]][co]
                solved.append(piece[0])
                piece = corners[piece[0]]
            if piece[0] == new_buffer:
                solved.append(new_buffer)
                if new_buffer != corners.index(piece):
                    co = (co + piece[1]) % 3
                result = result + corner_speffz[new_buffer][co]
                cycle_done = True
        if set(solved) == set(range(8)):
            return result
        cycle_done = False
        
#draws the current state of the cube
#window = tk.Tk()
#c = tk.Canvas(window, width=1000, height=500)
#t = tk.Label(text="Uh... debug")
#c.pack()
#t.pack()
#c.create_rectangle(10,10,40,50)
#window.update()
        
#asks user for input
ebuffer_speffz = input("Enter the edge buffer you use (in Speffz lettering scheme).").upper()
cbuffer_speffz = input("Enter the corner buffer you use (in Speffz lettering scheme).").upper()
edge_buffer = 2
edge_flip = 0
corner_buffer = 2
corner_twist = 0
#assigns the buffers
for i in range(len(edge_speffz)):
    if ebuffer_speffz in edge_speffz[i]:
        edge_buffer = i
        edge_twist = edge_speffz[i].index(ebuffer_speffz)
for i in range(len(corner_speffz)):
    if cbuffer_speffz in corner_speffz[i]:
        corner_buffer = i
        corner_twist = corner_speffz[i].index(cbuffer_speffz)
        
while True:
    #creates the solved cube
    edges = []
    for edge in range (12):
        edges.append([edge,0])
    corners = []
    for corner in range(8):
        corners.append([corner,0])
    orientation = { #dictionary stores the cube's current orientation
        "r": "r",
        "u": "u",
        "f": "f",
        "l": "l",
        "d": "d",
        "b": "b"
        }
    eo = 0
    co = 0
    moves = input("Enter a series of valid 3x3 moves. (please use w for wide moves)").split()
    for move in moves:
        #does the actual moves based on input
        move = move.lower()
        if move[0] in ["m", "e", "s", "x", "y", "z"]:
            #slice moves and rotations
            if len(move) < 2:
                eval(move + "(1)")
            elif move[1] == "2":
                eval(move[0] + "(2)")
            elif move[1] == "'":
                eval(move[0] + "(3)")
        else:
            #normal moves (which need to be converted based on orientation)
            if len(move) < 2:
                eval(orientation[move] + "(1)")
            elif move[1] == "w":
                #wide moves
                if len(move) == 2:
                    eval(move + "(1)")
                elif move[2] == "2":
                    eval(move[:2] + "(2)")
                elif move[2] == "'":
                    eval(move[:2] + "(3)")
            elif move[1] == "2":
                eval(orientation[move[0]] + "(2)")
            elif move[1] == "'":
                eval(orientation[move[0]] + "(3)")
    #prints the result (not readable)
    print("Edges:", edges)
    print("Corners:", corners)

    #finds and prints 3bld memo (readable)
    print("Edge memo:", edge_memo(edge_buffer, edge_twist))
    print("Corner memo:", corner_memo(corner_buffer, corner_twist))
