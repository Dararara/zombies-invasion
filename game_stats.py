class GameStats():
    def __init__(self):

        self.game_active = False
        self.win = True

    def restart(self):
        self.score = 0
        self.gold = 5000
        self.life = 3
        self.zombie_number = 20
        self.buckethead_zombie_number = 10
        self.float_zombie_number = 10
        self.bullet_accumulate = 0
        self.zombie_accumulate = 0
        self.buckethead_zombie_accumulate = 0
        self.float_zombie_accumulate = 0
        self.level_2 = False
        self.level_3 = False
        self.total_zombies = self.zombie_number+self.buckethead_zombie_number+self.float_zombie_number
        self.happy_ending = False
