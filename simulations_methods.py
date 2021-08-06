import random


def print_board(player):
    print(player.name + "'s board: |", end="")
    for minion in player.minion_list:
        print(minion.name, end="|")
    print()


def remove_dead_minion(minion, player):
    # print("**DEBUG** removing dead minion: " + minion.name)
    for i, o in enumerate(player.minion_list):
        if o.name == minion.name:
            del player.minion_list[i]
            break
    print_board(player)


def check_alive(minion, player, isAttacking):
    if minion.health <= 0:
        print(minion.name + " died during combat")
        remove_dead_minion(minion, player)
    else:
        # print(minion.name + " lived during combat")
        if isAttacking:
            temp = player.minion_list.pop(0)
            print(temp.name)
            player.minion_list.append(temp)
            print_board(player)


def attack(minion_1, attacker, minion_2, defender):
    """
    Simulates the attack of two minions and changes health and records death.

    :param minion_1: attacking minion
    :param minion_2: defending minion
    :return: Returns a list of dead minions
    """
    print(">>>" + str(minion_1.name) + " attacked " + str(minion_2.name))
    minion_2.health -= minion_1.attack
    minion_1.health -= minion_2.attack

    # print("**DEBUG Health of " + minion_1.name + ": " + str(minion_1.health))
    # print("**DEBUG Health of " + minion_1.name + ": " + str(minion_2.health))

    check_alive(minion_1, attacker, True)
    check_alive(minion_2, defender, False)


def decide_first(player1, player2):
    """
        Simple RNG function to decide who attacks first

        :param player1: First player
        :param player2: Second player
        :return: Returns the players in the order of who goes first
        """

    rand_num = random.randint(0, 1)
    if rand_num == 0:
        first_player = player1
        second_player = player2
    else:
        first_player = player2
        second_player = player1
    # print('**DEBUG** PLAYER FIRST: ' + str(rand_num))
    return first_player, second_player


def get_defending_minion(defender):
    # print("**DEBUG** Getting defending minion for defender: " + defender.name)
    # Generate random number for the random minion defending
    rand_index = random.randint(0, len(defender.minion_list) - 1)
    return defender.minion_list[rand_index]


def check_winner(attacker, defender):
    """
    Checks if any player has a board of no minions left.

    :param player_1: Player who started first
    :param player_2: Player who started second
    :return: returns the name of the player who won, or if it is a TIE
    """

    if len(attacker.minion_list) == 0 and len(defender.minion_list) != 0:
        return defender.name
    elif len(attacker.minion_list) != 0 and len(defender.minion_list) == 0:
        return attacker.name
    elif len(attacker.minion_list) == 0 and len(defender.minion_list) == 0:
        return "TIE"
    return "continue"


def attack_sequence(attacker, defender):
    # print("**DEBUG** Attack sequence for attacker: " + attacker.name)
    # Attacking minion//It should always be the next in queue, aka left most, aka index 0
    attacking_minion = attacker.minion_list[0]  # may want to make this pop in the future
    # Defender minion
    defending_minion = get_defending_minion(defender)

    # print("**DEBUG** ATTACKING MINION: " + attacking_minion.name)
    # print("**DEBUG** DEFENDING MINION: " + defending_minion.name)

    attack(attacking_minion, attacker, defending_minion, defender)
    return check_winner(attacker, defender)


def combat_phase(player1, player2):
    # print("**DEBUG** combat phase started")
    # Getting the first and second players in order
    player_tuple = decide_first(player1, player2)
    first = player_tuple[0]
    second = player_tuple[1]
    print_board(first)
    print_board(second)
    while True:
        # First player going
        result = attack_sequence(first, second)
        if result != "continue":
            return result

        # Second player going
        result = attack_sequence(second, first)
        if result != "continue":
            return result

        # break  # Temp break statement only run 1 instance

def requeue(minion, player):
    print(str(minion) + " has been re-queued.")

