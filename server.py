from logger import Logger


class Server(Logger):
    IDLE = 'IDLE'
    BUSY = 'BUSY'

    def __init__(self, state=IDLE):
        Logger.__init__(self)
        self.state = state
        self.jobStartTime = 0.0

    def __repr__(self):
        return 'Server: %s' % self.state

    def setState(self, state, currentTime):
        if state == Server.BUSY:
            if self.state == Server.BUSY:
                self.departure(1, currentTime, self.jobStartTime)
            self.arrival(1 if self.state == Server.BUSY else 0, currentTime)
            self.jobStartTime = currentTime
        elif state == Server.IDLE:
            self.departure(1 if self.state == Server.BUSY else 0, currentTime, self.jobStartTime)
        self.state = state
