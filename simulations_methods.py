import random

'''

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
        minion_1.setDeath()
        dead_minions.append("attacking")
    if minion_2.health <= 0:
        minion_2.setDeath()
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
    # print("len: " + str(len(attacker.minion_list)))
    # print("**DEBUG** COUNT: " + str(count))
    # print("**DEBUG** Minion List Length: " + str(len(attacker.minion_list)))

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

    # remove_dead_minions(attack_results, player_1, player_2, count, fighting_minions[2])


def reset_player_board(count, player, p2):
    for minion in player.minion_list:
        if minion.isDead:
            player.minion_list.remove(minion)

    # print("**DEBUG** COUNT: " + str(count))
    # print("**DEBUG** Minion List Length: " + str(len(player.minion_list)))

    winner = combat_over(player, p2)

    if not winner == "continue":
        return winner

    if len(player.minion_list) == 0:
        return 0

    count %= len(player.minion_list)
    return count


def player_attack(player_1, player_2, count):
    while count < len(player_1.minion_list) and player_1.minion_list[count].isDead:
        #print("skipped dead")
        count += 1

    if count >= len(player_1.minion_list):
        #print('here')
        count = reset_player_board(count, player_1, player_2)
        if isinstance(count, str) :
            return count

    attack_sequence(player_1, player_2, count)

    return combat_over(player_1, player_2)


def combat_phase(player_1, player_2):
    """
    Pilot function that does the combat phase entirely of one fight

    :param player_1: Player going first
    :param player_2: Player going second
    :return: returns the name of the winner or of it's a TIE
    """

    p1_count = -1
    p2_count = -1
    while True:
        # MIGHT NEED TO UPDATE HOW TO WRAP THE COUNT HERE
        p1_count += 1
        p2_count += 1
        # THIS IS WHERE I LEFT OFF, I ADDED THE NEW WAY OF CHECKING IF A MINION CAN ATTACK
        # I AM GOING TO INCREMENT THE COUNT IF THE MINION IS CURRENTLY DEAD

        # print("count before while: " + str(p1_count))

        # I AM GOING TO GO THROUGH THE ENTIRE LIST OF MINIONS, SKIPPING DEAD MINIONS, AND WHEN I GET TO THE END OF THE
        # LIST, I JUST DELETE THE MINIONS THAT DIED

        """
        while p1_count < len(player_1.minion_list) and player_1.minion_list[p1_count].isDead:
            print("skipped dead")
            p1_count += 1

        if p1_count >= len(player_1.minion_list):
            print('here')
            p1_count = reset_player_board(p1_count, player_1)

        attack_sequence(player_1, player_2, p1_count)
        """
        # player_attack(player_1, player_2, p1_count)

        winner = player_attack(player_1, player_2, p1_count)
        # print(winner)
        if not winner == "continue":
            return winner

        """
        while player_2.minion_list[p2_count].isDead:
            p2_count += 1
            # need this here because if the last minion is dead, it will increment and cause index out of bounds
            if p2_count > len(player_2.minion_list):
                break

        if p2_count > len(player_2.minion_list):
            p2_count = reset_player_board(p2_count, player_2)

        attack_sequence(player_2, player_1, p2_count)
        """

        winner = player_attack(player_2, player_1, p2_count)
        # print(winner)
        if not winner == "continue":
            return winner

'''


def print_board(player):
    print(player.name + "'s board: |", end="")
    for minion in player.minion_list:
        print(minion.name, end="|")
    print()


def remove_dead_minion(minion, player, isAttacking, defender_index):
    # print("**DEBUG** removing dead minion: " + minion.name)
    '''
    for i, o in enumerate(player.minion_list):
        if o.name == minion.name:
            del player.minion_list[i]
            break
    '''
    if isAttacking:
        player.minion_list.pop(0)
    else:
        player.minion_list.pop(defender_index)
    print_board(player)


def check_alive(minion, player, isAttacking, defender_index):
    if minion.health <= 0:
        print(minion.name + " died during combat")
        remove_dead_minion(minion, player, isAttacking, defender_index)
    else:
        # print(minion.name + " lived during combat")
        if isAttacking:
            temp = player.minion_list.pop(0)
            print(temp.name)
            player.minion_list.append(temp)
            print_board(player)


def attack(minion_1, attacker, minion_2, defender_index, defender):
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

    check_alive(minion_1, attacker, True, defender_index)
    check_alive(minion_2, defender, False, defender_index)


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
    return defender.minion_list[rand_index], rand_index


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
    defending_minion_values = get_defending_minion(defender)

    # print("**DEBUG** ATTACKING MINION: " + attacking_minion.name)
    # print("**DEBUG** DEFENDING MINION: " + defending_minion.name)

    attack(attacking_minion, attacker, defending_minion_values[0], defending_minion_values[1], defender)
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

