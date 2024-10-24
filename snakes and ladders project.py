import time
import random
print("WELCOME TO SNAKES AND LADDERS: REMASTERED EDITION!")
start = ""
#keeps asking the player to start until they start
while start != "start" and start != "Start":
 start = input("Start? (type start to start)")
#sets player count
player_count = int(input("How many players are there? Choose from 2 to 4."))
if player_count < 2 or player_count > 4:
 print("NOOOO! YOU PICKED A NUMBER OUTSIDE THE RANGE OF 2 TO 4 PLAYERS MEANING THAT THIS GAME CANNOT PROGRESS!!!")
 quit()
else:
 print("Very well.")
names = []
#adds the names to the names list
for i in range(player_count):
 names.append(input("Player " + str(i+1) + ", what's your name?"))
#starting the game
positions = []
for i in range(player_count):
 positions.append(1)
player_turn = 0
end_square = 50
#positions of default snakes and ladders
ladder_starts = [4,9,22,26,27,36,43]
ladder_ends = [22,13,40,31,43,49,45]
snake_starts = [15,19,30,33,39,44,46]
snake_ends = [7,2,17,29,23,36,3]
while True:
 #has a 10% chance of skipping the player's turn
 if random.randint(1,8) == 1:
   print("A random event has occured! " + names[player_turn] + ", your turn has been skipped!")
   player_turn = (player_turn + 1) % player_count
 #the \n skips the line so it makes an empty line to denote when a new turn has started
 print("\n" + names[player_turn] + ", you are on square " + str(positions[player_turn]) + ".")
 #has a 4% chance of switching the players' positions in any given turn (temp_switch_positions is there so that Player 1's position doesn't get lost)
 if random.randint(1,25) == 1:
   temp_switch_positions = positions[0]
   for i in range(player_count - 1):
     positions[i] = positions[i + 1]
   positions[len(positions) - 1] = temp_switch_positions
   print("A random event has occured! All players' positions have been switched!")
 #the 'input' is here to let the player press enter to roll the die
 input("Roll the die. (press enter)")
 print("Rolling the die...")
 #rolls the die
 dice = random.randint(1,6)
 #adds the result to the position of the player
 positions[player_turn] = positions[player_turn] + dice
 #waits 2 seconds
 time.sleep(2)
 print(names[player_turn] + ", you rolled a " + str(dice) + ". You are now on square " + str(positions[player_turn]) + ".")
 #has a 5% chance of randomly spawning a ladder, the if statement is to make sure the end of the ladder doesn't spawn too close to the beginning
 if random.randint(1,10) == 1:
   new_ladder = random.randint(5,42)
   ladder_starts.append(new_ladder)
   if new_ladder <= 13:
     ladder_ends.append(random.randint(14,48))
   else:
     ladder_ends.append(random.randint(new_ladder + 1,48))
   print("A random event has occured! A new random ladder has suddenly appeared!")
 #has a 5% chance of randomly spawning a snake, the if statement is to make sure the end of the snake doesn't spawn too close to the end
 if random.randint(1,10) == 1:
   new_snake = random.randint(16,45)
   snake_starts.append(new_snake)
   if new_snake >= 36:
     snake_ends.append(random.randint(3,35))
   else:
     snake_ends.append(random.randint(3,new_snake - 1))
   print("A random event has occured! A new random snake has suddenly appeared!")
 #moves the player up if the player's position is in the list of ladders
 if positions[player_turn] in ladder_starts:
   positions[player_turn] = ladder_ends[ladder_starts.index(positions[player_turn])]
   positions[player_turn]
   print("You reached a ladder! You are now on square " + str(positions[player_turn]) + ".")
 #moves the player down if the player's position is in the list of snakes
 if positions[player_turn] in snake_starts:
   positions[player_turn] = snake_ends[snake_starts.index(positions[player_turn])]
   positions[player_turn]
   print("You reached a snake! You are now on square " + str(positions[player_turn]) + ".")
 #has a 4% chance of moving the winning square to anywhere from 51 to 75
 if random.randint(1,20) == 1:
   end_square = random.randint(51,69)
   print("A random event has occured! The winning square has now been moved to Square " + str(end_square) + "!")
 #ends the game if the player reaches the winning square or above
 if positions[player_turn] >= end_square:
   print(names[player_turn] + ", you reached Square " + str(end_square) + " meaning you win!!!")
   quit()
 #has a 10% chance of giving the player an extra turn
 if random.randint(1,8) == 1:
   print("A random event has occured! " + names[player_turn] + ", you got an extra turn!")
   player_turn = (player_turn - 1) % player_count
 #adds 1 to the player_turn and then divides it by player_count to get the remainder (player_turn mustn't go above player_count)
 player_turn = (player_turn + 1) % player_count
