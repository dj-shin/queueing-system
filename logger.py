class Logger():
    def __init__(self):
        self.totalWaitingTime = 0.0
        self.totalJob = 0
        self.startTime = 0.0
        self.totalLoggingTime = 0.0
        self.timedSum = 0.0
        self.logging = False
        self.lastEventTime = 0.0

    def setLogging(self, logging, currentTime):
        if self.logging == logging: return
        self.logging = logging
        if logging:
            self.startTime = currentTime
            self.lastEventTime = currentTime
        else:
            self.totalLoggingTime += currentTime - self.startTime
        
    def arrival(self, length, currentTime):
        if self.logging:
            self.timedSum += length * (currentTime - self.lastEventTime)
        self.lastEventTime = currentTime

    def departure(self, length, currentTime, arrivalTime):
        if self.logging:
            self.timedSum += length * (currentTime - self.lastEventTime)
            self.totalWaitingTime += currentTime - arrivalTime
            self.totalJob += 1
        self.lastEventTime = currentTime

    def W(self):
        return self.totalWaitingTime / self.totalJob

    def L(self):
        return self.timedSum / self.totalLoggingTime
