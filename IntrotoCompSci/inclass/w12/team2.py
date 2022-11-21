class Team(object):
    def __init__(self, name, team_type):
        self.name = name
        self.type = team_type
        self.roster = []
        self.wins = 0
        self.losses = 0
    def __str__(self):
        return "%s (%s) Wins: %d Losses: %d" % \
            (self.name, self.type, self.wins, self.losses)
    def addPlayer(self, player_name):
        self.roster.append(player_name)
    def getRoster(self):
        return self.roster
    def getWins(self):
        return self.wins
    def getLosses(self):
        return self.losses

    def won(self):
        self.wins = self.wins + 1
    def lost(self):
        self.losses = self.losses + 1

def main():
    t = Team("SwatCS", "ICPC")
    assert(t.getWins() == 0)
    assert(t.getLosses() == 0)
    assert(t.getName() == "SwatCS")
    t.wonGame()
    t.wonGame()
    t.lostGame()
    assert(t.getWins() == 2)
    assert(t.getLosses() == 1)
    print("Passed all unit testing!")

if __name__ == '__main__':
    main()

main()
