class Goomba:
    def __init__(self):
          self.lives = 1 # Goomba goes away after being hit.
          self.health = 1 # Can be defeated in 1 hit
          self.is_hit = False # Goomba determines if it has been hit
class BrickBlock:
    def __init__(self):
          self.strength = 2 # can only be broken if Mario is "Big"
          self.hits = 1 # Can be broken if hit once
          self.color = "Brown" # Makes the color of the brick brown
class Player:
    def __init__(self):
          self.alive = True # Player is alive
          self.coins = 0 # Player starts with 0 coins
          self.is_small = True # Player starts small