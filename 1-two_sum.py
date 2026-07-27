class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i
            
        return []

if __name__ == "__main__":
    solution = Solution()
    print("Örnek 1: nums = [2, 7, 11, 15], target = 9")
    print("Çıktı:", solution.twoSum([2, 7, 11, 15], 9))
    
    print("\nÖrnek 2: nums = [3, 2, 4], target = 6")
    print("Çıktı:", solution.twoSum([3, 2, 4], 6))
    
    print("\nÖrnek 3: nums = [3, 3], target = 6")
    print("Çıktı:", solution.twoSum([3, 3], 6))
