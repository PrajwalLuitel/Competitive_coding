def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        print(f"nums[i-1] = {nums[i-1]}, i = {nums[i]}")
        if nums[i] == nums[i-1]:
            return True
    return False
     

my_numbers = [3,3]
print(f"{containsDuplicate(my_numbers)}")



def containsDuplicateUsingSet(nums: list[int]) -> bool:
    my_set:set[int] = set()

    for num in nums:
        if num in my_set:
            return True
        else:
            my_set.add(num)
    return False

my_numbers = list(range(-22700, 29000))
print(f"using the set, we get: {containsDuplicateUsingSet(my_numbers)}")