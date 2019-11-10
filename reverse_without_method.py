nums = [1,2,3,4,5,6,7]
nums_reverse = []
for i in range(1,len(nums)+1):
    nums_reverse.append(nums[-i])
print(nums_reverse)