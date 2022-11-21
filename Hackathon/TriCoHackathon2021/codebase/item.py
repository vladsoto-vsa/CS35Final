class Item(object):
    def __init__(self, scenario, consq, exp, cfoot, consq_alt, exp_alt, cfoot_alt, tag, ptag):
        self.scenario = scenario
        self.consq = consq
        self.exp = exp
        self.cfoot = cfoot
        self.consq_alt = consq_alt
        self.exp_alt = exp_alt
        self.cfoot_alt = cfoot_alt
        self.tag = tag
        self.ptag = ptag
   
    def getScenario(self):
        return self.scenario
    def getConsq(self):
        return self.consq
    def getExp(self):
        return self.exp
    def getCarbonFoot(self):
        return self.cfoot
    def getConsqAlt(self):
        return self.consq_alt
    def getExpAlt(self):
        return self.exp_alt
    def getCarbonFootAlt(self):
        return self.cfoot_alt
    def getTag(self):
        return self.tag
    def getPTag(self):
        return self.ptag