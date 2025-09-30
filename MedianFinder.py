# 295. Find Median from Data Stream
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
