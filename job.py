class Job():
    def __init__(self, arrivalTime):
        self.arrivalTime = arrivalTime

    def __repr__(self):
        return 'Job: %lf' % self.arrivalTime
