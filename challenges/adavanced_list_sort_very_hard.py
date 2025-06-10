def advanced_sort(nums:list):
    nums.sort(reverse=True)
    numMap = {}
    for n in nums:
        numMap[n]=numMap.get(n,0)+1
    output = []
    for k in numMap.keys():
        output.append([k]*numMap[k])
    output.sort(reverse =True)
    return output
def main():
    print(advanced_sort([2, 1, 2, 1]))
main()