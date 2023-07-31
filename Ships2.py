"""
    Connor Ostrowski
    CIS 159-01
    Project 3 - Battle Ship Game
    Due 12/05/2022
    I certify that this work was done in accordance with GV academic honesty policies.

    Constructor Method for the Cruiser class
    Attributes:
        Health: Random number with limit of 300
        Shield: 0 - 100 <- Random Number
        Attack: 0 - 100 <- Random Number
"""

class Ships2:

    def __init__(self):
        self.name = 'default'
        self.health = 1000.0
        self.shield = 100.0
        self.attack = 0.0

    """returns the name of the ship if the set_name function is used or it will return default"""
    def get_name(self):
        return self.name

    """set name function receives an input new_name that sets the attributed of the class to that input"""
    def set_name(self, new_name):
        if new_name:
            self.name = new_name
            return self.name

    """printings and returns the health and shield"""
    def get_levels(self):
        #print(f'{self.name} has health of {self.health} and shield of {self.shield}')
        return [self.health, self.shield]

    """takes an input of list levels and sets self.health to levels[0] and self.shield to levels[1]
    If the random number is greater than 700 limit the health to 700 """
    def set_levels(self, levels):
        if levels[0] > 700:
            self.health = 700
            self.shield = levels[1]
            return [self.health, self.shield]
        else:
            self.health = levels[0]
            self.shield = levels[1]
            return [self.health, self.shield]

    """set_attack functions set the attack attribute of the class to the input of new_attack"""
    def set_attack(self, new_attack):
        if new_attack > 0.0 and new_attack < 101.0:
            self.attack = new_attack
            return self.attack

    """prints and returns the attribute of attack of the class spaceship"""
    def get_attack(self):
        #print(f'{self.name} has an attack level of {self.attack}')
        return self.attack

    """ACSII Art for a cruiser ship to print"""
    def cruiser_art(self):
        print('                                     # #  ( )')
        print('                                 ____#_#___|__')
        print('                         __      |____________|  ')
        print('                   =====| |      |            |  ')
        print('        =====| |     .-------------------------------.  | |====')
        print('<--------------------|                               |-------------/')
        print(' \\   CGN-11                                                       /')
        print('  \\______________________________________________________________/')

    """hit will calculated the damage done when the shield is at a certain level and will also decrease the amount of 
    health that the spaces ship will have. This changes the attributed self.shield and self.health
    hit function also has a nested function called miss_attack which if a 5 or 6 is passed in rolled argument of hit() then 
    nothing will happen to health and shield and if any other number then a shield or health will decrease. """

    def hit(self, other_ship, rolled):
        def miss_attack(rolled_hit):
            if (rolled_hit == 5) or (rolled_hit == 6):
                print(f'{self.name} missed and there was no affect')
                return [self.health, self.shield]

            if rolled_hit <= 4:

                """This while will check if the attack value entered was greater than zero"""
                while other_ship > 0.0:

                    """When the shield is greater than 75 reduce by 10% of other ships attack"""
                    if self.shield >= 75.0:
                        self.shield = self.shield - (other_ship * (.1))
                        return [self.health, self.shield]

                    """When the shield is greater than or equal to 50 and less 75 reduce shield by 20% of other ships attack"""
                    if self.shield < 75.0 and self.shield >= 50.0:
                        self.shield = self.shield - (other_ship * (.2))
                        return [self.health, self.shield]

                    """when the shield is less than 50 reduce the shield by %50 of the other ships attack"""
                    if self.shield < 50.0 and self.shield > 0.0:
                        self.shield = self.shield - (other_ship * (.5))
                        return [self.health, self.shield]

                    """Will print when the health is zero or less than zero which signal a destroyed ship"""
                    if self.shield <= 0.0:
                        while self.health > 0.0:
                            self.health = self.health - (other_ship * (.5))
                            if self.health < 0.0:
                                print(f'{self.name} has been destroyed')
                            return [self.health, self.shield]

        """miss_attack is called here to check for a 1 to miss the other ships attack"""
        miss_attack(rolled)


