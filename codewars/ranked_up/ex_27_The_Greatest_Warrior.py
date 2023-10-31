class Warrior:
    RANKS = [
        "Pushover", "Novice", "Fighter", "Warrior", "Veteran",
        "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"
    ]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []

    def battle(self, enemy_level):
        if not (1 <= enemy_level <= 100):
            return "Invalid level"

        level_difference =  self.level - enemy_level
        # print(level_difference)
        exp = 0

        if level_difference >= 2:
            return "You've been defeated"
        elif level_difference == 1:
            exp = 5
        elif level_difference == 0:
            exp = 10
        elif level_difference == -1:
            exp = 20 * level_difference ** 2

        self.experience += exp
        if self.experience >= 10000:
            self.experience = 10000
        self.update_level_and_rank()
        
        if level_difference >= 2:
            return "Easy fight"
        elif level_difference == 1 or level_difference == 0:
            return "A good fight"
        elif level_difference == -1:
            return "An intense fight"

    def update_level_and_rank(self):
        self.level = 1 + (self.experience - 100) // 100
        if self.level > 100:
            self.level = 100
        rank_index = (self.level - 1) // 10
        self.rank = self.RANKS[rank_index]

    def training(self, training_data):
        description, exp, min_level = training_data
        if self.level >= min_level:
            self.experience += exp
            self.achievements.append(description)
            self.update_level_and_rank()
            return description
        return "Not strong enough"




bruce_lee = Warrior()
print(bruce_lee.level)  # 1
print(bruce_lee.experience)  # 100
print(bruce_lee.rank)  # "Pushover"
print(bruce_lee.achievements)  # []

# Training
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))  # "Defeated Chuck Norris"
print(bruce_lee.experience)  # 9100
print(bruce_lee.level)  # 91
print(bruce_lee.rank)  # "Master"
print(bruce_lee.battle(90))  # "A good fight"
print(bruce_lee.experience)  # 9105
print(bruce_lee.achievements)  # ["Defeated Chuck Norris"]