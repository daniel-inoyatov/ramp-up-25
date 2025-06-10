def asc_des_none(nums:list, order:str):
    match order.lower():
        case 'asc':
            nums.sort()
        case 'des':
            nums.sort(reverse=True)
        case '_':
            return nums
    return nums
def main():
    ls = asc_des_none([3,2], 'asc')
    print(ls)
if __name__ == '__main__':
    main() 