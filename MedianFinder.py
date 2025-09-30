# 295. Find Median from Data Stream
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []


     def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
