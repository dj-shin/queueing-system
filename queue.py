import math
from job import Job
from logger import Logger


class Queue(Logger):
    def __init__(self, k):
        Logger.__init__(self)
        self.k = k
        self.list = []

    def push(self, job, currentTime):
        self.arrival(len(self.list), currentTime)
        self.list.append(job)

    def pop(self, currentTime):
        length = len(self.list)
        job = self.list.pop(0)
        self.departure(length, currentTime, job.arrivalTime)
        return job

    def empty(self):
        return len(self.list) == 0

    def __repr__(self):
        return 'Queue(%d): %s' % (len(self.list), str(self.list))
