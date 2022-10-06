from collections import deque

class HitCounter(object):
    #Complexity: O(n) time and O(n) space
    #All timestamps in increasing order => ignore the timestamps have difference >= 300

    def __init__(self):
        self.hitCounter = deque() #use a queue to store the number of hits that's within timestamp 300
        

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.hitCounter.append(timestamp)
        

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        while self.hitCounter:
            diff = timestamp - self.hitCounter[0]
            if diff >= 300: #if timestamp get over 300, delete from the queue
                self.hitCounter.popleft()
            else:
                break
        return len(self.hitCounter) #the length of the queue is the number of hits that's within timestamp 300
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)