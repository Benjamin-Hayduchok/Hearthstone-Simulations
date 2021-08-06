import datetime
from Player import Player
from Minion import Minion
from simulations_methods import combat_phase


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

    return player_1, player_2


if __name__ == "__main__":
    """
    Runs the program a set amount of times and records the stats of each outcome
    """
    stat_dict = {"p1": 0, "TIE": 0, "p2": 0}
    begin_time = datetime.datetime.now()
    iterations = 3_000
    for i in range(iterations):
        players = doit()
        result = combat_phase(players[0], players[1])
        print("Winner: " + result)
        stat_dict[result] += 1
    print(stat_dict)

    print("|")
    for result in stat_dict:
        print(result + ": " + str(round((stat_dict[result]/iterations * 100), 2)) + "% | ", end="")
    print()
    print(datetime.datetime.now() - begin_time)
