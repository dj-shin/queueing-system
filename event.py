class Event():
    ARRIVAL = 'ARRIVAL'
    COMPLETE = 'COMPLETE'

    def __init__(self, type, occurenceTime):
        self.type = type
        self.occurenceTime = occurenceTime

    def __le__(self, other):
        return self.occurenceTime <= other.occurenceTime

    def __lt__(self, other):
        return self.occurenceTime < other.occurenceTime

    def __repr__(self):
        return '%s: %lf' % (self.type, self.occurenceTime)
