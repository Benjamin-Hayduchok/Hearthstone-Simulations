from Player import Player
from Minion import Minion
from simulations_methods import decide_first


def doit():
    """
    Initializes the players minions and their hands
    :return: a list of both players
    """
    # Player 1
    murloc = Minion("murloc", 1, 1)
    mech = Minion("mech", 3, 1)
    king = Minion("king", 6, 2)
    baron = Minion("baron", 4, 3)
    tiny = Minion("tiny", 1, 8)
    queen = Minion("queen", 2, 3)
    player_1 = Player("p1", [murloc, mech, king, baron, tiny, queen])

    # Player 2
    tide_hunter = Minion("tide_hunter", 2, 1)
    dragon = Minion("dragon", 2, 3)
    evil = Minion("evil", 6, 1)
    divine = Minion("divine", 5, 2)
    trog = Minion("trog", 7, 6)
    cat = Minion("cat", 4, 2)
    player_2 = Player("p2", [tide_hunter, dragon, evil, divine, trog, cat])

    return [player_1, player_2]


if __name__ == "__main__":
    """
    Runs the program a thousand times and records the stats of each outcome
    """
    stat_dict = {}

    iterations = 10_000
    for i in range(iterations):
        players = doit()
        # should really change decide_first to combat
        winner = decide_first(players[0], players[1])
        if winner not in stat_dict:
            stat_dict[winner] = 1
        else:
            stat_dict[winner] += 1
    print(stat_dict)
    # print(player_1.minion_list[0].health)

    """
    =========================================================================================
    **BUG**: If a minion dies on the left of a minion which is about to attack,
    the minion that should be attacking next is moving into the slot that is considered 
    to have attacked already
        >> **POSSIBLE FIX**: Have a boolean value that checks if a minion attacks,
            and then reset the attack values when the % is triggered to cycle back around.
    =========================================================================================
    
    
    """
