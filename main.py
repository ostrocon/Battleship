"""
    Connor Ostrowski
    CIS 159-01
    Project 3 - Battle Ship Game
    Due 12/05/2022
    I certify that this work was done in accordance with GV academic honesty policies.

    This is the main runs a game of two spaceships that battle
    Check the heading of each .py of Ships for more information on each type of ship
"""

import Ships, Ships2, Ships3, random, time

def main():
    print("             This game has 3 classes of ships you can choose: Battleship, Cruiser, or Destroyer")
    print("              Battleships have a max of 1000 health but also the highest chance of being hit")
    print("             Cruisers have a max of 700 health but have less chance of being hit")
    print("             Destroyers have a max of 300 health and have the smallest chance of being hit")

    """Time library imported to wait 8 seconds"""
    time.sleep(8)

    global player2, player1
    user1 = input("Player 1 enter the name of the ship   ")
    print("Please choose 1 for a Battleship or 2 for Cruiser or 3 for destroyer")
    choice = int(input())


    user2 = input("Player 2 enter the name of the ship   ")
    print("Please choose 1 for a Battleship or 2 for Cruiser or 3 for destroyer")
    choice2 = int(input())

    """Sets the choice value of 1 2 3 to the corresponding class of ship"""
    """When choice is 1 select a Battleship Class """
    if choice == 1:
        player1 = Ships.Ships()
        player1.set_name(user1)
        player1.battleship_art()
    """When choice is 2 select s a Cruiser Class"""
    if choice == 2:
        player1 = Ships2.Ships2()
        player1.set_name(user1)
        player1.cruiser_art()
    """When choice is 3 select a Destroyer Class"""
    if choice == 3:
        player1 = Ships3.Ships3()
        player1.set_name(user1)
        player1.destroyer_art()

    time.sleep(3)

    """Sets the choice2 value of 1 2 3 to the corresponding class of ship"""
    """When choice2 is 1 select a Battleship Class """
    if choice2 == 1:
        player2 = Ships.Ships()
        player2.set_name(user2)
        player2.battleship_art()
    """When choice2 is 2 select s a Cruiser Class"""
    if choice2 == 2:
        player2 = Ships2.Ships2()
        player2.set_name(user2)
        player2.cruiser_art()
    """When choice2 is 3 select a Destroyer Class"""
    if choice2 == 3:
        player2 = Ships3.Ships3()
        player2.set_name(user2)
        player2.destroyer_art()

    time.sleep(3)

    """import random library to assign a random value to health, shield, and attack level for player 1"""
    pla1health = random.randrange(0, 1000, 2)
    pla1shield = random.randrange(0, 100, 2)
    pla1attack = random.randrange(0, 100, 2)
    """Set these values"""
    lvls1 = [pla1health, pla1shield]
    player1.set_levels(lvls1)
    player1.set_attack(pla1attack)

    """import random library to assign a random value to health, shield, and attack level for player 2"""
    pla2health = random.randrange(0, 1000, 2)
    pla2shield = random.randrange(0, 100, 2)
    pla2attack = random.randrange(0, 100, 2)
    """Set these values"""
    lvls2 = [pla2health, pla2shield]
    player2.set_levels(lvls2)
    player2.set_attack(pla2attack)

    """status is used to get the health and shield of each ship"""
    status1 = player1.get_levels()
    status2 = player2.get_levels()

    """While the health of ship 1 or ship 2 is greater than zero """
    while (status1[0] >= 0.0) or (status2[0] >= 0.0):

        print()
        """Random roll for player 1"""
        num_rolled = random.randrange(1, 7)
        print('Player 1 random rolled number is:', num_rolled)

        """Random roll for player 2"""
        num_rolled2 = random.randrange(1, 7)
        print('Player 2 random rolled number is:', num_rolled2)

        print('Health and Shield levels are:')
        print(player1.get_levels())
        print(player2.get_levels())

        """Hit player 1 with the attack level of player 2 and check the number rolled by player 1"""
        player1.hit(player2.get_attack(), num_rolled)
        """Hit player 2 with the attack level of player 1 and check the number rolled by player 2"""
        player2.hit(player1.get_attack(), num_rolled2)

        """If either of the ships health get below the game will end and break will execute"""
        if player1.get_levels()[0] <= 0.0:
            print()
            print("THE GAME HAS ENDED")
            print('Player 2 has won the game\n')
            break

        if player2.get_levels()[0] <= 0.0:
            print()
            print('THE GAME HAS ENEDED')
            print('Player 1 has won the game\n')
            break

        else:
            status1 = player1.get_levels()
            status2 = player2.get_levels()
            """Wait 2 seconds"""
            time.sleep(2)

    return status1, status2


if __name__ == "__main__":
    """while loop to re run the game"""
    while True:
        main()
