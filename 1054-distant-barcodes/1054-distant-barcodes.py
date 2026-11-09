class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        hashmap = {}
        for barcode in barcodes:
            if barcode not in hashmap:
                hashmap[barcode] = 1
            else:
                hashmap[barcode] += 1
        
        max_heap = []
        for barcode, frequency in hashmap.items():
            heapq.heappush(max_heap, (-frequency, barcode))
        
        result = []
        prev_freq = 0
        prev_barcode = -1
        while max_heap:
            freq, barcode = heapq.heappop(max_heap)
            result.append(barcode)
            freq += 1

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_barcode))

            prev_freq = freq
            prev_barcode = barcode
        
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna