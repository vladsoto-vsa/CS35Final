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
    def won(self):
        self.wins + self.wins + 1
    def lost(self):
        self.losses = self.losses + 1
    def winPct(self):
        return self.wins/(self.wins+self.losses)

def main():
    t = Team("Swarthmore ICPC", "programming")
    print(t)
    t.addPlayer("Xoe")
    t.addPlayer("Andrew")
    t.addPlayer("Isaac")
    t.addPlayer("Lydia")
    print(t.getRoster())

main()
