class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        
        heap = [(-val,key) for key,val in c.items()] 
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]