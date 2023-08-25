def removeElement(nums: list[int], val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

print(removeElement([0,0,1,1,1,2,2,3,3,4]))