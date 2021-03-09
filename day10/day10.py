file = open('input.txt', 'r')

nums = [int(i) for i in file]
nums.append(0)
nums = sorted(nums)
steps = {1:0, 2:0, 3:1}
for i in range(len(nums)-1):
    diff = nums[i+1] - nums[i]
    steps[diff] += 1
print("Part 1 Result : ", steps[1] * steps[3])

def computeK(cards, c, index):
    k = 0
    for child in c:
        k += cards[child]
    cards[index] = k

#Part 2
children = {}
for i, val in enumerate(nums):
    nexts = []
    j = 1
    while i+j < len(nums) and nums[i+j] - val <= 3:
        nexts.append(nums[i+j])
        j += 1
    children[val] = nexts

highestNumber = nums[-1]
cards = {highestNumber:1}

for val in reversed(nums):
    if val == highestNumber:
        continue
    computeK(cards, children[val], val)
computeK(cards, children[0], 0)

print("Nb of possible combinations :", cards[0])
