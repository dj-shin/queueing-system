import random
import math
from dist import expntl
from event import Event
from queue import Queue
from server import Server
from job import Job


def timeDist(type):
    if type[0] == 'M':
        return lambda: expntl(1.0 / type[1])
    else:
        return None

class System():
    def __init__(self, A, B, c, k=math.inf):
        self.queue = Queue(k)
        self.arrival = timeDist(A)
        self.service = timeDist(B)
        self.server = Server()
        self.eventList = []

    def scheduleEvent(self, eventType, currentTime):
        if eventType == Event.ARRIVAL:
            ev = Event(Event.ARRIVAL, currentTime + self.arrival())
            self.eventList.append(ev)
            self.eventList.sort()
        elif eventType == Event.COMPLETE:
            ev = Event(Event.COMPLETE, currentTime + self.service())
            self.eventList.append(ev)
            self.eventList.sort()

    def handleEvent(self, ev):
        currentTime = ev.occurenceTime
        if ev.type == Event.ARRIVAL:
            self.scheduleEvent(Event.ARRIVAL, currentTime)
            if self.server.state == Server.BUSY:
                # Enters queue
                self.queue.push(Job(currentTime), currentTime)
            else:
                self.queue.totalJob += 1
                self.server.setState(Server.BUSY, currentTime)
                self.scheduleEvent(Event.COMPLETE, currentTime)
        elif ev.type == Event.COMPLETE:
            if self.queue.empty():
                self.server.setState(Server.IDLE, currentTime)
            else:
                # Get it from queue
                job = self.queue.pop(currentTime)
                self.server.setState(Server.BUSY, currentTime)
                self.scheduleEvent(Event.COMPLETE, currentTime)

    def run(self, stableTime, totalTime):
        self.scheduleEvent(Event.ARRIVAL, 0.0)

        while True:
            ev = self.eventList.pop(0)
            currentTime = ev.occurenceTime
            if currentTime > totalTime:
                self.server.setLogging(False, currentTime)
                self.queue.setLogging(False, currentTime)
                break
            if currentTime >= stableTime:
                self.server.setLogging(True, currentTime)
                self.queue.setLogging(True, currentTime)
            self.handleEvent(ev)
