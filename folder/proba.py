nums = [2,7,11,15,5,4,6,3]
target = 9
output = []

for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if nums[i] + nums[j] == target :
            if nums[i] not in output or nums[j] not in output:
                output.append(nums[i])
                output.append(nums[j])
                print(output)

