import random


def attack(minion_1, minion_2):
    """
    Simulates the attack of two minions and changes health and records death.

    :param minion_1: attacking minion
    :param minion_2: defending minion
    :return: Returns a list of dead minions
    """
    print(str(minion_1.name) + " attacked " + str(minion_2.name))
    minion_2.health -= minion_1.attack
    minion_1.health -= minion_2.attack

    # print(minion_1.health)
    # print(minion_2.health)

    dead_minions = []

    if minion_1.health <= 0:
        dead_minions.append("attacking")
    if minion_2.health <= 0:
        dead_minions.append("defending")

    # print(dead_minions)
    return dead_minions


def remove_dead_minions(attack_results,  attacker, defender, index_1, index_2):
    """
    Pops the dead minions from the players hand

    :param attack_results: list of result of attacking/defending minion deaths
    :param attacker: player who is attack so we can remove that minion
    :param defender: player who is defending so we can remove that minion
    :param index_1: index of where the attacking dead minion is
    :param index_2: index of where the defending dead minion is
    :return: returns nothing.
    """
    for result in attack_results:
        if result == "attacking":
            attacker.minion_list.pop(index_1)
        if result == "defending":
            defender.minion_list.pop(index_2)


def decide_first(player_1, player_2):
    """
    Simple RNG function to decide who attacks first

    :param player_1: First player
    :param player_2: Second player
    :return: Returns the players in the order of who goes first
    """

    rand_num = random.randint(0, 1)
    if rand_num == 0:
        first_player = player_1
        second_player = player_2
    else:
        first_player = player_2
        second_player = player_1
    # print('**DEBUG** PLAYER FIRST: ' + str(rand_num))
    return combat_phase(first_player, second_player)


def decide_winner(player):
    """
    Simply prints out the result of the winner, will likely remove later

    :param player:
    :return:
    """

    print("Winner: " + player + "\n")
    return player


def combat_over(player_1, player_2):
    """
    Checks if any player has a board of no minions left.

    :param player_1: Player who started first
    :param player_2: Player who started second
    :return: returns the name of the player who won, or if it is a TIE
    """

    if len(player_1.minion_list) == 0 and len(player_2.minion_list) != 0:
        return decide_winner(player_2.name)
    elif len(player_1.minion_list) != 0 and len(player_2.minion_list) == 0:
        return decide_winner(player_1.name)
    elif len(player_1.minion_list) == 0 and len(player_2.minion_list) == 0:
        return decide_winner("TIE")
    return "continue"


def setup_attack(count, attacker, defender):
    """
    Decides what defending minion will be attacked by the attacking minion

    :param count: Using index of currently attacking minion to find the minion in the attacker list
    :param attacker: Attacking player
    :param defender: Defending player
    :return: Returns the attacking & defending minions, as well as the defenders index in player hand
    """

    attacking_minion = attacker.minion_list[count]
    # Generate random number for the random minion defending
    rand_index = random.randint(0, len(defender.minion_list) - 1)
    defending_minion = defender.minion_list[rand_index]

    return [attacking_minion, defending_minion, rand_index]


def attack_sequence(player_1, player_2, count):
    """
    Small pilot function that calls other functions to completes an action sequence

    :param player_1: Player going first
    :param player_2: Player going second
    :param count: Index of current attacking minion
    :return: returns nothing.
    """

    # attack code
    fighting_minions = setup_attack(count, player_1, player_2)
    attack_results = attack(fighting_minions[0], fighting_minions[1])

    remove_dead_minions(attack_results, player_1, player_2, count, fighting_minions[2])


def combat_phase(player_1, player_2):
    """
    Pilot function that does the combat phase entirely of one fight

    :param player_1: Player going first
    :param player_2: Player going second
    :return: returns the name of the winner or of it's a TIE
    """

    # Need to make it so it checks if the game is over after an attack is made.
    count = -1
    while True:
        # MIGHT NEED TO UPDATE HOW TO WRAP THE COUNT HERE
        count += 1
        p1_count = count % len(player_1.minion_list)

        attack_sequence(player_1, player_2, p1_count)

        winner = combat_over(player_1, player_2)
        # print(winner)
        if not winner == "continue":
            return winner

        p2_count = count % len(player_2.minion_list)

        attack_sequence(player_2, player_1, p2_count)

        winner = combat_over(player_1, player_2)
        # print(winner)
        if not winner == "continue":
            return winner
