# Define the base class player.
class player:
  def play (self):
    print("The player is playing cricket.")
#Define the derived class batsman.
class Batsman(player):
  def play (self):
    print("The batsman is batting.")
#define the derived class bowler.          
class Bowler(player):
  def play (self):
    print("The bowler is bowling.")
#create oblets of batsman and bowler classes.          
batsman = Batsman()
bowler = Bowler()
#call the play() method for each object.
batsman.play()
bowler.play()
