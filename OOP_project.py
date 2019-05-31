# Section A:
# The OOP text based game I will be creating is blackjack. This game will allow at two players to play against each other. In the game the user will be dealt his cards initially, once these cards are dealt each player will be able to see their cards and either “hit” or “stay”. After this the players will be able to place their bets from their wallet. This will keep happening until both players select “stay” in which case both cards will be revealed and the winner will receive all of the money on the table. After each hand the players will be given an option to play the “last hand”. If players select “last hand” they will be able to play a normal hand or do “Winner Takes all” in which case whoever wins will get all of the money.  

# Success Criteria:
# The game has a deck of cards which excludes the joker
# The game will allow at least two players to play against each other 
# The game will be able to keep track of the hands dealt



import random

class Cards(object):

    # function to generate random numbers from 1 to 10
    def __init__(self):
        self.val = random.randrange(1, 12, 1)

    def hit(self):
        return self.val

class Player(object):

    def __init__(self):
        self.choice = 0
        self.score = 0
        self.total_won = 0

total_games, hitn = 0, 0
play = ""

print("WELCOME TO BLACKJACK!")

player_a = Player()
player_b = Player()

player_a.total_won = 0
player_b.total_won = 0

while(play != 'N'):

    player_a.score = 0
    player_b.score = 0

    play = input(
        'Do you want to play this game? (press "Y" to play or "N" to exit the game): ')

    if (play == 'N'):
        break

    if (play != 'Y'):

        while True:

            play = input(
                'Entered character is incorrect. Press "Y" to play or "N" to exit the game: ')

            if (play == 'Y' or play == 'N'):
                break

    if (play == 'N'):
        break

    # total number of games played are saved in this variable
    total_games += 1

    print("Enter 1 to hit and 0 to pass.")

    while True:
        # Turn of player A
        player_a.choice = input("Player A, do you want to hit or pass? ")

        # check that the user enters correct choice
        if (player_a.choice != '1' and player_a.choice != '0'):

            while True:

                player_a.choice = input(
                    "Entered choice is incorrect. Enter 1 to hit and 0 to pass. ")

                if (player_a.choice == '1' or player_a.choice == '0'):
                    break

        if (player_a.choice == '1'):

            card = Cards()
            hitn = card.hit()

            player_a.score = player_a.score + card.hit()

            # checking which user wins
            if (player_a.score == 21):

                print("Player A hits {hitn} and wins(score is 21)")
                player_a.total_won += 1

                break

            elif (player_a.score > 21):

                print(f"Player A hits {hitn} and loses(score exceeds 21)")
                player_b.total_won += 1

                break

            else:
                print("Player A hits ", hitn)

        # in case of a pass, this condition will run

        elif (player_a.choice == '0'):

            print("Player A passes.")

            # if both players pass, this condition will run
            if (player_a.choice == '0' and player_b.choice == '0'):

                if (player_a.score > player_b.score):

                    print(
                        "Both players passed, So Player A wins.(Player with the higher score wins.")
                    player_a.total_won += 1

                    break

                elif (player_b.score > player_a.score):

                    print(
                        "Both players passed, So Player B wins.(Player with the higher score wins.")
                    player_b.total_won += 1

                    break

                else:

                    print("Scores are equal. Player B passed first so Player B wins.")
                    player_b.total_won += 1

                    break

        # same is repeated with player B
        player_b.choice = input("Player B, do you want to hit or pass? ")

        # check that the user enters correct choice
        if (player_b.choice != '1' and player_b.choice != '0'):

            while True:

                player_a.choice = input(
                    "Entered choice is incorrect. Enter 1 to hit and 0 to pass. ")

                if (player_b.choice == '1' or player_b.choice == '0'):
                    break

        if (player_b.choice == '1'):

            card = Cards()
            hitn = card.hit()

            player_b.score = player_b.score + card.hit()

            # checking which user wins
            if (player_b.score == 21):

                print(f"Player B hits {hitn} and wins(score is 21)")
                player_b.total_won += 1

                break

            elif (player_b.score > 21):

                print(f"Player B hits {hitn} and loses(score exceeds 21)")
                player_a.total_won += 1

                break

            else:
                print("Player B hits ", hitn)

        # in case of a pass, this condition will run

        elif (player_b.choice == '0'):

            print("Player B passes.")
            # if both players pass, this condition will run
            if (player_a.choice == '0' and player_b.choice == '0'):

                if (player_a.score > player_b.score):

                    print(
                        "Both players passed, So Player A wins.(Player with the higher score wins.")
                    player_a.total_won += 1

                    break

                elif (player_b.score > player_a.score):

                    print(
                        "Both players passed, So Player B wins.(Player with the higher score wins.")
                    player_b.total_won += 1

                    break

                else:

                    print("Scores are equal. Player A passed first so Player A wins.")
                    player_a.total_won += 1

                    break

print(f"Out of {total_games} game(s), Player A won {player_a.total_won} game(s) and Player B won {player_b.total_won} game(s)!")

print("Thank you for playing Blackjack!")
