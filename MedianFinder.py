# 295. Find Median from Data Stream
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []


     def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

         if(self.small and self.large and
                (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2


if __name__ == '__main__':
    # Input from the problem description
    commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    values = [[], [1], [2], [], [3], []]

    output = []
    median_finder_obj = None

    # Process each command and store the result
    for i, command in enumerate(commands):
        if command == "MedianFinder":
            median_finder_obj = MedianFinder()
            output.append(None)
        elif command == "addNum":
            if median_finder_obj:
                median_finder_obj.addNum(values[i][0])
            output.append(None)
        elif command == "findMedian":
            if median_finder_obj:
                median = median_finder_obj.findMedian()
                output.append(median)
            else:
                output.append(None)

     # Format the final list to match the desired output style
    def format_output(results):
        formatted_results = []
        for res in results:
            if res is None:
                formatted_results.append("null")
            else:
                # Format floating point numbers to 5 decimal places
                formatted_results.append(f"{res:.5f}")
        return f"[{','.join(formatted_results)}]"

    print("Output is : ", format_output(output))


